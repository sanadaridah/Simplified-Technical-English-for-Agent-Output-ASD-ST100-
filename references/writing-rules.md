# ASD-STE100 Issue 9 — The writing rules (Part 1), condensed

Source: ASD-STE100 Simplified Technical English, Issue 9, 2025-01-15, Part 1. 53 rules in 9 sections plus 8 general recommendations (GR). Rule text is quoted as written in the standard; explanations and examples are condensed. Examples marked "STE:" are compliant, "Non-STE:" are not.

Contents: §1 Words · §2 Multi-word nouns · §3 Verbs · §4 Sentences · §5 Procedural writing · §6 Descriptive writing · §7 Safety instructions · §8 Punctuation and word count · §9 Writing practices · General recommendations

---

## Section 1 — Words

**Rule 1.1** Use words that are: approved in the dictionary, technical nouns, or technical verbs.
The dictionary (Part 2; `references/approved-words.md`) holds the general vocabulary. Everything else must qualify as a technical noun (Rule 1.5) or technical verb (Rule 1.12). Example: "use" is an approved verb, "engine" is a technical noun, "ream" is a technical verb.

**Rule 1.2** Use approved words from the dictionary only as the specified part of speech.
"Test" is an approved noun, not a verb. Non-STE: *Test the system for leaks.* STE: *Do the leak test of the system.* "Dim" is an adjective only: STE: *Set the lights to the dim position.* When the approved alternative has a different part of speech, restructure the sentence: Non-STE: *Make sure that the valve is operable.* STE: *Make sure that the valve can operate.*

**Rule 1.3** Use approved words only with their approved meanings.
"Follow" means only "come after". STE: *Do the procedures that follow.* Non-STE: *Follow the safety instructions.* STE: *Obey the safety instructions.* Many approved words carry a restricted meaning; the dictionary entry says "for other meanings use ...".

**Rule 1.4** Use only the approved forms of verbs and adjectives.
The dictionary lists each verb's forms (REMOVE, REMOVES, REMOVED, REMOVED = infinitive/imperative, simple present, simple past, past participle-as-adjective). Adjectives list comparatives (SLOW: SLOWER, SLOWEST); others take "more/most".

**Rule 1.5** You can use words that you can include in a technical noun category.
A technical noun is a noun term for a specified concept in a subject field. Not in the dictionary because there are too many; take them from the company glossary or parts information. The 22 categories are in `technical-noun-categories.md` (parts; vehicles; tools; materials; facilities; systems; math/science/engineering; navigation; numbers and units; quoted text; roles and organizations; body parts; personal effects; medical; documents; environmental conditions; colors; damage terms; computing/ICT; civil and military operations; law; life forms).

**Rule 1.6** Use a word that is not approved in the dictionary, only when it is a technical noun or part of a technical noun.
"Base" is not approved (use "bottom") but *The base of the triangle is 5 cm* is fine (math TN). "Backup" is not approved (use emergency/auxiliary) but *Do the backup of the computer* is fine (ICT TN). "Main" is not approved (use "primary") but *Retract the main landing gear* keeps the official TN.

**Rule 1.7** Do not use words that are technical nouns as verbs.
Non-STE: *Oil the steel surfaces.* STE: *Apply oil to the steel surfaces.* Non-STE: *If you think it will snow ...* STE: *If you think that snow will fall ...* (A word can be both a TN and a TV if it fits both category lists: "drill" the tool / "drill a hole".)

**Rule 1.8** Use technical nouns that are approved in your company, industry, or subject field.
If the company or industry has an official name for the item, use it (*touchscreen*, *home button*).

**Rule 1.9** When you must select a technical noun, use one which is short and easy to understand.
Not more than three words. Non-STE: *Remove the four stainless steel pan head machine screws (10) that attach the metallic machined flange (15) ...* STE: *Remove the four screws (10) that attach the flange (15) to the cover (20).* — item numbers and the illustration carry the detail.

**Rule 1.10** Do not use regional, slang, or jargon words as technical nouns.
*choker* → *cable*; *do not brick the router* → *do not set the router to OFF*; *remove your gear* → *remove your tools and equipment*.

**Rule 1.11** Do not use different technical nouns for the same item.
If it is "actuator" in step 1, it is "actuator" in every step, never "servo control unit" or "control unit".

**Rule 1.12** You can use verbs that you can include in a technical verb category.
Four categories: manufacturing processes (drill, weld, anneal, polish, cast); computer processes (click, enter, type, save, scroll, install, reboot, download); subject-field instructions (engineering, medical, military, navigation, automotive, energy: compensate for, sterilize, arm, land, brake, pump); law and regulations (comply with, notify, waive). Use an approved dictionary verb whenever one gives the instruction accurately: Non-STE: *If you detect broken wires, repair them.* STE: *If you find broken wires, repair them.* But *The security scanner detects metal objects* is correct (technical verb in context). Do not turn a TN into a TV: *Clamp the cable* → *Put clamps on the cable*; *Grease the fasteners* → *Apply grease to the fasteners*; *Wire the cable to the structure* → *Attach the cable to the structure with wire*. A word that is not approved can still be a TV in its field: *Enter your password* (ICT) but not *Do not enter the engine test area* (→ *go into*).

**Rule 1.13** Do not use technical verbs as nouns.
Non-STE: *Give the hole 0.20-inch ream.* STE: *Ream the hole to a 0.20-inch dimension.* The past participle may serve as an adjective: *the reamed hole*.

**Rule 1.14** Use American English spelling unless other official directives tell you differently.
*fiber* not *fibre*, *color* not *colour*. Keep quoted text (screen text, labels) as it is.

## Section 2 — Multi-word nouns

**Rule 2.1** Write multi-word nouns of no more than three words.
A long noun string hides how the words relate ("runway light connection resistance calibration": what relates "runway" to "calibration"?). Break it with prepositions and verbs:
- Non-STE: *Runway light connection resistance calibration.* STE: *Calibration of the resistance of the runway light connection.*
- Non-STE: *Install the forward turbine overheat thermocouple terminal tags.* STE: *Install the terminal tags on the forward overheat thermocouple of the turbine.*
- Non-STE: *Remove the engine transmission housing attachment bolts.* STE: *Remove the bolts that attach the transmission housing to the engine.*

**Rule 2.2** When a technical noun has more than three words, write it in full. Then, you can use one of these methods to make the technical noun clear: give a shorter form of the technical noun; use hyphens (-) between words that you use as one unit.
Method 1: write the official long name once, explain it, then use a short form or the official abbreviation: *engage the ramp service door safety connector pin (... referred to in this procedure as the "safety connector pin")*. Do not abbreviate names of three words or fewer (*the DA (8)* → *the diaphragm assembly (8)*), and do not fill procedures with abbreviations. Method 2: hyphenate the words that act as one unit: *cutoff-switch power connection* (3 words), *main-gear-door retraction-winch handle* (3 words). Never hyphenate everything into one blob, and never remove hyphens that are part of an official name (*inward-outward valve*).

## Section 3 — Verbs

**Rule 3.1** Use only the verb forms that are given in the dictionary.

**Rule 3.2** Use only these verb forms and tenses of verbs: the infinitive form; the imperative form (command form); the simple present tense; the simple past tense; the simple future tense; the past participle form (as an adjective).
Not permitted: present perfect (*have/has adjusted*), past perfect (*had adjusted*), progressive (*is/was adjusting*), and every other complex construction.

**Rule 3.3** Use the past participle form as an adjective.
It shows a condition, not an action, and is not the passive voice: *Examine all parts of the disassembled unit.* / *When the unit is fully disassembled, clean all the parts.* Use it before a noun, or after "be", "become", "stay". Some adjectives that look like participles are approved on their own (*permitted*, *damaged*).

**Rule 3.4** Do not use auxiliary verbs to make complex verb constructions.
Non-STE: *The operator has adjusted the linkage.* STE: *The operator adjusted the linkage.* Auxiliary + participle also produces passive constructions to avoid:
- *The seat is to be installed before you install the cushion* → *Before you install the cushion, install the seat.*
- *The volume control can be adjusted* → *You can adjust the volume control.*
- *The temperature must be adjusted* → *Adjust the temperature.*
- *The sleeve will be adjusted by the robot* → *The robot will adjust the sleeve.*
Note that BE has only the forms be, is, are, was, were: "been" and "being" are not approved.

**Rule 3.5** Use the "-ing" form of a verb only as a technical noun or as a modifier in a technical noun.
"-ing" words can be verb, adjective, noun, or the start of a long dependent clause, so they cause ambiguity. Non-STE: *When you are doing this procedure, obey all the safety precautions.* STE: *When you do this procedure, obey all the safety precautions.* Permitted: headings and technical nouns (*Cleaning*, *Troubleshooting*, *air-conditioning system*, *grinding wheel*, *welding torch*). The only approved dictionary words with -ing: nouns *lighting, opening, routing, servicing*; adjectives *mating, missing, remaining*; pronoun *something*; preposition *during*.

**Rule 3.6** Use the active voice. In descriptive writing, you can use the passive voice only when the agent is unknown.
Test for passive: can you ask "by whom or by what?" Four ways to make a sentence active:
1. Put the agent first: *The circuits are connected by a switching relay* → *A switching relay connects the circuits.*
2. Turn an infinitive into the main verb: *These values are used by the computer to calculate the energy consumption* → *The computer calculates the energy consumption from these values.*
3. In procedures, use the imperative: *The test can be continued by the operator* → *Continue the test.*
4. Supply "you" (the reader) or "we" (the company) as the subject: *On the ground, the valve can be opened with the override handle* → *On the ground, you can open the valve with the override handle.* *Additives are not used in this type of fuel* → *We do not use additives in this type of fuel* or *This type of fuel does not contain additives.*
Passive is acceptable only when the agent truly is unknown: *During transmission, the data was corrupted.* (Do not invent a wrong agent: *Transmission corrupted the data* is technically false.)

**Rule 3.7** Use an approved verb to describe an action, not a noun or other parts of speech.
*The ohmmeter gives an indication of 450 ohms* → *The ohmmeter shows 450 ohms.* *Before the removal of the unit, ...* → *Before you remove the unit, ...* But when the action word is not an approved verb, go the other way: Non-STE: *Check the laptop battery.* STE: *Do a check of the laptop battery.* ("check" is approved only as a noun.)

## Section 4 — Sentences

**Rule 4.1** Write short and clear sentences.
In procedures, give instructions directly to the reader in the imperative, one step per sentence, with numbered steps. In descriptions, one topic per sentence, no imperative. Be concrete: *No leaks are permitted* → *Make sure that there are no leaks.* *Different temperatures will change the cure time* → *When the temperature increases, the cure time will decrease* (better still: *The cure time is 2 hours at a temperature of 20 °C.*)

**Rule 4.2** Do not omit words or use contractions to make your sentences shorter.
- No missing noun: *Can be a maximum of five inches long* → *Cracks can have a maximum length of five inches.*
- No missing verb: *Rotary switch to INPUT* → *Set the rotary switch to INPUT.*
- No missing subject: *If installed, remove the shims* → *If shims are installed, remove them.*
- No missing article: *Remove the bolt and stop* (ambiguous) → *Remove the bolt and the stop.*
- No contractions: *don't* → *do not*.

**Rule 4.3** Use a vertical list for complex texts.
Put a colon at the end of the lead-in, mark each item (dash, bullet, letter, number), start each item with an uppercase letter, use an article before the subject noun of each item, end an item with a period only if it is a full sentence, never end an item with a comma or semicolon, end the last item with a period. Each item must connect grammatically to the lead-in. Do not mix procedural and descriptive items in one list. Do not nest lists; fold sub-items into parentheses. In safety text, repeat DO NOT on each item:
*CAUTION: WHEN YOU GET ACCESS TO THE REAR FUSELAGE THROUGH THE ACCESS PANEL: – DO NOT PUT YOUR FEET ON THE APU LINE. – DO NOT USE THE APU LINE AS A HANDLE.*
Example: *If the Ram Air Turbine (RAT) is retracted: (a) Remove the tag. (b) Open the isolating valves. (c) Slowly and fully extend the RAT and make sure that it does not touch other parts. (d) Close the isolating valves. (e) Tag the isolating valves with "DO NOT OPERATE." (f) Release the DOWN pressure.*

**Rule 4.4** Use connecting words and connecting phrases to connect sentences that contain related topics.
Approved connectors include *and, but, then, thus* and phrases *as a result, at the same time*. They may open a sentence: *The localizer course aligns with the centerline of the runway. And the glideslope path is at a constant angle to the threshold of the runway.* *Tag the disassembled parts. This method will help you during the subsequent procedures.*

**Rule 4.5** When applicable, use an article (the, a, an) or a demonstrative adjective (this, these) before a noun or a multi-word noun.
*Turn shaft assembly* → *Turn the shaft assembly.* *Data module tells you how to operate unit* → *This data module tells you how to operate the unit.* No article for general statements (*Solvents can cause damage to paint*) or abstract qualities (*This software increases performance*). In a series, an article before only the first noun applies an adjective to all items: *Install the new O-rings (15), spacers (14), nut (13), and safety pin (12)* (all new) versus *Install the new O-rings (15), the spacers (14), ...* (only the O-rings are new). No article before a noun followed by an identifier: *Tag circuit breaker 36L7.*

## Section 5 — Procedural writing

**Rule 5.1** Write short sentences. Use a maximum of 20 words in each sentence.
Applies to warnings and cautions too. Word count follows Section 8. Non-STE (25 words): *Put preservation oil into the unit through the vent hole until the oil level is approximately 6 mm (0.24 inches) below the surface of the flange cover.* STE: *Put preservation oil into the unit through the vent hole. Continue until the oil level is approximately 6 mm (0.24 in) below the surface of the flange cover.* Notes are descriptive text: 25 words.

**Rule 5.2** Write only one instruction in each sentence unless two or more actions occur at the same time.
Non-STE: *Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch.* STE: *A. Set the TEST switch to the middle position. B. Release the SHORT-CIRCUIT TEST switch.* Simultaneous actions may share a sentence: *Hold the panel in its open position and install the fastener.* *Remove and discard the seal.* A work step may hold two sentences when a result follows immediately: *Measure the leakage from the outlet port. The leakage must not be more than 0.5 cc/minute.*

**Rule 5.3** Write instructions in the imperative (command) form.
*The test can be continued* → *Continue the test.* Other forms leave the reader unsure whether the step is required, already done, or someone else's job. Do not put "must" before an imperative except in safety instructions or for an important condition: *Before you remove the clamp, you must disconnect the hose* → *Before you remove the clamp, disconnect the hose.*

**Rule 5.4** When there is a condition that the reader must know about first, start the instruction with a descriptive statement. Then, divide that descriptive statement from the command with a comma.
*Set the switch to NORMAL when the light comes on* → *When the light comes on, set the switch to NORMAL.* *Apply the primer when the surface is dry* → *When the surface is dry, apply the primer.* Comma placement changes meaning: *If the CSD does not operate correctly, disconnect it* ≠ *If the CSD does not operate, correctly disconnect it.*

**Rule 5.5** Write notes only to give information, not instructions.
A note is descriptive (25 words per sentence, no imperative): *NOTE: The gyroscope will become stable after approximately 15 seconds.* A note that contains an instruction must become a work step; one that prevents injury or damage must become a WARNING or CAUTION; a limit or tolerance goes directly after its work step, not in a note. Test: read the procedure without its notes — the reader must still be able to do it.

## Section 6 — Descriptive writing

Descriptive writing gives information, not instructions: no imperative. It covers descriptions of items and systems, general information (reports, brochures, papers), and notes in procedures.

**Rule 6.1** Give information gradually.
One subject per sentence, added in order. Non-STE crams the Instrument Landing System into four dense sentences; STE opens *The Instrument Landing System (the system) on the aircraft shows data that helps the pilot during the approach to the runway.* then adds one fact per sentence.

**Rule 6.2** Use key words and key phrases to give your text a logical structure.
Repeat the same key words (system, pilot, runway, localizer course) from sentence to sentence so each sentence visibly builds on the last. Do not vary terminology for style.

**Rule 6.3** Write short sentences. Use a maximum of 25 words in each sentence.
Non-STE (31 words): *A smartphone is a cellular telephone that has an integrated computer and many other functions, such as an operating system, internet browsing as well as the ability to run software applications.* STE: *A smartphone is a cellular telephone that has an integrated computer and many other functions. It includes an operating system and an internet browser, and it can also operate software applications.*

**Rule 6.4** Use paragraphs to show related information.
Each paragraph starts with a topic sentence; the rest explain it.

**Rule 6.5** Make sure that each paragraph has only one topic.
The topic sentences alone should form a good outline of the text.

**Rule 6.6** Make sure that no paragraph has more than six sentences.
Divide longer paragraphs.

## Section 7 — Safety instructions

A **warning** = risk of injury or death. A **caution** = risk of damage to objects. If both, use a warning. Other industries may use danger/attention/notice or symbols; the three rules still apply. Safety instructions obey the 20-word limit.

**Rule 7.1** Use an applicable word (for example, "warning" or "caution") to identify the level of risk.
Non-STE: *CAUTION: EXTREME CLEANLINESS OF OXYGEN TUBES IS IMPERATIVE.* STE: *WARNING: MAKE SURE THAT THE OXYGEN TUBES ARE FULLY CLEAN. OXYGEN AND GREASE MAKE AN EXPLOSIVE MIXTURE. AN EXPLOSION CAN CAUSE INJURY OR DEATH.*

**Rule 7.2** Start a safety instruction with a clear and accurate command or condition.
*WARNING: DO NOT SWALLOW THE SOLVENT. ...* *CAUTION: WHEN YOU ASSEMBLE THE UNIT, DO NOT LET THE PARTS FALL. ...*

**Rule 7.3** Give an explanation to show the risk or possible result.
*... SOLVENTS ARE POISONOUS AND CAN CAUSE INJURY OR DEATH.* *... IF THEY FALL, PERMANENT DAMAGE TO THE PARTS CAN OCCUR.*
Pattern: [WARNING|CAUTION]: [command or condition + command]. [what happens if you do not obey].

## Section 8 — Punctuation and word count

STE gives no general punctuation rules (use Chicago, Gregg, GPO, Swan). Specific rules:

**Rule 8.1** You can use all standard English punctuation marks but not the semicolon (;).
Write two sentences. *Examine the removed parts; replace the damaged ones* → *(1) Examine the removed parts for damage. (2) Replace the damaged part(s).* *The battery is not user-replaceable; it can only be replaced by an approved service station* → *Users cannot replace the battery. Only specialists at approved service stations can replace it.*

**Rule 8.2** Use hyphens (-) to connect words that are directly related.
Compound modifiers before a noun (*low-altitude flight, quick-release fastener, up-to-date information, self-sealing hose*); two-word numbers (*forty-seven, three-sixteenths*); letter/number + noun shapes (*L-shaped bracket, O-ring, 3-prong connector*); noun-first verbs (*heat-treat, short-circuit, jump-start*); vowel-vowel prefixes (*pre-amplifier, de-icing, anti-icing*).

**Rule 8.3** You can use parentheses: to make references to illustrations or text; to include letters or numbers that identify items; to identify the work steps; to include abbreviations; to give the singular and plural forms of a noun at the same time; to explain words or a part of a sentence; to include an alternative.
*Remove the valve (10, Figure 1).* *A Liquid Crystal Display (LCD) is ...* *Do the applicable test(s).* *Increase the pressure slowly (not more than 10 psi each minute).* *Open the left (right) access panel L42 (R42).*

**Rule 8.4** In a vertical list, a colon (:) has the same effect on word count as a period and shows the end of a sentence.
The lead-in has its own limit (20/25 words); each list item is a new sentence with its own limit.

**Rule 8.5** When you put text in parentheses, it counts as one word in that sentence.
*Make sure that the EMER pushbutton switch is released (the EMER legend is off).* = 10 words; the parenthetical is a separate 5-word sentence. *Remove the safety pin (10).* = 5 words.

**Rule 8.6** Count each of these elements as one word: numbers; numbers together with units of measurement; abbreviations; alphanumeric identifiers; quoted text; titles, headings, placards, and labels; proper nouns of individuals, groups, organizations, and geopolitical entities.
*Do steps 13 thru 16 a minimum of three times.* = 10. *The unit weighs 20 kg.* = 4. *For remote access, use the VPN.* = 6. *Tag circuit breaker 36L7.* = 4. *Touch the "Service Overview" arrow to select the function page.* = 9. *Release the SHORT-CIRCUIT TEST switch.* = 4. A formula is one word. A document or section title is one word (*Refer to Testing and Fault Isolation, page block 1001.* = 6). Text on a placard or label you cannot change counts as one word. *United States of America* = 1, *George Washington* = 1. Step numbers and paragraph numbers are not counted.

**Rule 8.7** Hyphenated words count as one word.
*Clean the surface with a soap-and-water solution.* = 7. *Main-gear-door retraction-winch handle* = 3.

## Section 9 — Writing practices

**Rule 9.1** Use a different sentence construction to write a sentence when a word-for-word replacement is not sufficient.
Word-for-word works when the alternative has the same part of speech and meaning: *acceptable* → *permitted*. Restructure when:
1. The alternative needs a new grammar: *The oil level on the sight gauge must be visible during the test* → *During the test, make sure that you can see the oil level on the sight gauge.* *Cycle the unit twice* → *Operate the unit for two cycles.*
2. Word-for-word gives nonsense: *the service life can be uncertain* → not *cannot be sure* but *it is possible that the service life of this unit will be shorter than usual.*
3. The alternative changes the meaning: *Just apply very light pressure* → *Only apply ...* not *Immediately apply ...*
4. The word is not in the dictionary at all: *The incidence of water in fuel is dangerous* → *Water in fuel is dangerous.*
Ask "what does this word mean here, and what must the reader do?": *Lift the seat so that it clears the track locks* → *Lift the seat until it is away from the track locks.* Often the best fix moves information into a table heading or splits the sentence; the objective is that the reader understands each sentence at first reading.

**Rule 9.2** Use each approved word correctly.
Restricted meanings catch writers out: *wear* means "become damaged by friction" (so *Wear protective clothing* → *Put on protective clothing*); *extend* = increase in size (*This regulation extends to all units* → *is applicable to all units*); *go down* is physical movement (*When the pressure goes down* → *decreases*); *see* is with the eyes (*Move the tube to see if the connection is tight* → *to make sure that*); *turn* = rotate (*The indicator turns green* → *The color of the indicator changes to green*); *above/below* are positions, not limits (*Do not let the pressure go below 20 psi* → *become less than 20 psi*). Part of speech matters: *work* is a noun (*When you do work with cleaning agents*), *help* is a verb (*with the aid of a second person*), *damage* is a noun (*Be careful not to cause damage to the sleeve*). A few words are approved as two parts of speech with distinct meanings (*flush* the pipes / *flush* with the surface).

**Rule 9.3** When you use two words together, do not make phrasal verbs.
Approved words must not combine into a phrase with a new meaning. *After you put out the fire* → *After you extinguish the fire.* *This compound can give off poisonous fumes* → *can release poisonous fumes.* Phrasal verbs are mostly not listed as non-approved, so watch for them yourself. A handful are approved with restricted meaning: *put on*, *come on*, *go off*.

**Rule 9.4** When you select terminology or wording, always use a consistent style.
The same instruction gets the same wording every time it occurs. Non-STE mixes *main body / body / body assembly* and *torque / torque-tighten* and two phrasings for lubrication across eight steps; STE uses one term and one phrasing for each.

## General recommendations (not rules, but follow them)

**GR-1 The conjunction "that".** Keep it after verbs like make sure, show, recommend: *Make sure that the valve is open.* *The gauge shows that the reservoir is full.* It marks where the clause starts and helps translation.

**GR-2 The preposition "with".** It can mean "having", "together with", or "by means of". *Install the panel with the green fasteners* has three readings. Rewrite: *Lift the aircraft at the maximum takeoff weight with passengers* → *(passenger weight included)*. Put the condition first: *When you supply hydraulic pressure, make sure that the lever does not touch the stop (1).* Keep the real action verb: *Use tool TS9867 to seal the opening* → *Seal the opening with tool TS9867.*

**GR-3 How to use pronouns.** Only dictionary pronouns (it, they, that, these, those, you, we...). If a pronoun could refer to more than one noun, repeat the noun: *If you engage the pins incorrectly with the seats, they can become damaged* → *... the pins can become damaged* (or the seats, or both — say which).

**GR-4 The pronoun "this".** Make the referent explicit: *Make sure that the cover is not locked (this can cause damage to the probe)* → *Make sure that the cover is not locked. If the cover is locked, this can cause damage to the probe.*

**GR-5 False friends.** A word that resembles one in the writer's native language may not mean the same in English (*dispositions* is not *instructions*).

**GR-6 Latin abbreviations.** No e.g., i.e., etc. Write *for example*, *that is*, or restructure: *insulation of different colors (blue, green, red, etc.)* → *insulation of different colors. They can be blue, green, red, or other colors.* Or omit.

**GR-7 Inclusive language.** No *he/she*; *man/woman* only where the context needs them (medical text). Use *you*, *the operator*, *personnel*, *they*.

**GR-8 Possessive form.** *the manufacturer's instructions* is permitted but is hard for non-native readers; use it only when you are sure it is correct, otherwise *the instructions of the manufacturer*.
