import json, re, subprocess, sys, os
# Usage: python3 evals/grade.py <iteration-dir>  (layout: <iter>/eval-N-name/{with_skill,without_skill}/run-1/outputs/)
CHECK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "ste_check.py")
ITER = sys.argv[1]

# generous glossary so word-approval assertion tests only general vocabulary
GLOSSARY = """pedestal
smart pedestal
meter
revenue-grade meter
breaker
upstream breaker
circuit breaker
upstream circuit breaker
terminal
terminals
terminal screw
anchor bolt
concrete base
base
shim
cable gland
gland
bottom gland
supply cable
conductor
earth conductor
earth bar
ground conductor
ground bar
neutral conductor
phase conductor
insulation
wiring diagram
door
cover
display
troubleshooting
voltmeter
rating
enclosure
steel
powder coating
powder-coated steel
key
keys
quick-start card
quick-start guide
installer
firmware
firmware version
home screen
setup menu
setup screen
setup
menu
tariff
LED
fault
detergent
detergent solution
cloth
solvent
water
hose
water hose
cross-section
commissioning
manual
head-end system
head-end
RS-485 cable
cable
termination
polarity
resistor
bus
device
manufacturer
lock
lockout
green
red
electric shock
voltage
communication
analysis
inspection
evaluation
save
communicate
kit
mm
"""
open(f"{ITER}/glossary-grading.txt", "w").write(GLOSSARY)

def ste_body(md):
    """Strip the compliance-notes section and code fences so only the deliverable is checked."""
    md = re.split(r"\n#+\s*STE compliance notes|\n\*\*STE compliance notes|\n---\s*\n\s*#+\s*(?:STE )?[Cc]ompliance", md)[0]
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    return md

def corrected_section(md):
    """For the review eval: take text after a 'Corrected' heading."""
    m = re.search(r"#+[^\n]*(Corrected|STE version|Rewritten)[^\n]*\n(.*)", md, re.S | re.I)
    return m.group(2) if m else md

def run_checker(text, mode="auto"):
    p = f"{ITER}/_tmp_check.md"
    open(p, "w").write(text)
    out = subprocess.run(["python3", CHECK, p, "--glossary", f"{ITER}/glossary-grading.txt", "--mode", mode, "--json"], capture_output=True, text=True)
    return json.loads(out.stdout)

def grade(eval_dir, cfg, fname, kind):
    path = f"{ITER}/{eval_dir}/{cfg}/run-1/outputs/{fname}"
    if not os.path.exists(path):
        return [{"text": "output file exists", "passed": False, "evidence": f"{path} missing"}]
    md = open(path).read()
    body = ste_body(md)
    if kind == "review":
        body = ste_body(corrected_section(md))
    rep = run_checker(body)
    f = rep["findings"]
    words = rep["words"]
    na = {k: v for k, v in words.items() if v["kind"] == "non_approved"}
    hard = lambda k: [x for x in f if x["kind"] == k and not x["rule"].endswith("?")]
    exp = []
    def A(text, passed, evidence):
        exp.append({"text": text, "passed": bool(passed), "evidence": evidence})

    A("No semicolons in the STE text (Rule 8.1)", not hard("punctuation"), f"{len(hard('punctuation'))} semicolon findings")
    A("No perfect tenses or 'been' (Rule 3.4)", not hard("tense"), "; ".join(x["message"] for x in hard("tense"))[:300] or "none")
    A("No -ing verb forms (Rule 3.5)", not hard("ing"), "; ".join(x["message"] for x in hard("ing"))[:300] or "none")
    A("No sentence over the 20/25-word limit (Rules 5.1, 6.3)", not hard("length"), "; ".join(x["message"] for x in hard("length"))[:400] or "none")
    A("No contractions or Latin abbreviations (Rule 4.2, GR-6)", not hard("contraction") and not hard("latin"), "; ".join(x["message"] for x in hard("contraction") + hard("latin"))[:300] or "none")
    A("No passive 'by' constructions (Rule 3.6)", not [x for x in f if x["rule"] == "3.6"], "; ".join(x["message"] for x in f if x["rule"] == "3.6")[:300] or "none")
    A("No non-approved general-vocabulary words (Rules 1.1–1.3), product terms excused", len(na) == 0, ", ".join(f"{k}->{v['alts'][:40]}" for k, v in list(na.items())[:12]) or "none")
    # safety instruction shape
    warns = re.findall(r"(?:WARNING|CAUTION)\s*:?\**\s*([^\n]+)", body)
    if kind != "review":
      shape_ok = bool(warns) and all(re.match(r"\s*(BEFORE|IF|WHEN|WHILE|DO NOT|DO |MAKE SURE|SET |LOCK|USE |PUT |KEEP|ALWAYS|NEVER|REMOVE|DISCONNECT|CONNECT)", w.strip("* "), re.I) for w in warns)
      A("Every WARNING/CAUTION starts with a command or condition (Rule 7.2)", shape_ok, " | ".join(w[:60] for w in warns) or "no safety instruction found")
      conseq = bool(warns) and all(re.search(r"(CAN CAUSE|CAN OCCUR|CAN KILL|CAN RESULT|CAN DAMAGE|CAUSES|IS DANGEROUS|ARE DANGEROUS|CAN BE DANGEROUS|POISONOUS|RISK)", w, re.I) for w in warns)
      A("Every WARNING/CAUTION states the risk or result (Rule 7.3)", conseq, " | ".join(w[-60:] for w in warns) or "no safety instruction found")
    A("Uses 'make sure that' instead of ensure/verify/confirm", "make sure that" in body.lower() and not re.search(r"\b(ensure|verify|confirm)\b", body, re.I), "make sure present" if "make sure that" in body.lower() else "make sure absent")
    A("No note contains an instruction (Rule 5.5)", not re.search(r"NOTE:\**\s*(Do not|Connect|Set|Make sure|Remove|Install|Refer)\b", body), (re.search(r"NOTE:\**\s*[^\n]{0,60}", body).group(0) if re.search(r"NOTE:", body) else "no note"))
    return exp, body

def numbers_kept(body, nums):
    missing = [n for n in nums if n not in body.replace(" ", " ")]
    return not missing, f"missing: {missing}" if missing else "all present"

evals = {
  "eval-0-rewrite-install-instructions": ("installation-ste.md", "rewrite", ["45 Nm", "2.5 Nm", "15 mm", "M12", "L1", "L2", "L3"]),
  "eval-1-write-quickstart-from-notes": ("quickstart-ste.md", "write", ["600", "150", "45 Nm", "2.5 Nm", "16", "35", "3 s", "5 s", "IP66", "M40", "M12", "400 V"]),
  "eval-2-review-troubleshooting-text": ("review.md", "review", ["120", "RS-485", "A and B"]),
}
for ed, (fname, kind, nums) in evals.items():
    for cfg in ("with_skill", "without_skill"):
        exp, body = grade(ed, cfg, fname, kind)
        ok, ev = numbers_kept(body, nums)
        exp.append({"text": "All numbers, units, and identifiers from the source preserved", "passed": ok, "evidence": ev})
        if kind == "review":
            md = open(f"{ITER}/{ed}/{cfg}/run-1/outputs/{fname}").read()
            has_81 = bool(re.search(r"\b8\.1\b", md)) and "semicolon" in md.lower()
            has_53 = bool(re.search(r"\b5\.3\b", md))
            has_34 = bool(re.search(r"\b3\.4\b", md))
            exp.append({"text": "Cites the correct Issue 9 rule numbers (8.1 semicolon, 5.3 imperative, 3.4 tense)", "passed": has_81 and has_53 and has_34, "evidence": f"8.1:{has_81} 5.3:{has_53} 3.4:{has_34}"})
            exp.append({"text": "Flags 'check' as a non-approved verb with the MAKE SURE/EXAMINE alternative", "passed": bool(re.search(r"check.{0,80}(make sure|examine)", md, re.I | re.S)), "evidence": "found" if re.search(r"check.{0,80}(make sure|examine)", md, re.I | re.S) else "not found"})
        passed = sum(e["passed"] for e in exp)
        json.dump({"expectations": exp, "summary": {"passed": passed, "failed": len(exp)-passed, "total": len(exp), "pass_rate": passed / len(exp)}}, open(f"{ITER}/{ed}/{cfg}/run-1/grading.json", "w"), indent=1)
        print(f"{ed:45s} {cfg:14s} {passed}/{len(exp)}")
        for e in exp:
            if not e["passed"]:
                print("     FAIL:", e["text"], "--", e["evidence"][:150])
