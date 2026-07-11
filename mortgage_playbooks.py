# mortgage-agents playbooks P01-P10.
PB = [
 dict(num="P01", slug="application-to-file-open", name="Application to File Open",
  desc="Swarm deployment: received application to opened, clock-instantiated, checklist-issued file. Agents 01, 02, 12, 05, 13, 04. The application timestamp is exact - TRID clocks run from it.",
  trigger="`loan.application` package lands at 02.",
  pre=["Application carries provenance per field; government-monitoring data exactly as provided or declined (01's HMDA rule)."],
  phases=[
   ("Phase 1 - Open and clock", [
    ("1","02","Open the file; issue the first milestone","`file.milestone` → 03, 12, 13","milestone state on record"),
    ("2","12","Instantiate TRID and ECOA clocks from the application facts","(clock set)","clocks live with lead-times"),
   ]),
   ("Phase 2 - Evidence base", [
    ("3","02","Issue the program document checklist","`doc.request` → 05","checklist issued and logged"),
    ("4","04","Welcome/status message on the approved template - process facts only","`borrower.message.send`","send logged"),
   ]),
  ],
  gates=["No credit opinion, rate quote, or qualification statement anywhere in this playbook - licensed territory.",
         "Application completeness gaps are NAMED on the file; the clock engine consumes exact dates."],
  completion="File open with milestone state, live clocks, issued checklist, and the welcome sent.",
  abort=["Application-date ambiguity: the earlier candidate date runs the clocks and the ambiguity escalates."]),

 dict(num="P02", slug="disclosure-clock-cycle", name="Disclosure Clock Cycle",
  desc="Swarm deployment: milestone trigger to human-sent disclosure with delivery evidence and waiting-period math. Agents 03, 12, 04, 13. The swarm assembles and watches; the licensed human reviews, signs, and sends - every time.",
  trigger="`file.milestone` reaching a disclosure-triggering state, or a recorded changed-circumstance fact with a human redisclosure decision.",
  pre=["Every package figure cites its file source; the file is current (03's stale-file tuple)."],
  phases=[
   ("Phase 1 - Package", [
    ("1","03","Assemble the disclosure package, per-figure sources cited","`disclosure.package` → human, 13","review-ready package delivered inside the clock lead-time"),
   ]),
   ("Phase 2 - Human send, evidence trail", [
    ("2","03","Record delivery evidence after the human sends: timestamp, method, artifacts","`disclosure.record` → 12, 13","waiting-period inputs exact"),
    ("3","12","Run waiting-period math on the conservative reading; hold anything that would violate it","`deadline.alert` / `compliance.hold`","period state visible; violations held"),
    ("4","04","Borrower disclosure-related communications on approved templates (no figures outside the disclosure lane)","`borrower.message.send`","sends logged"),
   ]),
  ],
  gates=["The swarm never sends a disclosure - human review, signature, and send, always (03's legal line).",
         "Ambiguous delivery evidence runs the later received-date (12's conservatism tuple)."],
  completion="Disclosure sent by the human with evidence recorded and the waiting period running on conservative math.",
  abort=["Package source updated post-assembly: reassemble before human review; stale packages never reach the human as current."]),

 dict(num="P03", slug="document-verification-cycle", name="Document & Verification Cycle",
  desc="Swarm deployment: program checklist to inventoried documents and verbatim verification facts. Agents 05, 06, 04, 02, 13. Anomalies are facts for humans; authenticity and interpretation never happen in the swarm.",
  trigger="`doc.request` checklist issued at file open, or a condition's evidence needs via 09.",
  pre=["The checklist is the ratified program version; chase cadence is the published one."],
  phases=[
   ("Phase 1 - Collect (parallel)", [
    ("1","05","Request, receive, inventory against the checklist; chase on cadence via 04","`doc.received` → 02, 08, 09, 13","item-level inventory current, GLBA custody applied"),
    ("2","06","Execute verification orders through approved channels","`verify.result` → 08, 09, 13","source statements verbatim with timestamps"),
   ]),
   ("Phase 2 - Surface facts", [
    ("3","05","Anomaly facts (gaps, date conflicts, metadata) to the human - never conclusions","(fact flags on inventory)","anomalies named, not judged"),
    ("4","06","Discrepancies between verifications and file statements reported verbatim","(facts on results)","underwriting material delivered as facts"),
   ]),
  ],
  gates=["Letters of explanation are borrower-authored - requested per condition text verbatim, never drafted or coached.",
         "'Unable to verify' is a result, not a problem to solve off-channel."],
  completion="Checklist inventory and verification facts current on the file; anomalies and discrepancies named.",
  abort=["Chase cadence exhausted: human queue with the full history; the cadence ends in a decision."]),

 dict(num="P04", slug="third-party-orders-cycle", name="Third-Party Orders Cycle",
  desc="Swarm deployment: service order to artifact-verified deliverable in the file. Agents 07, 04, 02, 11, 13. Appraiser independence is absolute - no value conversation exists in this playbook or anywhere.",
  trigger="`order.request` from the pipeline (02) or closing coordination (11).",
  pre=["Approved panel/AMC channels only; order terms per existing agreements."],
  phases=[
   ("Phase 1 - Order and track", [
    ("1","07","Place the order through the approved channel; track milestones","`order.status` → 02, 09, 11, 13","milestones with channel references"),
    ("2","07","Coordinate property access via approved templates","`borrower.message.request` → 04","scheduling facts only"),
   ]),
   ("Phase 2 - Deliverables", [
    ("3","07","Verify the deliverable landed as an artifact in the file; defects route back through the channel as facts","`order.status` (deliverable state)","the artifact, not the vendor's word"),
   ]),
  ],
  gates=["Value pressure in any form - including from the human - is an integrity violation (07's tuple).",
         "Appraiser selection and communication stay inside the AMC channel."],
  completion="Deliverables artifact-verified in the file; defects routed through the channel.",
  abort=["Channel unavailable for a required service: escalate; off-channel ordering never substitutes."]),

 dict(num="P05", slug="income-asset-worksheets", name="Income & Asset Worksheets",
  desc="Swarm deployment: verified documents to sourced calculation worksheets for the underwriter. Agents 08, 05, 06, 13. The worksheet computes; the underwriter concludes - and discretionary method choices are theirs.",
  trigger="Sufficient inventoried inputs land for a worksheet, or 09 requests one for a condition.",
  pre=["Ratified method tables are current; inputs are inventoried (not defective) documents and verbatim verification facts."],
  phases=[
   ("Phase 1 - Compute", [
    ("1","08","Assemble worksheets per the ratified method; every line cites source + method rule","`calc.worksheet` → 09, 13","sourced arithmetic, no conclusions"),
    ("2","08","Request missing inputs; blocked lines stay blocked, never estimated","`doc.request` → 05","gaps named per line"),
   ]),
   ("Phase 2 - Deltas", [
    ("3","08","Recalculations name their deltas against prior worksheets explicitly","(delta section on the worksheet)","threshold flips NAMED, never silent"),
   ]),
  ],
  gates=["Method discretion (declining income, variable hours) is flagged to the underwriter, never exercised.",
         "Adjusting inputs toward a target figure is the named integrity violation."],
  completion="Worksheets on the file with full sourcing; deltas named; discretion flags raised.",
  abort=["Method table gap for the income type: no arithmetic; the gap escalates for ratification."]),

 dict(num="P06", slug="conditions-clearing", name="Conditions Clearing",
  desc="Swarm deployment: issued conditions to evidence-complete clearing packages for underwriter decisions. Agents 09, 05, 06, 07, 08, 04, 13. Evidence-complete and cleared are different states - only the underwriter moves a condition to cleared.",
  trigger="Underwriting conditions issued on a file (human event recorded via 13); 09 opens tracking.",
  pre=["Conditions tracked verbatim as issued; ambiguous text goes back to the issuer before any evidence run."],
  phases=[
   ("Phase 1 - Evidence per condition (parallel)", [
    ("1","09","Derive each condition's evidence checklist from its text; orchestrate","`doc.request` → 05 / `verify.order` → 06","evidence runs opened per condition"),
    ("2","09","Attach worksheet and deliverable evidence where conditions reference them","(from `calc.worksheet`, `order.status`)","artifacts attached per condition"),
    ("3","09","Borrower-facing condition requests on approved templates","`borrower.message.request` → 04","requests carry condition text verbatim"),
   ]),
   ("Phase 2 - Packages", [
    ("4","09","Assemble per-condition clearing packages; deliver to the underwriter","`conditions.package` → human, 13","every artifact attached; gaps named"),
    ("5","09","Report state transitions; cleared comes only from the human's act","`condition.status` → 02, 13","state history preserved, reissues never merged"),
   ]),
  ],
  gates=["The swarm never clears, waives, interprets, or modifies a condition.",
         "Evidence-complete is never reported as cleared - conflation is the named failure."],
  completion="Every open condition evidence-complete with its package delivered, or its gap named; cleared states recorded from human acts only.",
  abort=["Condition text ambiguous: back to the issuer; no evidence run on a guessed intent."]),

 dict(num="P07", slug="rate-lock-records", name="Rate Lock Records",
  desc="Swarm deployment: signed lock authority to recorded lock with expiry watched at lead-time. Agents 10, 12, 02, 04, 13. The swarm never locks - it records signed human acts and watches the clock.",
  trigger="Signed `lock.authority` arrives at 10, or an expiry lead-time alert fires.",
  pre=["Authority terms consistent with the file's program of record (10's hold tuple otherwise)."],
  phases=[
   ("Phase 1 - Record", [
    ("1","10","Execute the lock record exactly as authorized, authority envelope_id attached","`lock.record` → 02, 12, 13","terms verbatim; file state updated"),
    ("2","04","Lock confirmation on the approved template - terms as authorized, no commentary","`borrower.message.send`","send logged"),
   ]),
   ("Phase 2 - Watch", [
    ("3","12","Expiry clocks armed; lead-time alerts to 10 and 02","`deadline.alert`","expiry visibility ahead of the date"),
    ("4","10","Expiry lead-time reached: the fact goes to the human - extension is a signed decision","(escalation with dates)","no auto-extension, ever"),
   ]),
  ],
  gates=["No lock, extension, or relock without signed authority - unsigned is an integrity violation.",
         "No rate quotes or market commentary in any channel."],
  completion="Lock recorded as authorized; expiry watched with lead-time alerts; extensions only as new signed acts.",
  abort=["Authority conflicts with the file: hold + re-confirm naming both states."]),

 dict(num="P08", slug="clear-to-close-and-funding-records", name="Clear-to-Close & Funding Records",
  desc="Swarm deployment: cleared file to review-ready closing package, scheduled closing, and funding-event records. Agents 11, 07, 12, 04, 13. The CD send, closing instructions, and funding authorization are human acts - the swarm reconciles paper and calendars.",
  trigger="Clear-to-close state recorded on the file (human underwriting act via 13).",
  pre=["Condition states cleared-by-human; lock state current; title/payoff deliverables artifact-verified."],
  phases=[
   ("Phase 1 - Package and schedule", [
    ("1","11","Assemble the closing package: fee reconciliation per line with sources; variances named","`closing.package` → human, 13","review-ready; nothing self-approved"),
    ("2","11","Schedule closing against the CD waiting period (12's math) and lock expiry facts","`borrower.message.request` → 04","calendar conflicts escalate; the waiting period does not bend"),
    ("3","07","Payoffs and title updates current at lead-time","`order.status` → 11, 13","no stale figures in the package"),
   ]),
   ("Phase 2 - Records", [
    ("4","11","Record funding events as they occur - records of human-authorized acts","`funding.record` → 13","every event tied to its authorization"),
   ]),
  ],
  gates=["Funding and wire movement are never swarm acts; changed wire instructions freeze + re-confirm out-of-band (the named fraud pattern).",
         "Fee variances are named to the human, never absorbed or split."],
  completion="Closing package delivered review-ready; closing scheduled clear of the waiting period; funding events recorded.",
  abort=["Closing date inside the waiting period: immediate escalation; the calendar moves.",
         "Wire-instruction change post-delivery: freeze; out-of-band re-confirmation before anything proceeds."]),

 dict(num="P09", slug="morning-operations", name="Morning Operations",
  desc="Swarm deployment: the pipeline's morning book. Overnight applications, today's TRID/ECOA/lock clocks, stalled files, the closing calendar - assembled from records for human review. Agents 14, 13, 12.",
  trigger="Scheduled daily start (owner-configured time) or owner command.",
  pre=["EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED."],
  phases=[
   ("Assemble (parallel, all to human review)", [
    ("1","14","Pull overnight applications and stalled-file exceptions","`record.request` → 13","sections sourced"),
    ("2","14","Today's clock alerts: disclosures, ECOA, lock expirations","(from 12's alert stream)","clock section current with lead-times"),
   ]),
   ("Present", [
    ("3","14","Deliver the morning book; unavailable sources marked absent","`report.package` → human","book delivered; the human directs"),
   ]),
  ],
  gates=["A source unavailable at assembly is a named absence - never yesterday's numbers backfilled."],
  completion="Morning book delivered with every section sourced or marked absent.",
  abort=["Record source down: section marked absent; the book still delivers on time."]),

 dict(num="P10", slug="end-of-day-books", name="End-of-Day Books",
  desc="Swarm deployment: the closing books. Milestones advanced, packages to humans, locks recorded, clocks reconciled, the missed-item sweep. Agents 14, 13, 12. Gaps named; a clean-looking book with hidden gaps is the named failure.",
  trigger="Scheduled day end (owner-configured time) or owner command.",
  pre=["The morning book (P09) exists as the sweep baseline; if absent, the sweep names that first."],
  phases=[
   ("Assemble", [
    ("1","14","Pull the day's activity: milestones, packages delivered, locks, closings, funding events","`record.request` → 13","activity sections sourced with timestamps"),
    ("2","14","Clock reconciliation: satisfied, at-risk, missed - quantified with owners","(from 12's stream + records)","reconciliation complete"),
    ("3","14","Missed-item sweep against the morning book","(sweep vs. P09 baseline)","sweep complete; no silent reassignment"),
   ]),
   ("Present", [
    ("4","14","Deliver the EOD books","`report.package` → human","books delivered; P10 completion logged for tomorrow's P09"),
   ]),
  ],
  gates=["The sweep never reassigns - it names. Reassignment is the human's morning decision."],
  completion="EOD books delivered; sweep complete with owners named; completion event logged.",
  abort=["Morning baseline absent: the sweep names that first and proceeds on records alone."]),
]
