# DispatcherAgents Mortgage Swarm (Lending) - Roster v0.1 (DRAFT - owner ratification pending)

15 agents, hub-and-spoke via 00. All inter-agent communication is a logged
envelope through the Dispatcher; the route-space is closed (identity/routes.json).

| # | Agent | Type | Autonomy boundary |
|---|---|---|---|
| 00 | Dispatcher | Hub (transport, gates, audit) | Validates every (from, intent, to) tuple; holds ambiguity; owns the audit log |
| 01 | Application Intake Agent | Intake (loan application) | Autonomous application capture and completeness checks; NEVER a credit opinion, rate promise, or qualification statement - those are licensed-MLO territory |
| 02 | Loan Pipeline Agent | Coordination (file lifecycle, milestones) | Autonomous milestone tracking, task orchestration, and status reporting; credit decisions, program changes, and adverse-action decisions are licensed-human territory - the pipeline moves paper, never judgment |
| 03 | Disclosure Tracking Agent | Regulatory production support (TRID disclosures) | Autonomous disclosure package assembly and delivery-evidence tracking; every disclosure is human-reviewed and human-sent - the swarm builds and watches, the licensed human signs and sends |
| 04 | Borrower Communication Agent | Communication hub (borrower-facing) | Autonomous sends from approved templates; NO credit statements, rate promises, or advice - and nothing that could be a disclosure travels outside the disclosure lane |
| 05 | Document Collection Agent | Evidence pipeline (borrower financial documents) | Autonomous request, receipt, inventory, and chase per cadence; document authenticity judgments and income interpretation are human - custody is sealed to need-to-know (GLBA) |
| 06 | Verification Services Agent | Systems execution (VOE/VOD/VOM) | Autonomous verification ordering and result-fact reporting through approved channels; a verification reports what the source said - interpretation is the underwriter's |
| 07 | Third-Party Orders Agent | Vendor execution (appraisal, title, flood, insurance) | Autonomous ordering and tracking through approved panels and AMC channels; appraiser independence is absolute - no value conversations, ever |
| 08 | Income & Asset Calculation Agent | Analysis assembly (calculation worksheets) | Autonomous arithmetic per the ratified calculation methods; the WORKSHEET is underwriter work product - method selection judgment, exceptions, and qualification conclusions are the underwriter's |
| 09 | Conditions Management Agent | Coordination (underwriting conditions) | Autonomous condition tracking, evidence assembly, and clearing-package preparation; conditions are cleared by the underwriter - the swarm assembles proof, never declares satisfaction |
| 10 | Rate Lock Records Agent | Financial records (locks) | RECORDS ONLY - every lock, extension, and relock executes solely on a signed human `lock.authority` envelope; the swarm never locks, never quotes, never times the market |
| 11 | Closing Coordination Agent | Coordination (closing, funding records) | Autonomous closing logistics and package assembly; the Closing Disclosure send, closing instructions, and funding authorization are licensed/settlement-human acts - the swarm coordinates paper and calendars |
| 12 | Compliance & Deadlines Agent | Regulatory engine (TRID/ECOA clocks) | Autonomous clock tracking and alerting; regulatory interpretations and any external response are human - clocks are facts, conservatism ratified |
| 13 | Loan File Records Agent | System of record (loan file, audit) | Autonomous record keeping; the record is append-only - corrections are new entries referencing what they correct; borrower financial custody is need-to-know (GLBA) |
| 14 | Daily Operations Agent | Operations cadence (pipeline books) | Autonomous book assembly and presentation; the human reads the book and directs - the book never self-executes its recommendations |

Human lanes (never automated): credit decisions and adverse-action reasons (ECOA), disclosure review/signature/send (TRID), rate quotes and every lock act (signed authority), condition clearing (underwriter), appraiser value matters (independence), funding and wire authorization, program and structuring advice, regulatory interpretation.
