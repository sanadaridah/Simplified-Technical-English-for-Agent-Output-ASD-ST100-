# Technical nouns and technical verbs — the categories (Rules 1.5 and 1.12)

Words that are not in the STE dictionary are permitted only if they fit one of these categories. The lists are the standard's own examples; they are illustrations, not a closed list. When you accept a word as a technical noun or verb, you should be able to name its category. Keep a project glossary of the ones you accept (one per line) and pass it to `scripts/ste_check.py --glossary` so the checker stops flagging them.

Reminders that go with these categories:
- A technical noun is used only as a noun or as a modifier inside another technical noun, never as a verb (Rule 1.7): *apply oil*, not *oil the surface*.
- A technical verb is used only as a verb, never as a noun (Rule 1.13); its past participle may be an adjective (*the reamed hole*).
- Prefer an approved dictionary verb over a technical verb whenever the dictionary verb gives the instruction accurately (*find* broken wires, not *detect*).
- Take the technical noun your company, industry, or parts catalog uses (Rule 1.8). Keep it to three words or fewer (Rule 1.9). No slang, jargon, or regionalisms (Rule 1.10). One name per item throughout the document (Rule 1.11).

## Technical noun categories (Rule 1.5)

1. **Official parts information** — design items from parts catalogs and drawings: bolt, cable, clip, conductor, contact, engine, filter, hatch, indicator, light, oil seal, pipe, propeller, screw, switch, transceiver.
2. **Vehicles or machines, and locations on them** — aircraft, bicycle, cabin, car, cargo compartment, cockpit, deck, engine room, fuselage, helicopter, ship, tank, train, truck, wing.
3. **Tools and support equipment, their parts, and locations on them** — access ladder, blade, brush, cap, clamp, cover, display, drill, file, gauge (gage), handle, jack, label, roller, rope, shaft, stand, tag, test rig, torque wrench.
4. **Materials, consumables, and unwanted material** — acid, adhesive, aluminum alloy, compound, copper, debris, detergent, dirt, dust, foam, foreign object, fuel, grease, hazardous waste, metal, oil, paint, plastic, primer, sealant, soap, stainless steel, tape, waste, water, wire.
5. **Facilities, infrastructure, and logistic procedures** — airport, base, building, dock, gate, handling, hangar, packaging, packing, port, service bay, shipping, shop, storage, transport.
6. **Systems, components and circuits, their functions, configurations, and parts** — air conditioning, amplifying circuit, audio, exhaust, hardware, inlet, input frequency, latch, pedal, power unit, pump, reverse mode, standby mode, upright position, vent.
7. **Mathematical, scientific, engineering terms, and formulas** — acceleration, average, capacitance, center, circle, coefficient, configuration, count, curve, cycle, defect, degree, density, diameter, duty cycle, electricity, energy, failure, force, gravity, hardness, heat treatment, ignition, interference, load, loss, measurement, modification, phase, polarity, power, pressure, process, radius, ratio, resistance, signal, standard, strength, temperature, tension, thread, torque, vapor, voltage, "C = (A - B) - 0.063 mm".
8. **Navigation and geographic terms** — altitude, attitude, axis, clearance, coordinates, datum, deviation, drag, east, heading, landing, north, pitch, roll, south, west.
9. **Numbers, units of measurement and time (and their symbols)** — 92, ampere (A), degree, first (1st), half (½), hour (h), kilogram (kg), liter (L), meter (m), minute, month, ohm, one, second (s), three, year, winter, zero.
10. **Quoted text** — text you cannot change: placards, labels, signs, markings, display text: abort button, EXIT sign, ON position, NEXT button, FAULT legend, NO STEP marking.
11. **Professional roles, individuals, groups, organizations, and geopolitical entities** — air traffic control, captain, crew, crew chief, manufacturer, operator, Federal Aviation Administration (FAA), Transport Canada Civil Aviation (TCCA), United States of America (USA).
12. **Parts of the body** — blood, ear, eyes, hair, hand, head, lung, mouth, skin, stomach.
13. **Common personal effects, food, and beverages** — clothing, coffee, footwear, jewelry, matches, milk, shampoo.
14. **Medical terms** — allergy, aspirin, breathing, circulation, dizziness, headache, heart rate, irritation, medication, nausea, pulse, skin irritation.
15. **Official documents, parts of documentation, standards, and guidelines** — caution, chapter, checklist, danger, diagram, figure, flowchart, font, issue, letter, note, notice, page, paragraph, prerequisite, reference, revision, section, service bulletin, table, test procedure, training material, warning, and named manuals and sections (Removal/Installation, Structural Repair Manual).
16. **Environmental and operational conditions** — atmosphere, cloud, day, daylight, ice, humidity, lightning, moisture, night, rain, sand, snow, storm, wind.
17. **Colors** — beige, black, dark brown, gray, green, orange, red, white, yellow. (No comparatives: not *redder*.)
18. **Damage terms** — buckle, chafing, corrosion, crack, deformation, dent, discoloration, distortion, erosion, fracture, kink, nick, score, scratch, stain, spurious fault message.
19. **Computer science, information and communication technology** — add-on, AI, arrow, artificial intelligence, authentication, backup, backup file, bookmark, chatbot, content, cursor, cybersecurity, database, dialog check box, e-mail, field, file, firewall, HTML, icon, interface, internet, laptop, large language model, machine learning, memory, menu, metadata, mouse, network, operating system, phone, plug-in, preset value, remote operation, screen, search engine, smartphone, status bar, store, tablet, token, toolbar, touchscreen, update, voice mail, XML.
20. **Civil and military operations** — armed forces, checkpoint, contractor, customer, customer support, customer service, deployment, end user, evacuation, lifecycle, maintenance concept, mission, obsolescence, operator, Original Equipment Manufacturer (OEM), patrol.
21. **Law and regulations** — action, ambiguity, appeal, arbitration, communication, competence, compliance, contract, court, damages, explanation, jurisdiction, law, purpose, recommendation, scope, signature, statute, term, waiver, wording.
22. **Animals, plants, and other life forms** — bacteria, bird, cat, dog, fungi, horse, insect, moss, mouse, termite.

## Technical verb categories (Rule 1.12)

1. **Manufacturing processes** — remove material: drill, grind, mill, ream, unsolder; add material: flame, insulate, remetal, retread; attach material: braze, crimp, solder, weld; change properties: anneal, cure, decay, freeze, heat-treat, magnetize, normalize, vaporize; change surface finish: buff, burnish, dress, passivate, plate, polish; change shape: blend, cast, extrude, spin, stamp.
2. **Computer processes and applications** — input/output: click, digitize, enter, press, print, swipe, tap, type; user interface: clear, close, copy, cut, delete, deselect, disable, drag, drag and drop, enable, encrypt, erase, filter, highlight, maximize, minimize, navigate, open, paste, save, scroll, sort, store, validate, zoom in, zoom out; system operations: abort, boot, communicate, debug, download, format, install, load, manage, process, reboot, update, upgrade, upload.
3. **Instructions and information for applicable subject fields** — engineering/scientific: bisect, compensate for, convert, detect, float, modulate, radiate, transform; medical: disinfect, intubate, operate, prescribe, sanitize, sterilize; civil and military: aim, arm, detect, disable, enable, explode, fire, inhibit, intercept, load, unlatch, unload; navigation: approach, descend, deviate, fly, hover, land, maintain, navigate, taxi, trim; automotive and railway: accelerate, brake, couple, crank, decouple, drift, inflate, park, steer; energy, oil, and gas: compress, distill, drill, emit, extract, inject, pump.
4. **Law and regulations** (legal and regulatory texts only) — acknowledge, comply with, conform to, describe, enforce, explain, inform, meet (a requirement), modify, notify, omit, regulate, sign, supersede, understand, waive.

A technical verb keeps its category context. *Enter your password* (ICT) is fine; *enter the test area* is not (use *go into*). *If the tower does not respond* (navigation) is fine; *if the instrument fails to respond* is not (use *does not operate correctly*).
