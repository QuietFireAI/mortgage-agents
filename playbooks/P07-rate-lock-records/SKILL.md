---
name: P07-rate-lock-records
description: "Swarm deployment: signed lock authority to recorded lock with expiry watched at lead-time. Agents 10, 12, 02, 04, 13. The swarm never locks - it records signed human acts and watches the clock."
---

# Playbook P07 - Rate Lock Records

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Signed `lock.authority` arrives at 10, or an expiry lead-time alert fires.

## Preconditions
- Authority terms consistent with the file's program of record (10's hold tuple otherwise).
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Record
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 10 | Execute the lock record exactly as authorized, authority envelope_id attached | `lock.record` → 02, 12, 13 | terms verbatim; file state updated |
| 2 | 04 | Lock confirmation on the approved template - terms as authorized, no commentary | `borrower.message.send` | send logged |

### Phase 2 - Watch
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 12 | Expiry clocks armed; lead-time alerts to 10 and 02 | `deadline.alert` | expiry visibility ahead of the date |
| 4 | 10 | Expiry lead-time reached: the fact goes to the human - extension is a signed decision | (escalation with dates) | no auto-extension, ever |

## HITL gates (hard stops)
- No lock, extension, or relock without signed authority - unsigned is an integrity violation.
- No rate quotes or market commentary in any channel.

## Completion criteria
Lock recorded as authorized; expiry watched with lead-time alerts; extensions only as new signed acts.

## Abort paths
- Authority conflicts with the file: hold + re-confirm naming both states.
