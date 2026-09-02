# Changelog

## 1.0.0 — 2026-09-02

- First release. Built from ASD-STE100 Issue 9 (2025-01-15).
- Dictionary: 876 approved and 1,319 non-approved entries extracted from Part 2 (official counts 875 / 1,274; the small surplus is entries the standard lists twice under different parts of speech).
- Rules: all 53 rules and 8 general recommendations condensed in `references/writing-rules.md` with the standard's examples.
- Checker: `scripts/ste_check.py` (word approval, word count per §8, tenses, passive, -ing forms, semicolons, contractions, Latin abbreviations, gendered pronouns, paragraph length, noun clusters) with `--lookup` and `--glossary`.
- Evals: three prompts (rewrite, write from notes, review). With skill 36/36 mechanical checks, without 23/36.
