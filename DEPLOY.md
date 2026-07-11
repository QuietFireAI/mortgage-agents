# DEPLOY - Mortgage Swarm (Lending) (v0.1, ratified 2026-07-11 - owner sign-off)

The operator runbook: what a deployment site must have, ratify, and verify
before this identity runs live.

## Prerequisites (site property, never repo property)

Systems and credentials for each seam in INTEGRATIONS.md:
- POS / 1003 intake (IN)
- LOS (system of record bridge) (OUT+IN)
- Verification services (VOE/VOD) (OUT+IN)
- AMC (appraisal channel) (OUT+IN)
- Title/flood/insurance vendors (OUT+IN)
- Disclosure delivery platform (OUT+IN)
- E-signature (OUT+IN)

## Config tables to ratify before live mode

Every table below ships as an UNRATIFIED TEMPLATE. The owner edits it to the
site's reality, changes `_status` to a ratified line with date and sign-off,
and only then loads it. A table still marked UNRATIFIED TEMPLATE must fail
closed at load.
- `config/milestone_map.json` - Ratified file milestones and entry criteria
- `config/program_checklists.json` - Document/verification checklists per loan program
- `config/method_tables.json` - Ratified income/asset calculation methods
- `config/business_day_calendar.json` - Ratified calendar for TRID math
- `config/regulatory_table.json` - TRID/ECOA/state periods (conservative on conflict)
- `config/message_templates.json` - Approved borrower templates (no figures outside disclosure lane)
- `config/authority_signers.json` - Humans authorized on lock.authority

## Go-live doctrine: shadow mode first

1. **Dark run**: load the identity, connect read-only inbound seams, leave every
   outbound seam disconnected (queue-only). The swarm builds books and records;
   nothing leaves.
2. **Compare**: the operator runs their existing process in parallel and compares
   the morning/EOD books against reality for the ratified trial period. Every
   discrepancy is a config-table or seam defect to fix - the books are the test.
3. **Ratify tables**: no config table loads in live mode while marked UNRATIFIED
   TEMPLATE. The owner edits, ratifies (status line + date + sign-off), then loads.
4. **Staged outbound**: enable outbound seams one at a time, lowest-risk first
   (record lookups before communications before money-adjacent), each behind its
   human lane exactly as the spec states.
5. **Rollback is config**: disconnecting a seam returns that lane to manual with
   the record intact. Nothing about rollback loses audit history.

## Go-live gates (all must be green)

- [ ] verify_swarm: 0 failures, 0 warnings on the deployed checkout
- [ ] Loader: identity loads with warnings []
- [ ] Every config table ratified (no UNRATIFIED TEMPLATE in live config)
- [ ] Every connected seam passed the INTEGRATIONS.md conformance checklist
- [ ] Shadow-mode book comparison signed off by the owner for the trial period
- [ ] Authority signers registered and signature verification live
- [ ] Human lanes staffed: every human-routed intent has a named owner

## Not in scope of this repo

Adapter code, credentials, vendor agreements, and legal/compliance review of
the deployment are site responsibilities. This identity ships the contract
and the governance; the site ships the connections.
