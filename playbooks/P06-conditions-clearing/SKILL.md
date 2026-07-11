---
name: P06-conditions-clearing
description: "Swarm deployment: issued conditions to evidence-complete clearing packages for underwriter decisions. Agents 09, 05, 06, 07, 08, 04, 13. Evidence-complete and cleared are different states - only the underwriter moves a condition to cleared."
---

# Playbook P06 - Conditions Clearing

**Swarm:** DispatcherAgents Mortgage Swarm (Lending)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
Underwriting conditions issued on a file (human event recorded via 13); 09 opens tracking.

## Preconditions
- Conditions tracked verbatim as issued; ambiguous text goes back to the issuer before any evidence run.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Evidence per condition (parallel)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 09 | Derive each condition's evidence checklist from its text; orchestrate | `doc.request` → 05 / `verify.order` → 06 | evidence runs opened per condition |
| 2 | 09 | Attach worksheet and deliverable evidence where conditions reference them | (from `calc.worksheet`, `order.status`) | artifacts attached per condition |
| 3 | 09 | Borrower-facing condition requests on approved templates | `borrower.message.request` → 04 | requests carry condition text verbatim |

### Phase 2 - Packages
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 09 | Assemble per-condition clearing packages; deliver to the underwriter | `conditions.package` → human, 13 | every artifact attached; gaps named |
| 5 | 09 | Report state transitions; cleared comes only from the human's act | `condition.status` → 02, 13 | state history preserved, reissues never merged |

## HITL gates (hard stops)
- The swarm never clears, waives, interprets, or modifies a condition.
- Evidence-complete is never reported as cleared - conflation is the named failure.

## Completion criteria
Every open condition evidence-complete with its package delivered, or its gap named; cleared states recorded from human acts only.

## Abort paths
- Condition text ambiguous: back to the issuer; no evidence run on a guessed intent.
