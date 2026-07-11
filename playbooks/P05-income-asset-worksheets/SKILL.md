---
name: P05-income-asset-worksheets
description: "Swarm deployment: verified documents to sourced calculation worksheets for the underwriter. Agents 08, 05, 06, 13. The worksheet computes; the underwriter concludes - and discretionary method choices are theirs."
---

# Playbook P05 - Income & Asset Worksheets

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
Sufficient inventoried inputs land for a worksheet, or 09 requests one for a condition.

## Preconditions
- Ratified method tables are current; inputs are inventoried (not defective) documents and verbatim verification facts.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Compute
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 08 | Assemble worksheets per the ratified method; every line cites source + method rule | `calc.worksheet` → 09, 13 | sourced arithmetic, no conclusions |
| 2 | 08 | Request missing inputs; blocked lines stay blocked, never estimated | `doc.request` → 05 | gaps named per line |

### Phase 2 - Deltas
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 08 | Recalculations name their deltas against prior worksheets explicitly | (delta section on the worksheet) | threshold flips NAMED, never silent |

## HITL gates (hard stops)
- Method discretion (declining income, variable hours) is flagged to the underwriter, never exercised.
- Adjusting inputs toward a target figure is the named integrity violation.

## Completion criteria
Worksheets on the file with full sourcing; deltas named; discretion flags raised.

## Abort paths
- Method table gap for the income type: no arithmetic; the gap escalates for ratification.
