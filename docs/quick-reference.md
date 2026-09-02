# STE in one page — for humans

Rule numbers are from ASD-STE100 Issue 9. The full text with examples is in `references/writing-rules.md`.

**Two kinds of text, two limits.** A *procedure* tells the reader to do something: imperative verb, numbered steps, one action per step, **20 words** per sentence (5.1–5.3). A *description* tells the reader how something is: no imperative, **25 words** per sentence, one topic per paragraph, **6 sentences** per paragraph (6.1–6.6). A *note* is a description inside a procedure and may never contain an instruction, a limit, or a safety point (5.5).

**Words.** Use only approved dictionary words, technical nouns (our part and product names), and technical verbs (1.1). Every approved word has one part of speech and one meaning (1.2, 1.3): *test* and *check* are nouns (*do a test*, *do a check*); *follow* means "come after" (so *obey the instructions*); *see* is with the eyes; *turn* is rotate. Look up before you guess: `python3 scripts/ste_check.py --lookup <word>`.

**The ones everybody gets wrong.** check → *make sure that* / *examine* / *measure*. ensure, verify, confirm → *make sure that*. perform → *do*. press → *push*. turn on / switch on → *set to ON*, *start*, *energize*. turn off → *set to OFF*, *stop*, *de-energize*. plug in → *connect*. mount, fasten, secure → *install*, *attach*. allow, permit, enable → *let*. provide → *give*, *supply*. display, indicate → *show*. happen → *occur*. inspect → *examine*. should → *must*. may, could, would → *can*. need, require → *is necessary*. avoid → *prevent*. normal → *usual*. proper, appropriate, suitable → *correct*, *applicable*. several → *some*. additional → *more*. however → *but*. therefore → *thus*. whether → *if*. within → *in*. e.g. → *for example*. etc. → list the items or drop it.

**Verbs.** Simple present, simple past, simple future, imperative, infinitive, past participle as an adjective — nothing else (3.2). No *has/have been*, no *is being*, no *been* at all (3.4). No *-ing* verbs: *when you do*, not *when doing*; *-ing* survives only inside a technical noun or heading (*wiring diagram*, *Troubleshooting*) (3.5). Active voice; in a procedure that means the imperative (3.6). Passive only in descriptions when nobody knows the agent.

**Sentences.** One instruction per sentence unless two actions are simultaneous (5.2). Condition first, comma, then the command: *When the light comes on, set the switch to NORMAL* (5.4). No semicolons (8.1). No contractions, no dropped articles, subjects, or verbs (4.2, 4.5). Noun strings of three words maximum — break them with *of*, *for*, *that*, or hyphenate the unit that belongs together (2.1, 2.2). Three or more items or steps go in a vertical list with a colon lead-in (4.3). Repeat the noun instead of an ambiguous *it* or *this* (GR-3, GR-4). Keep *that* after *make sure* (GR-1). No *he/she* (GR-7).

**Counting words.** A number with its unit, an abbreviation, an identifier (36L7), a hyphenated word, a quoted label, a document title, a proper noun, and anything in parentheses each count as **one** word (8.4–8.7). Step numbers are not counted. A list lead-in ending in a colon is one sentence; each item is another.

**Safety instructions.** `WARNING:` = injury or death. `CAUTION:` = damage. Both → WARNING (7.1). Start with the command or the condition, then say what happens if the reader does not obey (7.2, 7.3):

> WARNING: BEFORE YOU OPEN THE COVER, SET THE UPSTREAM BREAKER TO OFF. THE TERMINALS CAN CAUSE ELECTRIC SHOCK, INJURY, OR DEATH.

**Never change the content.** Keep every limit, tolerance, quantity, and condition. Keep the author's certainty (*may* → *can*, not a bare assertion). Keep quoted label and screen text exactly as printed. Do not add steps or causes the source did not give — flag the gap instead.

**Before you hand it over.** `python3 scripts/ste_check.py draft.md --glossary glossary/voltsafe-glossary.txt`, fix what it finds, then add the compliance notes: mode, technical nouns accepted, anything left over the limit and why.
