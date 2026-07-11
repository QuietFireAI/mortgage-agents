---
name: P08-clear-to-close-and-funding-records
description: "Swarm deployment: cleared file to review-ready closing package, scheduled closing, and funding-event records. Agents 11, 07, 12, 04, 13. The CD send, closing instructions, and funding authorization are human acts - the swarm reconciles paper and calendars."
---

# Playbook P08 - Clear-to-Close & Funding Records

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
Clear-to-close state recorded on the file (human underwriting act via 13).

## Preconditions
- Condition states cleared-by-human; lock state current; title/payoff deliverables artifact-verified.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Package and schedule
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 11 | Assemble the closing package: fee reconciliation per line with sources; variances named | `closing.package` → human, 13 | review-ready; nothing self-approved |
| 2 | 11 | Schedule closing against the CD waiting period (12's math) and lock expiry facts | `borrower.message.request` → 04 | calendar conflicts escalate; the waiting period does not bend |
| 3 | 07 | Payoffs and title updates current at lead-time | `order.status` → 11, 13 | no stale figures in the package |

### Phase 2 - Records
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 11 | Record funding events as they occur - records of human-authorized acts | `funding.record` → 13 | every event tied to its authorization |

## HITL gates (hard stops)
- Funding and wire movement are never swarm acts; changed wire instructions freeze + re-confirm out-of-band (the named fraud pattern).
- Fee variances are named to the human, never absorbed or split.

## Completion criteria
Closing package delivered review-ready; closing scheduled clear of the waiting period; funding events recorded.

## Abort paths
- Closing date inside the waiting period: immediate escalation; the calendar moves.
- Wire-instruction change post-delivery: freeze; out-of-band re-confirmation before anything proceeds.
