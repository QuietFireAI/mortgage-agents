---
name: P01-application-to-file-open
description: "Swarm deployment: received application to opened, clock-instantiated, checklist-issued file. Agents 01, 02, 12, 05, 13, 04. The application timestamp is exact - TRID clocks run from it."
---

# Playbook P01 - Application to File Open

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`loan.application` package lands at 02.

## Preconditions
- Application carries provenance per field; government-monitoring data exactly as provided or declined (01's HMDA rule).
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Open and clock
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 02 | Open the file; issue the first milestone | `file.milestone` → 03, 12, 13 | milestone state on record |
| 2 | 12 | Instantiate TRID and ECOA clocks from the application facts | (clock set) | clocks live with lead-times |

### Phase 2 - Evidence base
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 02 | Issue the program document checklist | `doc.request` → 05 | checklist issued and logged |
| 4 | 04 | Welcome/status message on the approved template - process facts only | `borrower.message.send` | send logged |

## HITL gates (hard stops)
- No credit opinion, rate quote, or qualification statement anywhere in this playbook - licensed territory.
- Application completeness gaps are NAMED on the file; the clock engine consumes exact dates.

## Completion criteria
File open with milestone state, live clocks, issued checklist, and the welcome sent.

## Abort paths
- Application-date ambiguity: the earlier candidate date runs the clocks and the ambiguity escalates.
