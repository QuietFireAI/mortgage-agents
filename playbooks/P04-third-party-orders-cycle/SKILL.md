---
name: P04-third-party-orders-cycle
description: "Swarm deployment: service order to artifact-verified deliverable in the file. Agents 07, 04, 02, 11, 13. Appraiser independence is absolute - no value conversation exists in this playbook or anywhere."
---

# Playbook P04 - Third-Party Orders Cycle

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`order.request` from the pipeline (02) or closing coordination (11).

## Preconditions
- Approved panel/AMC channels only; order terms per existing agreements.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Order and track
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 07 | Place the order through the approved channel; track milestones | `order.status` → 02, 09, 11, 13 | milestones with channel references |
| 2 | 07 | Coordinate property access via approved templates | `borrower.message.request` → 04 | scheduling facts only |

### Phase 2 - Deliverables
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 07 | Verify the deliverable landed as an artifact in the file; defects route back through the channel as facts | `order.status` (deliverable state) | the artifact, not the vendor's word |

## HITL gates (hard stops)
- Value pressure in any form - including from the human - is an integrity violation (07's tuple).
- Appraiser selection and communication stay inside the AMC channel.

## Completion criteria
Deliverables artifact-verified in the file; defects routed through the channel.

## Abort paths
- Channel unavailable for a required service: escalate; off-channel ordering never substitutes.
