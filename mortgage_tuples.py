# mortgage-agents tuple layer.
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
