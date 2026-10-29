# Problem Statement — Containerized Insurance Document Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 1. Introduction
In modern insurance claim adjudication and policy onboarding, document verification remains the single largest operational bottleneck. Annually, insurance providers process millions of customer-submitted documents—including hospital discharge summaries, medical invoices, death/disability certificates, motor surveyor inspection reports, police First Information Reports (FIRs), and government KYC credentials.

Traditional document handling relies on fragmented email threads, manual physical file checks, and disjointed verification portals. This manual approach results in severe processing delays, elevated operational costs, poor customer satisfaction, and susceptibility to sophisticated document tampering and insurance fraud.

---

## 2. Problem
There is currently no unified, lightweight, containerized verification platform available to insurance carriers and third-party administrators (TPAs) that:
- Ingests multi-category claim documents and policy proofs in real time.
- Extracts and indexes key policy parameters (policy number, claimant identity, claimed amount, issuance authority).
- Automatically calculates heuristic authenticity scores and flags suspicious documents (risk score $\ge 70\%$) before manual underwriter review.
- Provides a centralized, searchable registry with role-based workflow state progression (Submitted $\to$ Under Review $\to$ Verified / Flagged Fraud / Rejected).
- Operates reliably within an automated CI/CD pipeline, ensuring automated testing, zero-downtime containerized updates, and repeatable infrastructure provisioning.

---

## 3. Proposed Solution
A **Containerized Insurance Document Verification Portal**—a cloud-native microservice built on Java 21/23, Spring Boot 3.2, and embedded H2 relational storage, backed by a responsive single-page web dashboard. The portal simulates real-time insurance document submission, evaluates risk heuristics and digital tampering indicators, and provides underwriters with instant drill-down and workflow action controls.

The entire system is developed, validated, and operated using a production-grade DevOps lifecycle:
```
Git Version Control ──> Jenkins CI/CD ──> Selenium Automated Testing ──> Docker Containerization ──> Ansible Configuration Management
```

---

## 4. Target Users
| # | Target User Persona | Primary Operational Role & Responsibilities |
|:--|:-------------------|:---------------------------------------------|
| **1** | **Policyholders & Claimants** | Upload policy proofs and claim bills; track real-time verification progress without physical branch visits. |
| **2** | **Verification Officers & Underwriters** | Review queued documents, inspect metadata and authenticity scores, log audit remarks, and update status. |
| **3** | **Claims Fraud Investigators** | Receive high-risk alerts (risk score $\ge 70\%$), cross-reference regional registries, and quarantine fraudulent submissions. |
| **4** | **DevOps & Infrastructure Engineers** | Manage automated CI/CD pipelines, container images, test suites, and target node provisioning. |

---

## 5. Existing Pain Points
1. **Prolonged Turnaround Times (TAT):** Manual document verification takes between 5 to 15 business days per claim, delaying legitimate payouts.
2. **Fraud Vulnerabilities:** Forged hospital bills, inflated workshop repair estimates, and duplicate claims across multiple insurers cost the industry billions annually.
3. **Lack of Audit Transparency:** Claimants and underwriters have no single source of truth regarding the exact stage of document review.
4. **Environment Inconsistencies:** Traditional on-premise verification tools fail when deployed across differing server environments due to missing runtime dependencies.
5. **Slow Deployment Cycles:** Manual updates risk software downtime during peak policy renewal and claim processing periods.

---

## 6. Measurable Success Criteria
| # | Metric / Criteria | Baseline Manual Standard | Target Project Standard |
|:--|:-------------------|:--------------------------|:-------------------------|
| **1** | Automated Intake & Triage | 24–48 hours | $< 2$ seconds per document |
| **2** | Fraud Detection Accuracy | ~60% caught manually | $100\%$ of threshold breaches ($\ge 70\%$) flagged |
| **3** | System Availability & Uptime | 95.0% | $99.9\%$ during testing and evaluation |
| **4** | CI/CD Commit-to-Deploy Time | 1–2 days | $< 3$ minutes via automated pipeline |
| **5** | Automated Test Pass Rate | Variable / Manual | $100\%$ pass across 5 critical user journeys |

