# Software Requirements Specification (SRS) Summary

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 1. Purpose & Scope
This document specifies the software requirements for the **Containerized Insurance Document Verification Portal MVP**. The system serves as an automated verification gateway and underwriter dashboard for processing, validating, and triaging customer insurance claim documents.

---

## 2. Functional Requirements (FR)

### FR-01: Document Registration & Intake
- The system shall provide an intake API endpoint (`POST /api/documents`) and interactive modal for uploading document metadata.
- System shall auto-generate unique sequential Document IDs (e.g. `DOC-2026-XXXX`).
- System shall require Policy Number, Claimant Name, Document Type, and Claim Amount.

### FR-02: Real-Time Searchable Registry
- The system shall display all ingested records in an interactive dashboard table.
- System shall support instant search across Document ID, Policy Number, Claimant Name, and Document Category.
- System shall support filtering by verification status (`ALL`, `SUBMITTED`, `UNDER_REVIEW`, `VERIFIED`, `FLAGGED_FRAUD`, `REJECTED`).

### FR-03: Summary KPI Indicators
- The portal shall compute and display live summary metrics:
  - Total Documents Ingested
  - Total Verified Clean Records
  - Total Under Review Records
  - Total Flagged Fraud Records
  - Average Fraud Risk Score (%)
  - Aggregated Claim Amount Volume (₹)

### FR-04: Automated Fraud Detection & Alert Engine
- The system shall evaluate document risk heuristics on a scale of $0$ to $100$.
- Any record with a risk score $\ge 70$ shall automatically be assigned `FLAGGED_FRAUD` status.
- A prominent alert banner shall render on the portal when active fraud suspects are present.

### FR-05: Underwriter Workflow Progression & Audit Notes
- Underwriters shall be able to inspect detailed metadata and authenticity confidence percentages.
- Authorized users shall be able to transition document status and record timestamped reviewer remarks.

### FR-06: Batch OCR Simulation
- The system shall provide a `POST /api/simulate` endpoint to simulate OCR heuristic re-evaluations for demonstration purposes.

---

## 3. Non-Functional Requirements (NFR)

### NFR-01: Performance & Latency
- The web portal dashboard shall load in under $1.5$ seconds on standard broadband.
- REST API response times for read and write queries shall remain under $150\text{ ms}$.

### NFR-02: Portability & Containerization
- The complete application must run self-contained within an Alpine-based Docker container requiring only standard Java JRE runtime.
- Microservice shall avoid port collisions by binding to port `8085`.

### NFR-03: Reliability & Health Telemetry
- The system shall expose a `/api/health` microservice endpoint reporting status, version, and author attribution for container orchestrators and Ansible monitors.

### NFR-04: Maintainability & Testability
- Codebase shall maintain modular separation between Controller, Model, and Repository tiers.
- Automated tests shall cover at least 5 critical user journeys with $100\%$ pass rates.
