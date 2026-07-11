# build config: mortgage-agents
ROOT = "/home/claude/mortgage-agents"
REPO = "mortgage-agents"
BRAND = "DispatcherAgents Mortgage Swarm (Lending)"
SWARM_SHORT = "Mortgage"
DOMAIN = "Lending"
NOUN = "loan"
VERTICAL = "mortgage-loan-agent"
AUTH_INTENT = "lock.authority"
PINGPONG = "(e.g., 02\u219409 condition ping-pong on a borderline evidence state)"
ESCALATIONS = "`escalation.licensed_line` / `escalation.wire_fraud`"
INSPECTION_REF = "09's evidence-vs-cleared discipline"
DATA = "mortgage_data.py"
TUPLES = "mortgage_tuples.py"
PLAYBOOKS = "mortgage_playbooks.py"
ENVELOPE_AGENT = "02-loan-pipeline"
IDENTITY_MD = "IDENTITY-mortgage-loan-agent.md"
LAST_AGENT = "14-daily-operations"
LIC_NOUN = "mortgage loan-agent"
CLASSES = {"P01": 2, "P02": 1, "P03": 2, "P04": 2, "P05": 2,
           "P06": 2, "P07": 1, "P08": 1, "P09": 2, "P10": 2}
PRIORITY_DOCTRINE = ("JIT run-priority per core doctrine: class 1 = statutory/commitment-critical "
 "(TRID disclosure clocks, lock expirations, closing/funding windows), class 2 = "
 "active file lifecycle and books. Pacing over braking: the siding scheduler "
 "paces class contention; nothing slam-stops.")
HUMAN_LANES = ("Human lanes (never automated): credit decisions and adverse-action reasons "
 "(ECOA), disclosure review/signature/send (TRID), rate quotes and every lock act "
 "(signed authority), condition clearing (underwriter), appraiser value matters "
 "(independence), funding and wire authorization, program and structuring advice, "
 "regulatory interpretation.")
DESC = '''DESC = {
 "00": "Mortgage swarm dispatcher. The hub: validates every (from, intent, to) tuple against the closed track, holds ambiguity in clarification, and owns the audit log. Nothing moves without it.",
 "01": "Application intake. Use when loan applications need complete, source-attributed capture with exact timestamps - no credit opinions, no rate quotes, HMDA data exactly as provided or declined.",
 "02": "Loan pipeline. Use when files need milestone tracking, evidence orchestration, condition-state visibility, and adverse-action SUPPORT packages - credit decisions and their reasons are licensed-human territory.",
 "03": "Disclosure tracking. Use when TRID disclosure packages need assembly with per-figure sources and delivery-evidence trails - the licensed human reviews, signs, and sends, every time.",
 "04": "Borrower communication. Use when borrowers need templated process messages or replies need content-routing - no credit statements, no rate figures outside the disclosure lane.",
 "05": "Document collection. Use when borrower financial documents need checklist requests, inventory, cadenced chase, and anomaly FACTS - authenticity judgments are human, LOEs are borrower-authored (GLBA custody).",
 "06": "Verification services. Use when employment, deposit, and housing-history verifications need approved-channel ordering and verbatim result facts - interpretation is the underwriter's.",
 "07": "Third-party orders. Use when appraisals, title, flood, insurance, and payoffs need channel ordering with artifact-verified deliverables - appraiser independence is absolute, no value conversation exists.",
 "08": "Income and asset calculation. Use when verified inputs need worksheets per ratified methods with per-line sourcing and NAMED deltas - discretion flags to the underwriter, conclusions never computed.",
 "09": "Conditions management. Use when underwriting conditions need verbatim tracking, evidence orchestration, and clearing packages - evidence-complete and cleared are different states; only the underwriter clears.",
 "10": "Rate lock records. Use when locks, extensions, and relocks need execution on SIGNED authority with expiry watched at lead-time - the swarm never locks, quotes, or times the market.",
 "11": "Closing coordination. Use when closings need review-ready fee-reconciled packages, waiting-period-safe scheduling, and funding-event records - CD sends and funding authorization are human acts.",
 "12": "Compliance and deadlines. Use when TRID, ECOA, and lock clocks need instantiation, conservative math, lead-time alerts, and waiting-period holds - clocks are facts.",
 "13": "Loan file records. Use when interactions need the append-only loan file, verbatim lookups, and chronologies - borrower financial custody is need-to-know (GLBA).",
 "14": "Daily operations. Use for the pipeline morning book, end-of-day books with missed-item sweep, and clock reconciliation - books inform, the human directs.",
}'''
