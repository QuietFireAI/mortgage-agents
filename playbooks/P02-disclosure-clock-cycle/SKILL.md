---
name: P02-disclosure-clock-cycle
description: "Swarm deployment: milestone trigger to human-sent disclosure with delivery evidence and waiting-period math. Agents 03, 12, 04, 13. The swarm assembles and watches; the licensed human reviews, signs, and sends - every time."
---

# Playbook P02 - Disclosure Clock Cycle

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
`file.milestone` reaching a disclosure-triggering state, or a recorded changed-circumstance fact with a human redisclosure decision.

## Preconditions
- Every package figure cites its file source; the file is current (03's stale-file tuple).
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Package
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 03 | Assemble the disclosure package, per-figure sources cited | `disclosure.package` → human, 13 | review-ready package delivered inside the clock lead-time |

### Phase 2 - Human send, evidence trail
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 2 | 03 | Record delivery evidence after the human sends: timestamp, method, artifacts | `disclosure.record` → 12, 13 | waiting-period inputs exact |
| 3 | 12 | Run waiting-period math on the conservative reading; hold anything that would violate it | `deadline.alert` / `compliance.hold` | period state visible; violations held |
| 4 | 04 | Borrower disclosure-related communications on approved templates (no figures outside the disclosure lane) | `borrower.message.send` | sends logged |

## HITL gates (hard stops)
- The swarm never sends a disclosure - human review, signature, and send, always (03's legal line).
- Ambiguous delivery evidence runs the later received-date (12's conservatism tuple).

## Completion criteria
Disclosure sent by the human with evidence recorded and the waiting period running on conservative math.

## Abort paths
- Package source updated post-assembly: reassemble before human review; stale packages never reach the human as current.
