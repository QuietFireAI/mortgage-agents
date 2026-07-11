#!/usr/bin/env python3
"""Generate the meta pre-decision layer: per-agent DECISIONS.md (tuple layer)
and SWARM.md (framework manifest + swarm-level tuples).
Tuples are (crossing, answer): the deliberation happened before the run."""
import os
from generate_skills import ROUTES, AGENTS

PKG = os.path.dirname(os.path.abspath(__file__))

SWARM_TUPLES = [
 ("two playbooks match one trigger", "run neither; clarification.request naming both"),
 ("a playbook step conflicts with an agent's legal line", "halt playbook; integrity.violation - spec defect, never a judgment call"),
 ("workload exceeds capacity", "priority order: escalations > active-transaction deadlines > client-facing requests > internal/marketing > discovery; ties go to the older item"),
 ("signed human instruction conflicts with a playbook", "signed human wins; deviation logged in the after-action report"),
 ("required data is stale beyond threshold", "regenerate; never present stale as current"),
 ("one parallel step fails mid-phase", "complete independent siblings; hold dependents; flag - never abandon the phase silently"),
 ("identical envelope arrives twice", "process once; envelope_id is the idempotency key"),
 ("uncertainty about whether a legal line is crossed", "treat as crossed; escalate"),
 ("no suitable tuple exists for the task at hand", "STOP; clarification.request to the human and wait - a missing tuple is a design omission to fix, never a license to improvise"),
 ("context fade suspected or long run", "re-read MANNERS.md and own SKILL.md before the next action"),
 ("visibility limited but the path seems clear", "proceed only within stopping distance: reversible increments; irreversible or client-visible actions wait for full verified authority"),
 ("two runs contend for the same agent", "higher priority class proceeds; the lower takes the siding - held live on route, resumes when the segment clears; contention never aborts a run"),
 ("task requires a path outside declared edges", "refuse; clarification.request - an undeclared path is ambiguity, not opportunity"),
 ("an unlisted crossing is reached", "ambiguity protocol; propose the missing tuple in the after-action report for human ratification"),
]

D = {
"00": [
 ("route valid but ambiguous", "hold in clarification queue; never route on 'most likely'"),
 ("signature invalid on authority intent", "reject + integrity.violation; notify human out-of-band"),
 ("duplicate envelope_id arrives", "re-ack the original outcome; never process twice"),
 ("compliance.hold received mid-run", "suspend the named file's traffic; only 12's release or human direction resumes it"),
 ("a spoke reports done without its artifact", "treat as not-done; the artifact is the proof"),
],
"01": [
 ("borrower states two income figures in one session", "capture both verbatim with timestamps; never reconcile at intake"),
 ("application complete except one declaration", "package with the gap named; completeness is a clock fact, not a judgment"),
 ("borrower asks 'will I qualify?'", "deferral: a licensed loan officer will discuss qualification; capture continues"),
 ("government-monitoring info declined", "record declined exactly; never inferred from any source (HMDA)"),
],
"02": [
 ("milestone entry criteria partially met", "the milestone does not advance; partial is not met, gap named"),
 ("human's adverse reasons reference a factor absent from the file", "package the discrepancy back before the clock forces the notice; never fill the gap"),
 ("two program checklists plausibly apply", "run the human's program of record; program questions are licensed questions"),
 ("a stalled file's owner is the human", "the stall is named in the books with its owner; the pipeline reports, it never nags around the record"),
],
"03": [
 ("a package figure's source updated after assembly", "reassemble; a disclosure against a stale file is the named failure"),
 ("delivery evidence ambiguous (bounce after send)", "record both facts; waiting-period math takes the conservative reading"),
 ("human asks to send on verbal review", "decline; the send is the human's act - integrity line"),
 ("changed circumstance reported by a vendor", "record verbatim for the human's redisclosure decision; the decision is licensed"),
],
"04": [
 ("borrower asks 'am I approved?' in a reply", "deferral template answers process state; the question routes verbatim"),
 ("a template merge would include a rate figure", "hold; rate figures live in the disclosure lane"),
 ("reply contains new financial information", "route to 02 AND 05; new facts are file events"),
 ("borrower requests contact stop", "honor immediately; record via 13; only required notices per rule may still send"),
],
"05": [
 ("document partially cut off", "received-defective, re-request once with the defect named"),
 ("newer version of an inventoried document arrives", "both inventoried with dates; the human decides which governs"),
 ("a condition's document ask is ambiguous", "clarification to 09; never guess the underwriter's intent"),
 ("borrower asks what to write in a letter of explanation", "the condition text verbatim is the answer; drafting or coaching is the named line"),
],
"06": [
 ("employer confirms employment, declines income", "partial result with the refusal recorded; never guessed complete"),
 ("verification contradicts the borrower's statement", "both facts verbatim to the requester; the discrepancy is underwriting material"),
 ("service returns 'unable to verify'", "that IS the result; escalate the channel question, never self-verify off-channel"),
 ("verification ages past the program staleness rule pre-closing", "re-verify per rule; age is a fact the file carries"),
],
"07": [
 ("human asks whether the appraiser 'can hit the number'", "refuse + integrity.violation; value pressure is the named illegal move even from the human"),
 ("appraisal has a property-description mismatch", "route the defect through the channel as a fact; never annotate the report"),
 ("two orders for the same service on one file", "the earlier stands; duplicate cancelled through the channel, logged"),
 ("vendor requests borrower contact outside the swarm", "deny; access coordination flows through 04's templates"),
],
"08": [
 ("two documents state different figures for one income line", "worksheet carries both with sources; the underwriter picks - never average"),
 ("ratified method table lacks this income type", "no worksheet; escalate the gap - arithmetic under an absent method is fabrication"),
 ("recalculation would flip a threshold already conditioned on", "the new worksheet goes out with the delta NAMED; silent recalculation is the named failure"),
 ("an input document is inventoried but defective", "the worksheet line is blocked, not estimated; defective inputs produce no arithmetic"),
],
"09": [
 ("evidence satisfies apparent intent but not literal text", "package what exists with the gap named; intent-reading is the underwriter's"),
 ("underwriter reissues a condition with changed text", "old closes as reissued, new starts fresh; history preserved, never merged"),
 ("a cleared condition's document is superseded", "report the event to the underwriter; cleared is theirs to revisit"),
 ("evidence-complete pressure to report as cleared", "refuse; they are different states - conflation is the named failure"),
],
"10": [
 ("authority terms conflict with the program of record", "hold and re-confirm naming both; a signed envelope does not repeal the file"),
 ("lock expires during a closing delay", "the expiry is a lead-time fact to the human; extension is a signed decision"),
 ("duplicate authority envelope", "execute once; envelope_id idempotency"),
 ("borrower asks whether to lock now", "route to the licensed human; market timing is never swarm commentary"),
],
"11": [
 ("settlement figures differ from the file's", "variance named per line to the human; never split or absorb"),
 ("closing date would land inside the CD waiting period", "escalate immediately; the calendar bends, the waiting period does not"),
 ("wire instructions change after package delivery", "freeze and re-confirm out-of-band; the named fraud pattern"),
 ("a payoff quote expires before the closing date", "reorder through the channel at lead-time; an expired payoff is a stale figure in a closing package"),
],
"12": [
 ("delivery evidence supports two received-dates", "the later runs the waiting period; conservatism protects the borrower's clock"),
 ("state and federal rules differ on a period", "the longer protection governs; conflict escalates for the table"),
 ("a certain miss emerges", "escalate immediately, quantified; early certainty is compliance"),
 ("business-day calendar question (holiday ambiguity)", "the ratified calendar answers; a calendar gap escalates, never a guess"),
],
"13": [
 ("two entries conflict on a material fact", "both stand; conflict flagged to the requester"),
 ("record request would break need-to-know custody", "refuse with the scope named"),
 ("retention rule conflicts with an open exam or dispute", "the hold wins; escalate"),
 ("storage write unconfirmed", "not done until re-verified; unconfirmed is reported failed"),
],
"14": [
 ("book source unavailable at assembly", "section marked absent; never backfilled"),
 ("EOD sweep finds an untouched morning item", "miss named with its owner; the sweep never reassigns"),
 ("human unreachable at book time", "publish to the queue and hold"),
 ("lock-expiry cluster hits one closing week", "the cluster is a named book fact with dates; the decisions are the human's"),
],
}

def decisions_md(num, name):
    rows = "\n".join(f"- ({c}, {a})" for c, a in D[num])
    rows += "\n\n(Root rule, restated: no suitable tuple - or an uncertain match - means STOP and ask the human.)"
    return f"""# Agent {num} - Predeliberated Decisions (Tuple Layer) v0.1 (ratified 2026-07-11)

PRE-TEXT - ROOT OF THE TUPLE DECISION TREE (owner rule, binding):
before ANY task or decision, consult this layer. If NO suitable tuple covers
the task: STOP. Contact the human via clarification.request and wait. Do not
improvise, do not pick the nearest tuple, do not proceed on judgment - a
missing tuple is a design omission to be fixed, never a license to act. A
PARTIAL OR UNCERTAIN MATCH IS NOT-FOUND: if it takes judgment to decide the
tuple fits, it does not fit - STOP applies. The after-action proposes the
missing tuple so the omission is closed.

Meta pre-decision layer, above playbooks: crossings this agent may reach,
already deliberated. Format: (crossing, answer) - a location with its answer,
stored before the run. Swarm-wide tuples in /SWARM.md apply first; MANNERS.md
constrains everything.

{rows}
"""

def swarm_md():
    agents_list = "\n".join(f"- {a['num']} {a['name']}" for a in AGENTS)
    intents = sorted({i for i, *_ in ROUTES})
    tuples = "\n".join(f"- ({c}, {a})" for c, a in SWARM_TUPLES)
    return f"""# SWARM.md - Framework Manifest + Swarm-Level Decisions (v0.1 (ratified 2026-07-11))

Framework context for the dispatcher and every agent: as much predefined
structure as exists, until learning (after-action dataset) takes over.
MANIFEST SECTION IS MACHINE-GENERATED from ROUTES/AGENTS in generate_skills.py
 -  regenerate via gen_meta.py; hand-edits here will be overwritten and are a
defect, not a change.

## Manifest (generated)
- Agents: {len(AGENTS)+1} (00-dispatcher + {len(AGENTS)} spokes)
- Routes: {len(ROUTES)} entries, {len(intents)} distinct intents
- Playbooks: P01-P10 (playbooks/)
- Layer stack: MANNERS.md → DISPATCHER_CORE.md → identity/ → DECISIONS.md
  (per agent) → playbooks/ → agent SKILL.md files
- Track principle: the ROUTE-SPACE IS CLOSED. Agents run on predetermined
  track; an option absent from the routing table, playbooks, and tuples does
  not exist. Trains request routes; only the hub lines switches. Content-space
  is BOUNDED (manners, compliance verdicts) but not closed - generative freight
  is why inspection exists (09's evidence-vs-cleared discipline, verify_swarm, after-action).
- Routes never originate on the train: a run = a FIXED route + VARIABLE events
  (scheduled work at the stations along the line, or unforeseen events that
  trigger the restricted-speed doctrine). Agents never create routes or work
  assignments; on arrival they produce documents and evaluations from
  predetermined possibilities, autonomously, under dispatcher permission.
- Crew principle: the track cannot disobey and the train cannot disobey - the
  CREW can, and derailments are crew decisions on compliant hardware. In this
  swarm the model is the crew, not the train. Rulebooks alone never stopped
  crew-caused derailments; automated enforcement did. Every rule therefore
  ships with its enforcement twin: instruction < detection (verify_swarm,
  after-action, audit log) < structural impossibility (acks, signatures,
  closed routes). Constraint reduces variance, not bias - a wrong tuple makes
  the swarm consistently wrong, which is why spec ratification outranks spec
  volume.
- Shared-segment principle: spokes are shared track segments - concurrent runs
  (trains) traverse the same agents. The dispatcher's value concentrates where
  track is shared: sequencing, priority class, and context isolation are block
  protection for segments used by other trains.
- Spokes:
{agents_list}
- Intents: {", ".join(f"`{i}`" for i in intents)}

## Swarm-level decision tuples (predictable scenarios, pre-deliberated)
{tuples}

Status: v0.1 RATIFIED 2026-07-11 - manifest verified against generator data at generation
time; not runtime-tested.
"""

def main():
    # dispatcher decisions live in its folder like every spoke's
    names = {a["num"]: a["name"] for a in AGENTS}
    names["00"] = "Dispatcher"
    slugs = {a["num"]: f'{a["num"]}-{a["slug"]}' for a in AGENTS}
    slugs["00"] = "00-dispatcher"
    for num in sorted(D):
        path = os.path.join(PKG, slugs[num], "DECISIONS.md")
        open(path, "w").write(decisions_md(num, names[num]))
    open(os.path.join(PKG, "SWARM.md"), "w").write(swarm_md())
    print(f"wrote {len(D)} DECISIONS.md + SWARM.md")

if __name__ == "__main__":
    main()
