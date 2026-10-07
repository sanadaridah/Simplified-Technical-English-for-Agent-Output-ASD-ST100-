# STE — ASD-STE100 Simplified Technical English skill for AI agents

A Claude skill (also usable by other agents) that writes and reviews technical documentation in **ASD-STE100 Simplified Technical English, Issue 9 (January 2025)**: manuals, installation and operating instructions, maintenance procedures, safety warnings and cautions, datasheets, troubleshooting guides, quick-start cards.

STE is the controlled language the aerospace and defence industry uses so that a technician who reads a procedure once — possibly in a second language — does exactly what the author meant. This repository makes the whole standard available to AI agents: the 53 writing rules, the complete dictionary (876 approved words, 1,319 non-approved words with their approved alternatives), and a checker that catches what a model misses.

**Copyright note.** The dictionary and rule text are ASD's copyright, not MIT. Make sure you have authority from ASD before you use or share them; see [LICENSE](LICENSE) for what is MIT and what is not.

## What is in here

| Path | What it is |
|---|---|
| `SKILL.md` | The skill itself: workflow, modes, the core rules a writer applies to every sentence, output format. This is what the agent reads. |
| `references/writing-rules.md` | All 53 rules and 8 general recommendations, condensed, with the standard's own before/after examples. |
| `references/technical-noun-categories.md` | The 22 technical-noun and 4 technical-verb categories that decide whether a domain word (pump, breaker, firmware) is permitted. |
| `references/approved-words.md` | The 876 approved words: part of speech, approved meaning, permitted verb forms. |
| `references/non-approved-words.md` | The 1,319 non-approved words with approved alternatives and STE example sentences. |
| `references/worked-example.md` | An engineer's installation paragraph rewritten in STE, with the rule behind each change. |
| `scripts/ste_check.py` | Checker and dictionary lookup. Python 3, no dependencies. |
| `scripts/dictionary.json` | The dictionary as data, used by the checker. |
| `scripts/glossary.example.txt` | Starter glossary of technical nouns and verbs. Copy it and replace the examples with your own product and part names. |
| `tools/build_dictionary.py` | Rebuilds the dictionary and reference files from the official PDF (needed only for a new Issue of the standard). |
| `evals/` | Three test prompts and a grader, used to measure the skill against Claude without it. |
| `docs/quick-reference.md` | One-page cheat sheet for humans. |
| `dist/asd-ste100.skill` | The packaged skill for uploading to claude.ai. |

## Install

### Claude Code (CLI)

For every project on your machine:

```bash
git clone git@github.com:<org>/<repo>.git ~/.claude/skills/asd-ste100
```

For one project only, clone (or add as a submodule) into `<project>/.claude/skills/asd-ste100`. Claude Code picks the skill up on the next session; it triggers automatically when you ask for a manual, procedure, instructions, or anything STE-related, and you can force it with `/asd-ste100`.

Update with `git pull` in that folder.

### Cowork and claude.ai

Upload `dist/asd-ste100.skill` in your Claude skill settings (Settings → Capabilities → Skills, or the "Save skill" button when the file is shared in a chat). Re-upload when the repo changes; to rebuild the file after edits run the `package_skill` step from Anthropic's skill-creator or simply zip the skill folder (`SKILL.md`, `references/`, `scripts/`) with the folder name `asd-ste100`.

### Other agents (Cursor, Codex, Copilot, custom agents)

The skill is plain markdown plus a Python script. Point the agent at `SKILL.md` as a rules or context file, keep `references/` and `scripts/` beside it so the relative paths resolve, and make sure the agent can run `python3 scripts/ste_check.py`. Everything the agent needs is described inside `SKILL.md`.

## Use

Ask in ordinary words. The skill is strict by default, which is what you want for anything an installer or technician acts on:

- *"Write the installation section for the Model 3 pump from these engineering notes."*
- *"Rewrite this troubleshooting page in Simplified Technical English."*
- *"Review this warning text against STE and tell me what breaks which rule."*
- *"Draft a quick-start card for the cordless drill, STE, one page."*

Say *"relaxed"* or *"STE-style"* for explanatory prose that nobody acts on (design notes, an FAQ); the agent then keeps the sentence discipline but treats the dictionary as advisory.

Every delivery ends with a few lines of **STE compliance notes**: which product words were accepted as technical nouns, any sentence left over the limit and why, and any place the source could not be expressed in approved words without changing its meaning. Read those notes — they are where the judgement calls are.

## The checker

```bash
# check a document (auto-detects procedural vs descriptive per sentence)
python3 scripts/ste_check.py draft.md --glossary glossary.txt

# force a mode
python3 scripts/ste_check.py draft.md --mode procedural

# look up words
python3 scripts/ste_check.py --lookup check ensure "turn on" may
```

It reports non-approved words with alternatives, words it does not know (which must be technical nouns in the glossary, or replaced), sentences over 20 words (procedural) or 25 (descriptive) counted the way §8 of the standard counts, perfect tenses, passive voice, -ing verb forms, semicolons, contractions, Latin abbreviations, gendered pronouns, paragraphs over six sentences, and probable noun clusters of four or more words. It is a heuristic, not a parser: findings marked `?` need a human or the agent to decide. It produces no false findings on the standard's own example sentences.

## The glossary

STE's dictionary holds general vocabulary only. Product and part names — pump, breaker, terminal block, firmware, the text on labels — are *technical nouns* and are permitted as long as they are used consistently, kept to three words, and never used as verbs (*apply oil to the linkage*, not *oil the linkage*).

Copy `scripts/glossary.example.txt` to a shared file in your project (for example `glossary.txt`) and keep it as your organization's list. When a writer or an agent accepts a new technical noun, add it there with its category so everyone uses the same word for the same thing (Rule 1.11). Keep it honest: if the checker flags an ordinary English word, the fix is the approved alternative, not a glossary entry.

## Rebuilding for a new Issue of the standard

Request the new PDF from https://www.asd-ste100.org/STE_downloads.html, then:

```bash
pip install pdfplumber
python3 tools/build_dictionary.py ASDSTE100_ISSUE10.pdf
```

This regenerates `scripts/dictionary.json`, `references/approved-words.md`, and `references/non-approved-words.md`. The page range and column heuristics at the top of the script are tuned to the Issue 9 layout and will need checking against the new document. `references/writing-rules.md` is hand-written and must be revised by reading the new Part 1.

## How it was measured

Three prompts (rewrite a dense installation paragraph; write a quick-start guide from raw engineering notes; review a troubleshooting paragraph rule-by-rule) were run with and without the skill and graded mechanically against twelve STE checks each. With the skill: 36/36. Without: 23/36 — Claude alone put the consequence before the command in warnings, left instructions inside NOTEs, used non-approved words (*live*, *mild*, *however*), and cited rule numbers from an older Issue. Run it yourself with `evals/grade.py` after producing outputs in the layout it expects. The cost of the skill is roughly twice the tokens and time per document, because the agent reads the rules and runs the checker.

## Provenance

Built from ASD-STE100 Issue 9 (2025-01-15), obtained from ASD through the official request process. Rule numbers, limits, and examples were verified against the PDF; the dictionary was extracted programmatically and spot-checked (two layout artefacts in the PDF are corrected by hand in the build script). It differs from the public `danyuchn/asd-ste100-skill`, which deliberately omits the dictionary for licensing reasons, which leaves half the standard unenforceable.
