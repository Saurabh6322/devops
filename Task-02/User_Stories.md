# Agile User Stories & Acceptance Criteria — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

### User Story 1 (US-01): Real-Time Verification Registry & KPIs
> **As an** Underwriting Officer,  
> **I want to** view a real-time dashboard displaying key verification metrics and document listings,  
> **So that** I can instantly understand processing backlogs and triage high-priority claims.

**Acceptance Criteria:**
- Dashboard loads within 1.5 seconds displaying Total Documents, Verified Count, Under Review Count, and Flagged Fraud Count.
- System displays a tabular registry showing Document ID, Policy Number, Claimant Name, Category, Risk Score, and Status.
- Each document displays a visual risk bar (Green $<30\%$, Yellow $30-69\%$, Red $\ge 70\%$).

---

### User Story 2 (US-02): High-Risk Fraud Alert Trigger
> **As a** Special Investigation Unit (SIU) Officer,  
> **I want to** be automatically alerted when an ingested document has a fraud risk score $\ge 70\%$,  
> **So that** I can intercept forged bills and fraudulent payouts before approval.

**Acceptance Criteria:**
- The system must display a conspicuous red warning banner at the top of the portal when high-risk documents are present.
- Clicking the alert banner filters the registry to display only flagged fraudulent records.
- High-risk records must automatically receive the status `FLAGGED_FRAUD` with default diagnostic notes.

---

### User Story 3 (US-03): Digital Document Intake & Registration
> **As a** Policyholder or Intake Clerk,  
> **I want to** submit new insurance document details via a web modal,  
> **So that** the document enters the verification pipeline without requiring physical branch visits.

**Acceptance Criteria:**
- Modal form validates mandatory fields: Policy Number, Claimant Name, Category, and Claim Amount.
- System generates a formatted unique Document ID (e.g. `DOC-2026-XXXX`).
- Persists record into H2 database and returns HTTP 201 Created with updated UI registry.

---

### User Story 4 (US-04): Search & Multi-Criteria Filtering
> **As an** Underwriter,  
> **I want to** search documents by policy number or claimant name and filter by status,  
> **So that** I can locate specific customer claim submissions immediately.

**Acceptance Criteria:**
- Search bar provides instantaneous client-side/API filtering on keystroke input.
- Status dropdown allows filtering by `ALL`, `SUBMITTED`, `UNDER_REVIEW`, `VERIFIED`, `FLAGGED_FRAUD`, `REJECTED`.
- Zero-match state displays a friendly helper message.

---

### User Story 5 (US-05): Underwriter Status Drill-Down & Audit Remarks
> **As an** Underwriting Officer,  
> **I want to** inspect detailed metadata, confidence scores, and update the verification status with notes,  
> **So that** an immutable audit record is maintained for insurance regulatory compliance.

**Acceptance Criteria:**
- Inspection modal displays full document metadata, claim amount, submission timestamp, and current status.
- Underwriter can change status to `UNDER_REVIEW`, `VERIFIED`, `FLAGGED_FRAUD`, or `REJECTED`.
- Remarks field allows saving custom audit notes with underwriter identification.

---

### User Story 6 (US-06): Automated OCR Simulation & Batch Scanning
> **As a** QA or Operations Lead,  
> **I want to** trigger a simulated batch OCR verification scan across all documents,  
> **So that** I can demonstrate automated risk re-evaluation and pipeline reactivity during testing.

**Acceptance Criteria:**
- Clicking "⚡ Run OCR Batch Scan" sends a `POST /api/simulate` request.
- The system recalculates risk scores, updates confidence percentages, and adjusts status flags dynamically.
- The UI triggers an immediate refresh reflecting modified KPI numbers.

