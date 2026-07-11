# mortgage-agents - mortgage lending vertical for the DispatcherAgents runtime

An **identity side-load**: everything vertical-specific for a 15-agent
mortgage loan-pipeline swarm, loadable into the content-neutral
[dispatcher-agents](https://github.com/QuietFireAI/dispatcher-agents) runtime.
The runtime never contains vertical text; this repo never contains transport
code. That split is the architecture.

**Status: v0.1 DRAFT - owner ratification pending. Not runtime-hardened. No
licensed legal, regulatory (TRID/ECOA/RESPA), or lending-compliance review
has been performed.**

## What this is for

Operations support for a loan officer, processor, or lending shop:
application capture with exact clock timestamps, milestone orchestration,
TRID disclosure packages for human review and send, document and verification
pipelines with anomaly facts, channel-only third-party orders, sourced
calculation worksheets, condition clearing packages, signed-authority lock
records, waiting-period-safe closing coordination, the statutory clock
engine, an append-only loan file, and the daily books.

What it never does - the five absolute lines (identity/IDENTITY-mortgage-loan-agent.md):

1. No credit voice, ever - qualification, rates, and adverse-action reasons
   are licensed-human territory (ECOA).
2. Disclosures are human acts - assembled by the swarm, sent by the licensed
   human, always (TRID).
3. No unsigned commitments - locks on signed authority only; funding and
   wires are never swarm acts.
4. Appraiser independence is absolute - no value conversation exists.
5. Evidence-complete is not cleared - only the underwriter clears conditions;
   borrower financial custody is need-to-know (GLBA).

## Layout

| Path | What it is |
|---|---|
| `identity/routes.json` | The closed track: 31 (intent, senders, receivers) routes - single source of truth |
| `identity/priority.json` | JIT playbook priority classes (DRAFT) |
| `identity/IDENTITY-mortgage-loan-agent.md` | The identity declaration |
| `00-dispatcher/ ... 14-daily-operations/` | 15 agent SKILL.md + DECISIONS.md (tuple layer) |
| `playbooks/P01 ... P10` | Deployment playbooks: application-to-file-open through EOD books |
| `SWARM.md` | Framework manifest + swarm-level tuples |
| `MANNERS.md` | Conduct constants, hash-registered at boot attestation |
| `TUPLE_INDEX.md` | Generated drill-down: tuple → agent → playbooks |
| `generate_skills.py` / `gen_meta.py` / `gen_playbooks.py` / `gen_tuple_index.py` | Generators - data tables are the spec; files are build artifacts |
| `verify_swarm.py` | Enforcement: tuple legality, edge completeness, regression - exit 0 = clean |

## Verify

```bash
python3 verify_swarm.py    # 0 failures, 0 warnings expected
```

## Load into the runtime

```bash
git clone https://github.com/QuietFireAI/dispatcher-agents.git
git clone https://github.com/QuietFireAI/mortgage-agents.git
cd dispatcher-agents && pip install -e ".[pillars,crypto,dev]"
```

```python
from dispatcher.loader import load_identity
ident = load_identity("/path/to/mortgage-agents")
```

The loader is fail-closed: no routes.json, no track, no load. It audits the
priority table's status on every load - never silently.

## Sibling identities

- [listing-agents](https://github.com/QuietFireAI/listing-agents) - real-estate listing vertical (ratified)
- [claim-agents](https://github.com/QuietFireAI/claim-agents) - insurance claims vertical (ratified)
- [reservation-agents](https://github.com/QuietFireAI/reservation-agents) - park/resort reservations vertical (ratified)
- medbilling-agents, property-mgmt-agents, practice-agents - this drop's siblings

## License

Proprietary - see LICENSE (placeholder pending legal review).
