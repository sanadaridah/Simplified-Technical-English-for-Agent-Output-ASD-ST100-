# Worked example — an installation procedure rewritten in STE

## Source text (as a product engineer wrote it)

> Before installation, ensure that the main breaker has been switched off and verify that there is no voltage present at the terminals; failure to do so may result in serious injury or death. Remove the four stainless steel pan head machine screws that secure the front cover, then carefully lift off the cover and set it aside, taking care not to damage the gasket. The wires should be connected to the terminals by the installer according to the wiring diagram (e.g. L1 to terminal 1) and each terminal screw tightened to 2.5 Nm. If the LED doesn't illuminate, check the fuse.
>
> NOTE: Turn on the breaker only after the cover has been reinstalled.

What the checker finds: 33-word sentence, semicolon, *has been* (3.4), *been switched* and *be connected* passives (3.6), *taking* and *according* (-ing verbs, 3.5), *e.g.* (GR-6), *doesn't* (4.2), a 7-word noun cluster (2.1), and non-approved *ensure, verify, present, may, serious, secure, take care, should, according, check, reinstall, main, so*. The note contains an instruction (5.5).

## STE version

**Installation**

Glossary (technical nouns): breaker, terminal, terminal screw, front cover, gasket, wiring diagram, LED, fuse.

WARNING: BEFORE YOU DO THIS PROCEDURE, SET THE BREAKER TO OFF. MAKE SURE THAT THERE IS NO VOLTAGE AT THE TERMINALS. VOLTAGE AT THE TERMINALS CAN CAUSE INJURY OR DEATH.

1. Remove the four screws (1) that attach the front cover (2).
2. Carefully lift the front cover (2) from the unit.
3. Put the front cover (2) in a safe area.

CAUTION: DO NOT LET THE FRONT COVER TOUCH THE GASKET (3). DAMAGE TO THE GASKET CAN OCCUR.

4. Connect the wires to the terminals (4) as shown in the wiring diagram. For example, connect L1 to terminal 1.
5. Torque each terminal screw (5) to 2.5 Nm.
6. Install the front cover (2).
7. Set the breaker to ON.
8. If the LED (6) does not come on, examine the fuse (7).

## Why each change

| Source | STE | Rule |
|---|---|---|
| ensure that ... has been switched off | SET THE BREAKER TO OFF | 3.4 (no perfect tense), 3.6 (imperative, not passive), *ensure* → *make sure* / direct command, *switch off* → *set to OFF* |
| verify that there is no voltage present | MAKE SURE THAT THERE IS NO VOLTAGE | *verify* → MAKE SURE; *present* not approved (→ BE) |
| ; failure to do so may result in serious injury or death | (new sentence) VOLTAGE AT THE TERMINALS CAN CAUSE INJURY OR DEATH | 8.1 no semicolon; 7.3 consequence stated; *may* → CAN; *serious* dropped (INJURY OR DEATH is the standard's own wording) |
| four stainless steel pan head machine screws that secure | the four screws (1) that attach | 1.9 / 2.1 short technical noun, item number carries the detail; *secure* → ATTACH |
| then carefully lift off the cover and set it aside, taking care not to damage | three steps + a CAUTION | 5.2 one instruction per step; 9.3 *lift off* → *lift ... from*; 3.5 no *taking*; 5.5 a damage risk is a CAUTION, not a clause |
| The wires should be connected ... by the installer according to | Connect the wires ... as shown in | 5.3 imperative; 3.6 active; *should* dropped in a command; *according to* → *as shown in* |
| (e.g. L1 to terminal 1) | For example, connect L1 to terminal 1. | GR-6; 4.2 full sentence, no omitted verb |
| each terminal screw tightened to 2.5 Nm | Torque each terminal screw (5) to 2.5 Nm. | 5.2 own step; 4.2 no omitted verb; *torque* is an approved verb |
| NOTE: Turn on the breaker only after the cover has been reinstalled. | steps 6 and 7 | 5.5 a note may not instruct; 3.4; *reinstall* → INSTALL; *turn on* → SET TO ON |
| If the LED doesn't illuminate, check the fuse. | If the LED (6) does not come on, examine the fuse (7). | 4.2 no contraction; *illuminate* → COME ON (approved phrasal verb); *check* (v) → EXAMINE |

## STE compliance notes (what you append to a delivery)

Mode: strict. Technical nouns accepted: breaker, terminal, terminal screw, front cover, gasket, wiring diagram (categories 1 and 6), LED, fuse (category 1). *Torque* used as an approved verb. The source did not state a torque tolerance; none added. The word "serious" from the source is not approved and was dropped because "injury or death" already states the highest level of risk. Item numbers (1)–(7) assume an illustration; remove them if there is none.
