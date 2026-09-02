---
name: asd-ste100
description: "Write or rewrite technical documentation in ASD-STE100 Simplified Technical English (Issue 9, 2025) — product manuals, installation and operating instructions, maintenance procedures, safety warnings and cautions, datasheets, spec sheets, work instructions, troubleshooting guides, quick-start guides, and any technical writeup for installers, technicians, electricians, or non-native English readers. Use this skill whenever the user asks for a manual, instruction guide, procedure, technical description, safety text, or 'technical writeup', or mentions STE, Simplified Technical English, controlled language, or plain-language technical writing — even if they do not name the standard. Bundles the full Issue 9 dictionary (876 approved words, 1,319 non-approved words with alternatives), the 53 writing rules, and a checker script. Not for marketing copy, blog posts, or conversational text."
metadata:
  version: "1.0.0"
  source: "ASD-STE100 Issue 9 (2025-01-15), extracted for VoltSafe internal use"
---

# ASD-STE100 Simplified Technical English — Issue 9

STE is the controlled language the aerospace and defence industry uses so that a technician who reads a procedure once, possibly in a second language, does exactly what the author meant. It works by removing choice: one approved word per idea, one part of speech per word, one instruction per sentence, one topic per paragraph, active voice, simple tenses, hard word limits. This skill applies the real standard — the rules and the dictionary from Issue 9 — to your technical documents. The dictionary was extracted from a copy of the standard that VoltSafe obtained from ASD for internal use. It is for VoltSafe staff and their AI agents only; do not redistribute the reference files or the dictionary outside the company.

## Modes

**Strict (default).** Procedures, installation and operating instructions, maintenance steps, safety instructions, product descriptions, datasheet text, troubleshooting tables, any document a technician or installer acts on. Every rule applies, including the dictionary. This is the mode for "write me a manual", "installation guide", "instructions", "technical writeup", "procedure".

**Relaxed.** Use only when the user says "relaxed", "STE-style", or "loosely", or when the text is explanatory prose whose reader is not acting on it (an internal design note, an engineering rationale, an FAQ). Apply all structural rules (sentence and paragraph limits, active voice, simple tenses, one instruction per sentence, no semicolons, articles present, condition first, no -ing verbs) and treat the dictionary as advisory: prefer approved words, allow an unapproved word when the approved alternative reads unnaturally, and do not report dictionary hits.

State the mode in one line at the top of your compliance notes. Never ask which mode to use for a manual or procedure — strict is the answer.

## Workflow

1. **Classify each block of text before you write it.** STE has different limits for the two kinds of writing, so decide for every heading which one you are in.
   - *Procedural*: tells the reader to do something. Imperative verbs, numbered steps, max **20 words** per sentence, one instruction per sentence.
   - *Descriptive*: tells the reader how something is or works. No imperative, max **25 words** per sentence, max **6 sentences** per paragraph, one topic per paragraph.
   - *Safety instruction* (WARNING = injury or death, CAUTION = damage): a procedural sentence that starts with a command or condition, followed by the consequence. 20-word limit applies.
   - *Note*: descriptive text inside a procedure, information only, never an instruction or a limit.

2. **Build the glossary of technical nouns and verbs first.** The dictionary holds general vocabulary; the product's own words (pedestal, breaker, terminal block, firmware, RS-485, the names on labels and screens) are *technical nouns* under Rule 1.5 or *technical verbs* under Rule 1.12. Before writing, list them, in the exact form the company or the parts list uses, no more than three words each, one name per item (Rules 1.8–1.11). If the source material names the same thing two ways, pick one and use it everywhere. Write this list to a glossary file (one term per line) so the checker accepts them. Start from `glossary/voltsafe-glossary.txt` in this repository when it exists next to the skill — it holds the company's agreed technical nouns and verbs; add new terms there rather than in a throwaway file so the next writer gets them too. Read `references/technical-noun-categories.md` if you are unsure whether a word qualifies; every accepted term should fit a named category. A technical noun is never used as a verb (*apply grease*, not *grease the bolt*).

3. **Write the document following the core rules below.** Draft in STE from the start rather than writing normally and converting; the sentence shape is different (condition first, then command; one action; the noun repeated instead of a pronoun). When a word you reach for is not approved, look it up before guessing: `python3 scripts/ste_check.py --lookup <word>` prints the approved meaning, the alternatives, and the standard's own before/after examples. Many alternatives require a different sentence construction, not a word swap (Rule 9.1) — the examples show how.

4. **Run the checker on the finished text.** `python3 scripts/ste_check.py draft.md --glossary glossary.txt` (add `--mode procedural` or `--mode descriptive` if the auto-detection picks the wrong limit for a block). It reports non-approved words with their alternatives, words it does not know, sentences over the limit (counted by the standard's own word-count rules), perfect tenses, passives, -ing verbs, semicolons, contractions, Latin abbreviations, gendered pronouns, paragraphs over six sentences, and probable noun clusters of four or more words. Fix everything in the first two groups and every hard finding. Findings marked `?` (a participle that may be an adjective, an -ing word that may be a technical noun) need your judgement. Words the checker does not know are either technical nouns you forgot to put in the glossary or words that need replacing; decide for each. Run it again until the only remaining items are ones you can justify.

5. **Deliver the document, then a short "STE compliance notes" section** at the end (or in your reply, if the document must stay clean): the mode; the technical nouns and verbs you accepted, with their category; any sentence you left over the limit and why (usually an official name or quoted label that would not divide); anything from the source you could not express in approved words without changing the meaning, and what you did instead. Keep this to a few lines. Do not pad the document itself with commentary.

## Core rules — the ones that shape every sentence

Full text with the standard's examples: `references/writing-rules.md`. Read it the first time you use this skill in a session and whenever a finding cites a rule you do not remember.

**Words (§1, §9)**
- Use only dictionary-approved words, technical nouns, and technical verbs (1.1). Look up, do not assume; common technical-writing verbs that are *not* approved: check → *make sure that* / *examine* / *measure* / *do a check of*; ensure, verify, confirm → *make sure that*; perform → *do*; press → *push*; switch on / turn on → *set the switch to ON*, *start*, *energize*; turn off → *set to OFF*, *stop*, *de-energize*; plug in → *connect*; mount, fasten, secure → *install*, *attach*; locate, position, place → *put*, *find*; allow, permit, enable → *let*; provide → *give*, *supply*; obtain → *get*; display, indicate → *show*; happen → *occur*; inspect → *examine*; observe → *monitor*; begin, initiate → *start*; finish, terminate → *stop*, *complete*; proceed → *continue*; run (a program) → *operate*; note (v) → *record*; should → *must*; may, could, would → *can*; need, require → *is necessary*; avoid → *prevent*; normal → *usual*; abnormal → *unusual*; proper, appropriate, suitable → *correct*, *applicable*; adequate → *sufficient*; complete (adj) → *full*; several → *some*; various → *different*; additional, extra → *more*; every → *each*, *all*; however → *but*; therefore → *thus*; whether → *if*; within → *in*; over/under (limits) → *more than* / *less than*; e.g. → *for example*; etc. → drop it or list the items.
- One part of speech per word (1.2): *test*, *check*, *damage*, *work* are nouns only (*do a test*, *do a check*, *cause damage*, *do work*); *help* is a verb only (*with the aid of*); *oil*, *grease*, *wire*, *clamp* are technical nouns only (*apply oil*, *attach with wire*, *put clamps on*).
- One meaning per word (1.3, 9.2): *follow* = come after (obey instructions, follow the lights); *see* = with the eyes; *turn* = rotate; *wear* = abrade (put on clothing); *above/below* = positions, not limits; *about* = concerning (approximately 2 liters, around the shaft).
- No phrasal verbs (9.3): *put out* → *extinguish*, *give off* → *release*, *take off* → *remove*, *set up* → *install* / *prepare*, *carry out* → *do*, *find out* → *find*, *fill in* → *complete*, *pick up* → *lift*, *shut down* → *stop* / *set to OFF*.
- The approved verb over a noun phrase (3.7): *shows 450 ohms*, not *gives an indication of*; *before you remove the unit*, not *before the removal of the unit*.
- American spelling (1.14); keep quoted screen text and label text exactly as printed.

**Verbs (§3)**
- Only: infinitive, imperative, simple present, simple past, simple future, past participle as an adjective (3.2). No *has/have/had + participle*, no *is/was + -ing*, no *been*, no *being* (3.4). *The operator has adjusted* → *adjusted*. *When you are doing* → *when you do*.
- -ing only inside a technical noun or heading (3.5): *wiring diagram*, *Troubleshooting*; never *before installing*, *taking care*, *according to* (→ *as given in*, *as specified in*).
- Active voice (3.6). *The cover is removed by the installer* → *The installer removes the cover*; in a procedure, *Remove the cover*. Passive only in descriptive text when nobody knows the agent (*the data was corrupted*). *Can be adjusted* → *You can adjust*. Past participles after *is* are fine when they describe a state (*the unit is installed*, *the surface is clean*) — that is an adjective, not passive.

**Sentences (§2, §4, §5, §6, §8)**
- 20 words procedural, 25 descriptive, counted STE-style: a number with its unit, an abbreviation, an identifier, a hyphenated word, a quoted label, a document title, a proper noun, and anything in parentheses each count as one word (8.4–8.7). Step numbers are not counted. A list lead-in ending in a colon is one sentence; each list item is another.
- One instruction per sentence (5.2), unless two actions are simultaneous (*hold the panel and install the fastener*) or a limit follows its measurement (*Measure the leakage. The leakage must not be more than 0.5 cc/minute.*).
- Imperative in procedures (5.3): *Continue the test*, not *the test can be continued*. Do not write *you must* before an imperative except in safety text.
- Condition first, then a comma, then the command (5.4): *When the light comes on, set the switch to NORMAL.* Never *Set the switch ... when ...*.
- No semicolons anywhere (8.1). No contractions, no dropped subjects, verbs, or articles (4.2): *If installed, remove the shims* → *If shims are installed, remove them*; *Rotary switch to INPUT* → *Set the rotary switch to INPUT*.
- Articles before nouns (4.5): *Turn the shaft assembly*, but none before a noun with an identifier (*Tag circuit breaker 36L7*) or in general statements (*Solvents can cause damage to paint*).
- Multi-word nouns of three words maximum (2.1): break longer ones with *of*, *on*, *for*, *that* — *Remove the bolts that attach the transmission housing to the engine* — or hyphenate the unit that belongs together (2.2). Official names longer than three words: write in full once, then use the short form or abbreviation you declared.
- Vertical lists for three or more items or steps (4.3): lead-in with a colon, one item per line, article on each item, period only on full sentences and on the last item, no nesting, DO NOT repeated on each safety item.
- Descriptive paragraphs: topic sentence first, one topic, six sentences maximum, information added one fact per sentence, key words repeated rather than varied (6.1–6.6).
- Notes give information only, never an instruction, limit, or safety point (5.5); a note that would prevent injury or damage becomes a WARNING or CAUTION, a note with an instruction becomes a step.

**Safety instructions (§7)**
`WARNING:` for injury or death, `CAUTION:` for damage (both → WARNING). Shape: command or condition first, then the reason. *WARNING: BEFORE YOU OPEN THE COVER, SET THE BREAKER TO OFF. THE TERMINALS CAN CAUSE INJURY OR DEATH FROM ELECTRIC SHOCK.* Abstract statements (*extreme cleanliness is imperative*) are not safety instructions.

**Reference and clarity (GR-1 to GR-8)**
Keep *that* after *make sure*, *show*, *recommend*. Repeat the noun instead of a pronoun that could point at two things (*the pins can become damaged*, not *they*). Make *this* point at one thing. Watch *with* (having / together with / by means of) and restructure when it is ambiguous. No *he/she*; use *you*, *the operator*, *personnel*. No Latin abbreviations. Prefer *the instructions of the manufacturer* to a possessive when in doubt.

## Preserve the meaning

STE changes the form of the text, never its content. When you rewrite:
- Keep every condition, limit, tolerance, quantity, and exception. If STE would force you to drop one to make the word count, split the sentence instead.
- Keep the author's certainty. *May* becomes *can* (possibility) or *possibly*, not a bare assertion; *should* becomes *must* only when the source means an obligation — if it means a recommendation, write *We recommend that you ...* or *It is recommended that you ...*. Say in the compliance notes when you had to choose.
- Do not add steps, causes, or explanations the source does not give. Rule 7.3 asks for the consequence in a safety instruction; if the source does not state it and you cannot be sure of it, write the command and flag the missing consequence rather than inventing one.
- Do not alter quoted text: screen messages, label text, part names from drawings, legal wording. They count as one word and stay as printed, even if non-STE.
- Numbers and units stay exactly as given. Do not round, convert, or "simplify" a specification.

## Output shape for common requests

*Installation or operating manual*: title; a short descriptive overview (what the product is, what the document covers); safety instructions that apply to the whole document; a numbered procedure per task with a heading in the -ing noun form the standard permits (*Installation*, *Cleaning*, *Troubleshooting*); notes only where information helps; a troubleshooting table (symptom, possible cause, action — the action column in the imperative). Use the user's requested file format; STE rules apply to the words, not the layout.

*Rewrite of an existing text*: return the rewritten text in the same structure, then the compliance notes. When the user asks to see what changed, add a three-column table: Original / STE / Rule.

*Review of a text against STE*: run the checker, then read the text yourself for the rules no script can check (one topic per sentence, condition first, notes that hide instructions, approved meaning of each word, ambiguous *with*/*this*/pronouns). Report by rule number, most serious first (dictionary and safety-instruction problems, then sentence structure, then style), with the corrected sentence for each.

## Files

- `references/writing-rules.md` — all 53 rules and 8 recommendations, condensed, with the standard's own examples. Read on first use.
- `references/technical-noun-categories.md` — the 22 technical-noun and 4 technical-verb categories with examples; read when deciding whether a domain word is permitted.
- `references/worked-example.md` — an engineer's installation paragraph rewritten in STE, with the rule behind each change and a sample of the compliance notes.
- `references/approved-words.md` — the 876 approved words with part of speech, meaning, and verb forms. Grep it; do not read it whole.
- `references/non-approved-words.md` — 1,319 non-approved words with alternatives and STE examples. Grep it; do not read it whole.
- `scripts/ste_check.py` — checker and dictionary lookup (`--lookup word`, `FILE --glossary terms.txt [--mode ...] [--json]`). Python 3, no dependencies. `scripts/dictionary.json` is its data.
