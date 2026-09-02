#!/usr/bin/env python3
"""
ste_check.py — mechanical checker for ASD-STE100 Issue 9 Simplified Technical English.

Usage:
  python3 ste_check.py FILE [--mode procedural|descriptive|auto] [--glossary TERMS.txt] [--json]
  python3 ste_check.py --lookup WORD [WORD ...]
  cat text.md | python3 ste_check.py -

What it checks (rule numbers refer to ASD-STE100 Issue 9, Part 1):
  Words     non-approved words with their approved alternatives (1.1–1.3, 9.1)
            words not in the dictionary at all (must be technical nouns/verbs, 1.5/1.12, or replaced)
  Verbs     -ing verb forms (3.5), have/has/had + participle (3.4), passive voice (3.6),
            be/must/can + "to be" + participle (3.4)
  Sentences word count > 20 procedural / > 25 descriptive, counted per rules 8.4–8.7
            semicolons (8.1), contractions (4.2), Latin abbreviations e.g./i.e./etc. (GR-6)
            possible multi-word nouns of 4+ words (2.1)
            gendered pronouns he/she/him/her (GR-3, GR-7)
  Paragraphs more than 6 sentences (6.6)

It is a heuristic, not a parser. It will produce some false positives (a noun mistaken
for a verb, a technical noun it cannot know). Use `--glossary` to give it your approved
technical nouns and verbs (one per line, multi-word allowed) so it stops flagging them.
The final judgement is the writer's.
"""
import argparse, json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
DICT_PATH = os.path.join(HERE, "dictionary.json")

# ---------------------------------------------------------------- dictionary

def load_dict():
    with open(DICT_PATH, encoding="utf-8") as f:
        d = json.load(f)
    approved = {}       # lower word -> list of entries
    non_approved = {}   # lower word -> list of entries
    for e in d["approved"]:
        approved.setdefault(e["word"].lower(), []).append(e)
    for e in d["non_approved"]:
        w = re.sub(r"\s*\(.*?\)\s*", " ", e["word"]).strip().lower()  # 'few (a few)' -> 'few'
        non_approved.setdefault(w, []).append(e)
        if w != e["word"].lower():
            non_approved.setdefault(e["word"].lower(), []).append(e)
    return approved, non_approved


def plural_forms(w):
    out = {w + "s"}
    if re.search(r"(s|x|z|ch|sh)$", w):
        out.add(w + "es")
    if re.search(r"[^aeiou]y$", w):
        out.add(w[:-1] + "ies")
    if w.endswith("f"):
        out.add(w[:-1] + "ves")
    if w.endswith("fe"):
        out.add(w[:-2] + "ves")
    return out


def build_form_index(approved):
    """Map every permitted surface form -> base approved word."""
    forms = {}
    for base, entries in approved.items():
        for e in entries:
            forms.setdefault(base, base)
            pos = e["pos"]
            extra = (e.get("forms", "") + " " + e.get("note", "")).lower()
            # verb forms and adjective comparatives are listed as UPPERCASE tokens
            for tok in re.findall(r"[a-z][a-z'\-]*", extra):
                tok = tok.strip()
                if tok in ("no", "other", "verb", "forms", "also", "for", "example", "use", "this",
                           "word", "only", "as", "an", "adjective", "or", "the", "a", "in", "of", "not",
                           "to", "do", "with", "that", "is", "it", "you", "and", "when", "but", "form",
                           "same", "plural", "noun", "singular", "adverb", "these", "words", "before",
                           "after", "used", "meaning", "meanings", "sense", "context", "refer"):
                    continue
                if len(tok) > 1:
                    forms.setdefault(tok, base)
            if pos == "n":
                for p in plural_forms(base):
                    forms.setdefault(p, base)
            if pos == "v" and not e.get("forms"):
                # regular verb without explicit forms listed: allow -s/-ed
                forms.setdefault(base + "s", base)
                forms.setdefault(base + "ed", base)
    for f_ in ("is", "was", "are", "were", "be"):
        forms[f_] = "be"
    # multi-word approved entries (MAKE SURE, AWAY FROM, ...) are also inflected
    forms.setdefault("makes sure", "make sure")
    forms.setdefault("made sure", "make sure")
    return forms


# words the standard lists as the ONLY approved -ing forms (Rule 3.5)
APPROVED_ING = {"lighting", "opening", "routing", "servicing", "mating", "missing",
                "remaining", "something", "during", "during"}

IRREGULAR_PARTICIPLES = {"been", "done", "given", "gone", "made", "put", "set", "shown", "seen",
                         "held", "kept", "known", "taken", "written", "broken", "cut", "let",
                         "read", "sent", "spent", "left", "found", "got", "worn", "torn", "bent",
                         "built", "lost", "run", "won", "begun", "become", "come", "drawn",
                         "driven", "fallen", "flown", "frozen", "hidden", "hit", "led", "lit",
                         "met", "paid", "said", "sold", "spoken", "stuck", "thrown", "understood",
                         "hung", "shut", "spread", "split"}

BE_FORMS = {"is", "are", "was", "were", "be", "been", "being", "am"}
NUMBER_WORDS = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                "hundred", "thousand", "million", "half", "quarter", "third", "fourth", "fifth"}
DETERMINERS = {"the", "a", "an", "this", "these", "its", "their", "your", "our", "each",
               "all", "some", "many", "no", "of", "front", "rear", "top", "bottom", "left", "right",
               "new", "old", "primary", "applicable", "correct", "two", "three", "four", "five", "six"}
HAVE_FORMS = {"have", "has", "had"}
# words that are always verbs in practice: modals plus common verbs with no noun sense
ALWAYS_VERB = {"may", "might", "should", "would", "could", "shall", "ought", "ensure", "take", "perform",
               "provide", "obtain", "require", "allow", "enable", "indicate", "occur", "avoid", "achieve",
               "verify", "confirm", "assure", "determine", "establish", "maintain", "prevent", "proceed",
               "remain", "become", "seem", "appear", "consist", "contain", "possess", "acquire", "utilize",
               "utilise", "employ", "conduct", "carry", "commence", "cease", "terminate", "initiate",
               "activate", "deactivate", "locate", "relocate", "accomplish", "facilitate", "eliminate",
               "exceed", "persist", "arise", "happen", "depend", "rely", "refer", "reinstall", "retighten"}
CONTRACTION_RE = re.compile(r"\b\w+'(t|s|re|ve|ll|d|m)\b", re.I)
LATIN_RE = re.compile(r"\b(e\.g\.|i\.e\.|etc\.?|et al\.?|vs\.|viz\.)", re.I)
GENDER_RE = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)

# tokens that count as one word under rules 8.5–8.7 (numbers, units, ids, abbreviations, parentheses)
UNIT_RE = r"(?:°[CF]|%|mm|cm|m|km|in|ft|kg|g|lb|lbs|oz|psi|kpa|mpa|bar|nm|n|v|kv|mv|a|ma|ka|w|kw|mw|hz|khz|mhz|ghz|ohm|ohms|Ω|s|ms|min|h|hr|hrs|l|ml|gal|rpm|db|c|f|k)"
ONE_WORD_RE = re.compile(
    r"\([^()]*\)"                                   # parenthetical (rule 8.5)
    r"|\"[^\"]+\"|“[^”]+”"                          # quoted text (8.6)
    r"|[+\-−]?\d[\d,.:/]*\s?" + UNIT_RE + r"\b"     # number + unit (8.6)
    r"|[+\-−]?\d[\d,.:/]*"                          # number (8.6)
    r"|\b[A-Z0-9][A-Z0-9\-/.]*\d[A-Z0-9\-/.]*\b"    # alphanumeric identifier (8.6)
    r"|\b[A-Z]{2,}(?:[-/][A-Z0-9]+)*\b"             # abbreviation / all-caps quoted label (8.6)
    r"|\b\w+(?:-\w+)+\b"                            # hyphenated word (8.7)
    r"|\b[\w']+\b",
    re.UNICODE)


def count_words(sentence):
    """STE word count: parentheses, numbers+units, identifiers, abbreviations, quotes, hyphenated = 1."""
    s = sentence.strip()
    # drop list markers / step numbers (rule 8.6 note: numbering of steps is not counted)
    s = re.sub(r"^\s*(\(?[0-9a-zA-Z]{1,3}[.)]|[-•*–]|\d+\.)\s+", "", s)
    s = re.sub(r"^(WARNING|CAUTION|NOTE|DANGER|NOTICE)\s*:\s*", "", s, flags=re.I)
    toks = [t for t in ONE_WORD_RE.findall(s) if re.search(r"[\w\d]", t)]
    return len(toks)


# ---------------------------------------------------------------- text segmentation

def split_paragraphs(text):
    paras, cur = [], []
    for line in text.splitlines():
        if line.strip() == "":
            if cur:
                paras.append(cur); cur = []
        else:
            cur.append(line)
    if cur:
        paras.append(cur)
    return paras


def is_list_item(line):
    return bool(re.match(r"^\s*(\(?[0-9a-zA-Z]{1,3}[.)]|[-•*–]|\d+\.)\s+", line))


def is_heading(line):
    return bool(re.match(r"^\s*#{1,6}\s", line)) or (len(line.split()) <= 8 and line.strip() == line.strip().title() and not line.strip().endswith("."))


ABBR_PROTECT = ["e.g.", "i.e.", "etc.", "No.", "Fig.", "fig.", "a.m.", "p.m.", "vs.", "approx.", "max.", "min."]


def split_sentences(block):
    """Split a text block into sentences. A colon that ends a list intro ends a sentence (8.4)."""
    t = block
    for a in ABBR_PROTECT:
        t = t.replace(a, a.replace(".", "<DOT>"))
    t = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)
    parts = re.split(r"(?<=[.!?:])\s+(?=[\"“(]?[A-Z0-9])", t)
    out = []
    for p in parts:
        p = p.replace("<DOT>", ".").strip()
        if p:
            out.append(p)
    return out


# ---------------------------------------------------------------- checks

class Checker:
    def __init__(self, mode="auto", glossary=None):
        self.approved, self.non_approved = load_dict()
        self.forms = build_form_index(self.approved)
        self.mode = mode
        self.glossary = set()
        self.glossary_multi = []
        for g in (glossary or []):
            g = g.strip().lower()
            if not g or g.startswith("#"):
                continue
            self.glossary.add(g)
            for p in plural_forms(g):
                self.glossary.add(p)
            if " " in g:
                self.glossary_multi.append(g)
                self.glossary_multi.extend(plural_forms(g))
        self.findings = []
        self.word_hits = OrderedDict()   # word -> {kind, alts, count, example}

    # -- helpers
    def add(self, rule, kind, msg, where):
        self.findings.append({"rule": rule, "kind": kind, "message": msg, "where": where})

    def lookup_base(self, tok):
        """Return ('approved', base) / ('non_approved', base) / ('unknown', tok)."""
        t = tok.lower()
        if t in self.glossary:
            return ("glossary", t)
        if t in self.forms:
            return ("approved", self.forms[t])
        if t in self.non_approved:
            return ("non_approved", t)
        # try simple de-inflection
        for suf, repl in (("ies", "y"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("ing", ""), ("ing", "e"), ("er", ""), ("est", ""), ("ly", "")):
            if t.endswith(suf) and len(t) > len(suf) + 2:
                b = t[: -len(suf)] + repl
                if b in self.forms:
                    return ("approved-inflected", self.forms[b])
                if b in self.non_approved:
                    return ("non_approved", b)
        return ("unknown", t)

    def sentence_mode(self, sent, para_is_list):
        if self.mode in ("procedural", "descriptive"):
            return self.mode
        # auto: imperative opener, list step, or safety word -> procedural
        first = re.sub(r"^\s*(\(?[0-9a-zA-Z]{1,3}[.)]|[-•*–]|\d+\.)\s+", "", sent)
        first = re.sub(r"^(WARNING|CAUTION|DANGER)\s*:\s*", "", first, flags=re.I)
        w = re.findall(r"[A-Za-z']+", first)
        if re.match(r"^(NOTE)\s*:", sent, re.I):
            return "descriptive"
        if not w:
            return "descriptive"
        head = w[0].lower()
        # condition-first imperative: "If/When/Before ..., do X"
        if head in ("if", "when", "before", "after", "while", "until", "unless"):
            m = re.search(r",\s*([A-Za-z']+)", first)
            if m and self.is_verb(m.group(1)):
                return "procedural"
        if head in ("do", "make", "put", "set", "remove", "install", "connect", "disconnect", "turn", "press", "push", "pull", "open", "close", "start", "stop", "use", "apply", "examine", "measure", "tighten", "loosen", "attach", "hold", "keep", "wait", "read", "refer", "record", "replace", "discard", "clean", "fill", "drain", "lift", "lower", "move", "operate", "energize", "de-energize", "obey", "get", "go", "let", "cut", "lubricate", "tag", "torque", "adjust", "align", "release", "engage", "disengage", "select", "touch", "enter", "type", "click", "tap", "swipe", "scroll", "save", "download", "upload", "reboot", "restart", "update", "insert", "mount", "unscrew", "screw", "supply", "send", "give", "show", "write", "add", "count", "identify", "compare", "continue", "repeat", "always", "never", "only", "carefully", "slowly", "immediately", "then", "first", "also"):
            return "procedural"
        if head == "do" or (self.is_verb(head) and head not in ("it", "this", "there")):
            return "procedural"
        return "descriptive"

    def is_verb(self, w):
        w = w.lower()
        return any(e["pos"] == "v" for e in self.approved.get(self.forms.get(w, w), []))

    # -- main
    def check(self, text):
        paras = split_paragraphs(text)
        sent_no = 0
        for pi, lines in enumerate(paras, 1):
            list_lines = [l for l in lines if is_list_item(l)]
            para_is_list = len(list_lines) >= max(1, len(lines) // 2)
            heading_only = len(lines) == 1 and is_heading(lines[0])
            if heading_only:
                continue
            # sentences: list items are individual sentences (8.4)
            sentences = []
            if para_is_list:
                for l in lines:
                    sentences.extend(split_sentences(l))
            else:
                sentences = split_sentences(" ".join(l.strip() for l in lines))
            if not para_is_list and len(sentences) > 6:
                self.add("6.6", "paragraph", f"Paragraph {pi} has {len(sentences)} sentences (max 6). Divide it.", f"para {pi}")
            for s in sentences:
                sent_no += 1
                self.check_sentence(s, pi, sent_no, para_is_list)
        return self.report()

    def check_sentence(self, s, pi, n, para_is_list):
        where = f"para {pi}, sentence {n}"
        short = s if len(s) <= 90 else s[:87] + "..."
        mode = self.sentence_mode(s, para_is_list)
        limit = 20 if mode == "procedural" else 25
        wc = count_words(s)
        if wc > limit:
            self.add("5.1" if mode == "procedural" else "6.3", "length",
                     f"{wc} words ({mode}, max {limit}): \"{short}\"", where)
        if ";" in s:
            self.add("8.1", "punctuation", f"Semicolon: \"{short}\"", where)
        m = CONTRACTION_RE.search(s)
        if m and not re.search(r"\w's\b", m.group(0)):  # possessive 's is allowed (GR-8)
            self.add("4.2", "contraction", f"Contraction \"{m.group(0)}\": write the words in full.", where)
        elif m and re.search(r"\b(it's|let's|that's|there's|what's|here's|who's)\b", s, re.I):
            self.add("4.2", "contraction", f"Contraction in: \"{short}\"", where)
        m = LATIN_RE.search(s)
        if m:
            self.add("GR-6", "latin", f"Latin abbreviation \"{m.group(0)}\": use \"for example\", \"that is\", or rewrite.", where)
        m = GENDER_RE.search(s)
        if m:
            self.add("GR-7", "pronoun", f"Gender-specific pronoun \"{m.group(0)}\": STE does not permit he/she. Use \"the operator\", \"you\", \"they\".", where)

        # tokens for word-level checks: strip parentheticals ids, quoted text, numbers
        body = re.sub(r"\([^()]*\)", " ", s)
        body = re.sub(r"\"[^\"]+\"|“[^”]+”", " ", body)
        body = re.sub(r"^\s*(\(?[0-9a-zA-Z]{1,3}[.)]|[-•*–]|\d+\.)\s+", "", body)
        body = re.sub(r"^(WARNING|CAUTION|NOTE|DANGER|NOTICE)\s*:", "", body, flags=re.I)
        # protect glossary multi-word terms (case-insensitive)
        work = body
        for g in sorted(self.glossary_multi, key=len, reverse=True):
            work = re.sub(r"\b" + re.escape(g) + r"\b", "GLOSSARYTERM", work, flags=re.I)
        for mw in ("make sure", "makes sure", "made sure", "away from", "out of", "in front of", "because of", "adjacent to", "each other", "in progress", "put on", "come on", "go off", "aft of", "forward of", "inboard of", "outboard of", "upstream of", "downstream of", "for example", "as a result", "at the same time"):
            work = re.sub(r"\b" + mw + r"\b", mw.replace(" ", "_"), work, flags=re.I)
        raw = re.findall(r"[A-Za-z][A-Za-z'\-_]*", work)
        tokens = []
        for idx, tok in enumerate(raw):
            if tok == "GLOSSARYTERM":
                tokens.append("_glossary_"); continue
            if "'" in tok:            # contractions are reported separately (4.2); possessives are fine (GR-8)
                if tok.lower().endswith("n't") or tok.lower() in ("it's", "let's", "that's", "there's", "what's", "here's", "who's"):
                    continue
                tok = tok.split("'")[0]
                if not tok:
                    continue
            if len(tok) > 1 and tok.isupper():
                continue              # abbreviation / quoted label (8.6)
            if idx > 0 and tok[0].isupper() and not tok.isupper() and "_" not in tok:
                # capitalized mid-sentence: proper noun or product name (TN category 11) — keep
                # but mark so word-approval is skipped
                tokens.append("_proper_:" + tok.lower()); continue
            tokens.append(tok.lower())

        prev = None
        prev2 = None
        run_nouns = []
        for i, tok in enumerate(tokens):
            if tok == "_glossary_":
                run_nouns.append("<term>"); prev2, prev = prev, "term"; continue
            if tok.startswith("_proper_:"):
                run_nouns.append(tok[9:]); prev2, prev = prev, tok[9:]; continue
            t = tok.replace("_", " ")
            if len(t) < 2:
                prev2, prev = prev, t
                continue
            if " " in t:  # multi-word approved phrase
                prev2, prev = prev, t
                run_nouns = []
                continue
            if t in NUMBER_WORDS:
                run_nouns.append(t); prev2, prev = prev, t; continue
            if t in ("been", "being"):
                self.add("3.4", "tense", f"\"{t}\": not an approved form of BE (only be, is, are, was, were). Rewrite without it.", where)
                prev2, prev = prev, t
                continue
            kind, base = self.lookup_base(t)
            # part-of-speech heuristic: a word after a determiner/adjective is used as a noun.
            # If it is non-approved only as a verb (or only as an adjective) that finding is moot.
            VERB_SLOT = {"to", "you", "we", "they", "it", "can", "will", "must", "not", "do", "does",
                         "did", "and", "then", "or", "always", "never", "carefully", "slowly", "immediately", "also", "only"}
            verb_only_note = ""
            if kind == "non_approved" and prev in DETERMINERS:
                entries = self.non_approved[base]
                poses = {e["pos"] for e in entries}
                if poses <= {"v"}:
                    approved_noun = any(e["pos"] == "n" for e in self.approved.get(base, []))
                    listed_tn = any(a.endswith("(TN)") for e in entries for a in e["use_instead"])
                    kind = "approved" if (approved_noun or listed_tn) else "unknown"
            elif kind == "non_approved" and i > 0 and prev not in VERB_SLOT:
                entries = self.non_approved[base]
                poses = {e["pos"] for e in entries}
                nounish = any(e["pos"] == "n" for e in self.approved.get(base, [])) or any(a.endswith("(TN)") for e in entries for a in e["use_instead"])
                looks_verb = base in ALWAYS_VERB or re.search(r"(ize|ise|ify|ate|en)$", base) or (base.startswith("re") and base[2:] in self.approved)
                if poses <= {"v"} and not looks_verb and (nounish or not self.is_function(prev)):
                    verb_only_note = "verb-only"

            # -ing forms (3.5)
            if t.endswith("ing") and t not in APPROVED_ING and t not in self.glossary and kind != "glossary":
                nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
                if prev in DETERMINERS or (nxt and not self.is_function(nxt) and not self.is_verb(nxt) and nxt not in BE_FORMS):
                    self.add("3.5?", "ing", f"\"-ing\" word \"{t}\": permitted only if it is a technical noun or a modifier in one (\"wiring diagram\"). Confirm, else rewrite.", where)
                else:
                    self.add("3.5", "ing", f"\"-ing\" verb form \"{t}\": not permitted. Rewrite with a simple tense (\"when you do\", not \"when doing\").", where)

            # complex tenses (3.4) and passive (3.6)
            if prev in HAVE_FORMS and (t.endswith("ed") or t in IRREGULAR_PARTICIPLES) and t not in ("need",):
                self.add("3.4", "tense", f"\"{prev} {t}\": perfect tense is not approved. Use the simple past or present.", where)
            if prev in BE_FORMS and (t.endswith("ed") or t in IRREGULAR_PARTICIPLES):
                # past participle after "be" may be an adjective (3.3). Flag as passive only when
                # followed by "by", or when the verb is a clear action verb.
                nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
                if nxt == "by":
                    self.add("3.6", "passive", f"Passive voice \"{prev} {t} by\": make the agent the subject.", where)
                else:
                    self.add("3.6?", "passive", f"\"{prev} {t}\": passive voice, or a past participle used as an adjective (permitted, 3.3)? Confirm. In procedures, use the imperative.", where)
            if prev == "be" and prev2 in ("must", "can", "will", "should", "to"):
                pass  # covered above via BE_FORMS

            # word approval
            if kind == "non_approved":
                entries = self.non_approved[base]
                alts = "; ".join(", ".join(e["use_instead"]) or e.get("note", "") for e in entries)
                key = base
                h = self.word_hits.setdefault(key, {"kind": "maybe_noun" if verb_only_note else "non_approved", "alts": alts, "count": 0, "example": short, "pos": "/".join(e["pos"] for e in entries)})
                h["count"] += 1
            elif kind == "unknown":
                key = base
                h = self.word_hits.setdefault(key, {"kind": "unknown", "alts": "", "count": 0, "example": short, "pos": ""})
                h["count"] += 1

            # multi-word noun heuristic (2.1): 4+ consecutive content words with no function word
            is_content = kind in ("unknown", "glossary", "approved", "approved-inflected", "non_approved") and not self.is_function(base)
            if is_content and not self.is_verb(base):
                run_nouns.append(t)
            else:
                if len(run_nouns) >= 4:
                    self.add("2.1", "noun-cluster", f"Possible multi-word noun of {len(run_nouns)} words: \"{' '.join(run_nouns)}\". Max 3 — use prepositions or hyphens (2.2).", where)
                run_nouns = []
            prev2, prev = prev, t
        if len(run_nouns) >= 4:
            self.add("2.1", "noun-cluster", f"Possible multi-word noun of {len(run_nouns)} words: \"{' '.join(run_nouns)}\". Max 3 — use prepositions or hyphens (2.2).", where)

    def is_function(self, w):
        for e in self.approved.get(w, []):
            if e["pos"] in ("prep", "conj", "art", "pron", "adv"):
                return True
        return w in ("a", "an", "the", "and", "or", "of", "to", "in", "on", "at", "for", "with", "by", "from", "as", "is", "are", "was", "were", "be", "not", "no", "if", "when", "that", "this", "these", "it", "you", "we", "they", "than", "then", "thus", "but", "also", "only", "each", "all", "its", "their")

    # -- output
    def report(self):
        return {"findings": self.findings, "words": self.word_hits}


def format_report(rep, text):
    out = []
    f = rep["findings"]
    words = rep["words"]
    na = {k: v for k, v in words.items() if v["kind"] == "non_approved"}
    unk = {k: v for k, v in words.items() if v["kind"] == "unknown"}
    maybe = {k: v for k, v in words.items() if v["kind"] == "maybe_noun"}
    n_sent = sum(1 for _ in f)  # placeholder
    out.append("ASD-STE100 CHECK")
    out.append("=" * 60)
    out.append(f"Structure/grammar findings: {len(f)}   Non-approved words: {len(na)}   Words not in dictionary: {len(unk)}")
    out.append("")
    if na:
        out.append("NON-APPROVED WORDS (Rules 1.1–1.3, 9.1) — replace or restructure")
        out.append("-" * 60)
        for w, h in sorted(na.items(), key=lambda kv: -kv[1]["count"]):
            out.append(f"  {w} ({h['pos']}) x{h['count']}  ->  {h['alts']}")
        out.append("")
    if maybe:
        out.append("NOT APPROVED AS A VERB — fine if used as a noun / technical noun here; otherwise replace")
        out.append("-" * 60)
        for w, h in sorted(maybe.items(), key=lambda kv: -kv[1]["count"]):
            out.append(f"  {w} x{h['count']}  ->  as a verb use: {h['alts']}")
        out.append("")
    if unk:
        out.append("WORDS NOT IN THE DICTIONARY — each must be a technical noun/verb (Rules 1.5, 1.12) or be replaced")
        out.append("-" * 60)
        out.append("  " + ", ".join(f"{w} x{h['count']}" for w, h in sorted(unk.items(), key=lambda kv: -kv[1]["count"])))
        out.append("  (Add legitimate technical terms to a glossary file and pass --glossary to silence them.)")
        out.append("")
    if f:
        out.append("STRUCTURE AND GRAMMAR")
        out.append("-" * 60)
        order = {"length": 0, "paragraph": 1, "tense": 2, "passive": 3, "ing": 4, "punctuation": 5, "contraction": 6, "noun-cluster": 7, "latin": 8, "pronoun": 9}
        for x in sorted(f, key=lambda x: (order.get(x["kind"], 99), x["where"])):
            out.append(f"  [{x['rule']}] {x['message']}   ({x['where']})")
        out.append("")
    if not f and not na and not unk:
        out.append("No findings. The text passes the mechanical checks. Still read it against the rules that no script can check (one topic per sentence, condition first, notes vs. instructions, approved meaning of each word).")
    return "\n".join(out)


def do_lookup(words):
    approved, non_approved = load_dict()
    forms = build_form_index(approved)
    for w in words:
        w = w.lower().strip()
        base = forms.get(w, w)
        print(f"== {w} ==")
        hit = False
        for e in approved.get(base, []):
            hit = True
            print(f"  APPROVED  {e['word']} ({e['pos']}): {'; '.join(e['meaning'])}")
            if e.get("forms"): print(f"    forms: {e['forms']}")
            if e.get("note"): print(f"    note: {e['note']}")
            if e.get("for_other_meanings_use"): print(f"    for other meanings use: {e['for_other_meanings_use']}")
            for ex in e.get("examples", [])[:2]: print(f"    e.g. {ex}")
        for e in non_approved.get(w, []) + ([] if base == w else non_approved.get(base, [])):
            hit = True
            print(f"  NOT APPROVED  {e['word']} ({e['pos']})  ->  {', '.join(e['use_instead']) or ''} {e.get('note', '')}")
            for a, b in zip(e.get("ste_example", []), e.get("non_ste_example", []) or [""] * 3):
                print(f"    STE: {a}")
                if b: print(f"    not: {b}")
        if not hit:
            # try de-inflecting
            for suf, repl in (("ies", "y"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("ing", ""), ("ing", "e")):
                if w.endswith(suf):
                    b = w[: -len(suf)] + repl
                    if b in approved or b in non_approved:
                        print(f"  (see \"{b}\")"); do_lookup([b]); hit = True; break
        if not hit:
            print("  Not in the STE dictionary. Permitted only as a technical noun (Rule 1.5) or technical verb (Rule 1.12), otherwise replace it.")
        print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="text/markdown file to check, or - for stdin")
    ap.add_argument("--mode", choices=["procedural", "descriptive", "auto"], default="auto")
    ap.add_argument("--glossary", help="file with approved technical nouns/verbs, one per line")
    ap.add_argument("--lookup", nargs="+", help="print dictionary entries for these words and exit")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()
    if a.lookup:
        do_lookup(a.lookup); return
    if not a.file:
        ap.print_help(); sys.exit(1)
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    glossary = open(a.glossary, encoding="utf-8").read().splitlines() if a.glossary else []
    c = Checker(mode=a.mode, glossary=glossary)
    rep = c.check(text)
    if a.json:
        print(json.dumps(rep, indent=1, ensure_ascii=False))
    else:
        print(format_report(rep, text))


if __name__ == "__main__":
    main()
