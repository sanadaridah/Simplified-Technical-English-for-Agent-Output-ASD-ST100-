#!/usr/bin/env python3
"""
build_dictionary.py — rebuild scripts/dictionary.json and the two dictionary reference
files from an official ASD-STE100 Issue 9 PDF.

Usage:
    python3 tools/build_dictionary.py ASDSTE100_ISSUE9.pdf [--out <skill root>]

Requires: pdfplumber  (pip install pdfplumber)

The PDF is not stored in this repository. Request it free of charge from
https://www.asd-ste100.org/STE_downloads.html and keep it on your own machine.
The layout parser targets Issue 9 (2025-01-15): Part 2 starts on PDF page 149 and
runs to page 434; the four dictionary columns are located from the header words
"Word", "Approved", "STE", "Non-STE" on each page. A new issue will need the page
range (FIRST/LAST) and possibly the layout heuristics revisited.
"""
import argparse, json, os, re, sys
from collections import defaultdict
try:
    import pdfplumber
except ImportError:
    sys.exit("pdfplumber is required: pip install pdfplumber")

FIRST, LAST = 148, 433  # 0-based page indexes of the Part 2 dictionary body (Issue 9)


POS = r"\((?:v|n|adj|adv|prep|pron|conj|art|TN|TV|prefix)\)"
head_re = re.compile(r"^(?P<word>[A-Za-z][A-Za-z'\-/ .()]*?)\s*(?P<pos>" + POS + r")\s*,?\s*$")
bare_pos = re.compile(r"^" + POS + r"\s*,?\s*$")
plain_word = re.compile(r"^[A-Za-z][A-Za-z'\-/ .()]*$")


def parse(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    entries = []
    cur = None

    def flush():
        nonlocal cur
        if cur:
            entries.append(cur)
        cur = None

    for pi in range(FIRST, LAST + 1):


        page = pdf.pages[pi]
        words = page.extract_words(keep_blank_chars=False, use_text_flow=False)
        # header positions
        hx = {}
        for w in words:
            if w['top'] < 90:
                if w['text'] == 'Word': hx['c1'] = w['x0']
                if w['text'] == 'Approved': hx['c2'] = w['x0']
                if w['text'] == 'STE' and 'c3' not in hx: hx['c3'] = w['x0']
                if w['text'] == 'Non-STE': hx['c4'] = w['x0']
        if len(hx) < 4:
            continue  # not a dictionary page (e.g. blank page)
        b2 = hx['c2'] - 6; b3 = hx['c3'] - 6; b4 = hx['c4'] - 6
        # group into rows by top (tolerance 3)
        rows = defaultdict(list)
        for w in words:
            if w['top'] < 90 or w['top'] > 740:  # skip header/footer
                continue
            key = None
            for k in rows:
                if abs(k - w['top']) <= 3:
                    key = k; break
            rows[key if key is not None else w['top']].append(w)
        rowlist = []
        for top in sorted(rows):
            r = sorted(rows[top], key=lambda w: w['x0'])
            rowlist.append(r)
        # merge a plain-word col1 row with a following bare-pos col1 row
        merged = []
        i = 0
        while i < len(rowlist):
            r = rowlist[i]
            c1 = " ".join(w['text'] for w in r if w['x0'] < b2).strip()
            if i + 1 < len(rowlist):
                n = rowlist[i+1]
                n1 = " ".join(w['text'] for w in n if w['x0'] < b2).strip()
                if c1 and plain_word.match(c1) and not head_re.match(c1) and bare_pos.match(n1) and c1 not in ("No other verb","forms.","For other","meanings, use:") and not c1.endswith(','):
                    # attach pos tokens to r, drop from n
                    for w in n:
                        if w['x0'] < b2: r.append(w)
                    rowlist[i+1] = [w for w in n if w['x0'] >= b2]
            merged.append(r)
            i += 1
        for r in merged:
            cols = {1: [], 2: [], 3: [], 4: []}
            for w in r:
                x = w['x0']
                c = 1 if x < b2 else 2 if x < b3 else 3 if x < b4 else 4
                cols[c].append(w['text'])
            c1 = " ".join(cols[1]).strip()
            c2 = " ".join(cols[2]).strip()
            c3 = " ".join(cols[3]).strip()
            c4 = " ".join(cols[4]).strip()
            if c1 in ("Blank Page",) or c1.startswith("Page ") or c1.startswith("Issue"):
                continue
            for k in ("c1","c2","c3","c4"):
                pass
            c1, c2, c3, c4 = [re.sub(r"\b2025-01-15\b|\bIssue 9\b|Page 2-1-[A-Z0-9]+|Part 2 - Dictionary", "", t).strip() for t in (c1,c2,c3,c4)]
            m = head_re.match(c1)
            if m:
                flush()
                word = m.group('word').strip()
                cur = {"word": word, "pos": m.group('pos').strip("()"),
                       "approved": word == word.upper() and any(ch.isalpha() for ch in word),
                       "col1_extra": [], "col2": [], "ste_example": [], "non_ste_example": [],
                       "page": pi + 1}
                c1 = ""
            if cur is None:
                continue
            if c1: cur["col1_extra"].append(c1)
            if c2: cur["col2"].append(c2)
            if c3: cur["ste_example"].append(c3)
            if c4: cur["non_ste_example"].append(c4)


    flush()
    return entries


POS_TOKEN = re.compile(r"\b([A-Z][A-Z'\-]+(?: [A-Z][A-Z'\-]+)*) \((v|n|adj|adv|prep|pron|conj|art|TN|TV)\)")


def join(lines):
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def split_examples(lines):
    text = join(lines)
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", text)
    return [p.strip() for p in parts if p.strip()]


def clean(raw, OUT):
    approved, nonapproved = [], []
    for x in raw:
        word = x['word']
        col1 = x['col1_extra']
        col2 = join(x['col2'])
        if x['approved']:
            forms, notes = [], []
            for l in col1:
                if re.match(r"^[A-Z][A-Z'\- ]*,?$", l.strip()) or re.match(r"^\(?also [A-Z, ]+\)?$", l):
                    forms.append(l.strip().rstrip(','))
                elif l.startswith('(') and l.endswith(')') and l.upper() == l:
                    forms.append(l.strip('()'))
                else:
                    notes.append(l)
            meanings = [m.strip() for m in re.split(r"\s*(?<!\d)\b\d\.\s+", col2) if m.strip()]
            restricted = None
            m = re.search(r"For other meanings,? use:?\s*(.*)$", col2)
            if m:
                restricted = m.group(1).strip()
                meanings = [re.sub(r"For other meanings,? use:?.*$", "", mm).strip() for mm in meanings]
                meanings = [mm for mm in meanings if mm]
            entry = {"word": word, "pos": x['pos'], "meaning": meanings}
            if forms: entry["forms"] = ", ".join(forms)
            if restricted: entry["for_other_meanings_use"] = restricted
            if notes: entry["note"] = join(notes)
            ex = split_examples(x['ste_example'])
            if ex: entry["examples"] = ex[:3]
            approved.append(entry)
        else:
            alts = [f"{w} ({p})" for w, p in POS_TOKEN.findall(col2)]
            note = POS_TOKEN.sub("", col2)
            note = re.sub(r"[\s,]+", " ", note).strip(" ,")
            entry = {"word": word, "pos": x['pos'], "use_instead": alts}
            if note and len(note) > 3: entry["note"] = note
            ste = split_examples(x['ste_example'])
            non = split_examples(x['non_ste_example'])
            if ste: entry["ste_example"] = ste[:3]
            if non: entry["non_ste_example"] = non[:3]
            nonapproved.append(entry)

    # --- known layout artefacts in Issue 9, fixed by hand ---
    # "chance (by chance) (n)" has its head split over two lines and is absorbed by "chafed"
    if not any(e['word'].startswith('chance') for e in nonapproved):
        nonapproved.append({"word": "chance (by chance)", "pos": "n", "use_instead": ["RISK (n)", "ACCIDENTALLY (adv)"],
                            "ste_example": ["IF THERE IS A RISK OF FUEL LEAKAGE, PUT A CONTAINER BELOW THE UNIT.", "IF THE LEVER MOVED ACCIDENTALLY, DO THE TEST AGAIN."],
                            "non_ste_example": ["If there is a chance of fuel leakage, put a container below the unit.", "If, by chance, the lever moved, do the test again."]})
    for e in nonapproved:
        if e['word'] == 'chafed':
            e['use_instead'] = ['WORN (adj)']; e['ste_example'] = e['ste_example'][:1]; e['non_ste_example'] = e['non_ste_example'][:1]
    # "UNSATISFAC-/TORY" is hyphenated across lines
    for e in approved:
        if e['word'] == 'TORY':
            e['word'] = 'UNSATISFACTORY'; e['meaning'] = ['Not satisfactory']
            e['examples'] = ['IF THE CONDITION OF THE FILTERS IS UNSATISFACTORY, REPLACE THEM.']
            e.pop('note', None)
    # "OF (prep)" is duplicated by a page break
    approved = [e for e in approved if e['word'] != 'UNSATISFAC-' and not (e['word'] == 'OF' and e['meaning'] == ['flow'])]

    json.dump({"source": "ASD-STE100 Issue 9 (2025-01-15), Part 2 Dictionary. Extracted for internal use.",
               "approved": approved, "non_approved": nonapproved},
              open(os.path.join(OUT, 'scripts', 'dictionary.json'), 'w'), indent=1, ensure_ascii=False)
    print(f'{len(approved)} approved, {len(nonapproved)} non-approved -> scripts/dictionary.json')
    return approved, nonapproved


def render_references(d, OUT):
    lines = ["# ASD-STE100 Issue 9 — Approved words (Part 2, Dictionary)", "",
             f"Extracted from ASD-STE100 Issue 9 (2025-01-15) for internal use. {len(d['approved'])} entries. Each approved word may be used ONLY as the part of speech and with the meaning given here (Rules 1.2, 1.3). Verb forms listed are the only forms permitted (Rule 1.4, 3.1). Nouns may take a regular plural. Where the entry says \"for other meanings use\", the word is restricted to the meaning shown.", "",
             "Lookup tip: `python3 scripts/ste_check.py --lookup <word>` prints the full entry with examples. Do not read this whole file into context; grep it or use the lookup.", "",
             "| Word (pos) | Approved meaning | Forms / notes |", "|---|---|---|"]
    for e in sorted(d['approved'], key=lambda e: (e['word'].lower(), e['pos'])):
        meaning = "; ".join(e['meaning']) if e['meaning'] else ""
        extra = []
        if e.get('forms'): extra.append(e['forms'])
        if e.get('note'): extra.append(e['note'])
        if e.get('for_other_meanings_use'): extra.append("For other meanings use: " + e['for_other_meanings_use'])
        lines.append(f"| {e['word']} ({e['pos']}) | {meaning.replace('|', '/')} | {' — '.join(extra).replace('|', '/')} |")
    open(os.path.join(OUT, 'references', 'approved-words.md'), 'w').write("\n".join(lines) + "\n")

    lines = ["# ASD-STE100 Issue 9 — Words that are NOT approved, with approved alternatives", "",
             f"Extracted from ASD-STE100 Issue 9 (2025-01-15) Part 2 for internal use. {len(d['non_approved'])} entries. A lowercase word here is not permitted in STE. Replace it with one of the UPPERCASE alternatives (word-for-word when the part of speech matches) or use a different sentence construction (Rule 9.1). (TN) = technical noun, (TV) = technical verb — permitted only under Rules 1.5/1.12.", "",
             "Lookup tip: `python3 scripts/ste_check.py --lookup <word>`. Do not read this whole file into context; grep it or use the lookup.", "",
             "| Not approved | Use instead | STE example |", "|---|---|---|"]
    for e in sorted(d['non_approved'], key=lambda e: (e['word'].lower(), e['pos'])):
        alts = ", ".join(e['use_instead']) if e['use_instead'] else ""
        if e.get('note'): alts = (alts + " — " if alts else "") + e['note']
        ex = " ".join(e.get('ste_example', [])[:2])
        lines.append(f"| {e['word']} ({e['pos']}) | {alts.replace('|', '/')} | {ex.replace('|', '/')} |")
    open(os.path.join(OUT, 'references', 'non-approved-words.md'), 'w').write("\n".join(lines) + "\n")
    print("-> references/approved-words.md, references/non-approved-words.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."), help="skill root (default: repo root)")
    a = ap.parse_args()
    OUT = os.path.abspath(a.out)
    os.makedirs(os.path.join(OUT, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "references"), exist_ok=True)
    raw = parse(a.pdf)
    print(f"{len(raw)} raw entries parsed")
    approved, nonapproved = clean(raw, OUT)
    d = json.load(open(os.path.join(OUT, 'scripts', 'dictionary.json')))
    render_references(d, OUT)


if __name__ == "__main__":
    main()
