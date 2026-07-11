---
name: P03-document-verification-cycle
description: "Swarm deployment: program checklist to inventoried documents and verbatim verification facts. Agents 05, 06, 04, 02, 13. Anomalies are facts for humans; authenticity and interpretation never happen in the swarm."
---

# Playbook P03 - Document & Verification Cycle

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`doc.request` checklist issued at file open, or a condition's evidence needs via 09.

## Preconditions
- The checklist is the ratified program version; chase cadence is the published one.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Collect (parallel)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 05 | Request, receive, inventory against the checklist; chase on cadence via 04 | `doc.received` → 02, 08, 09, 13 | item-level inventory current, GLBA custody applied |
| 2 | 06 | Execute verification orders through approved channels | `verify.result` → 08, 09, 13 | source statements verbatim with timestamps |

### Phase 2 - Surface facts
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 05 | Anomaly facts (gaps, date conflicts, metadata) to the human - never conclusions | (fact flags on inventory) | anomalies named, not judged |
| 4 | 06 | Discrepancies between verifications and file statements reported verbatim | (facts on results) | underwriting material delivered as facts |

## HITL gates (hard stops)
- Letters of explanation are borrower-authored - requested per condition text verbatim, never drafted or coached.
- 'Unable to verify' is a result, not a problem to solve off-channel.

## Completion criteria
Checklist inventory and verification facts current on the file; anomalies and discrepancies named.

## Abort paths
- Chase cadence exhausted: human queue with the full history; the cadence ends in a decision.
