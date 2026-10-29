# Stakeholder Analysis — Insurance Document Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 1. Stakeholder Classification Matrix

| Stakeholder Group | Key Responsibilities | Primary Interest & Value Expected | Impact / Influence |
|:------------------|:---------------------|:-----------------------------------|:-------------------|
| **Policyholders & Claimants** | Submit genuine documentation; verify accuracy of policy numbers and claim amounts. | Fast, transparent verification; rapid claim approvals with zero physical paperwork friction. | High Interest / High Impact |
| **Verification Officers & Underwriters** | Validate submitted bills and certificates; approve or escalate claims; record audit logs. | Automated pre-screening, clear risk score indicators, and one-click workflow transitions. | High Interest / High Impact |
| **Special Investigation Unit (SIU) / Fraud Officers** | Intercept and investigate high-risk anomalies (risk score $\ge 70\%$); maintain blacklists. | Instant alert triggers, tamper detection audit trails, and fraud pattern recognition. | High Interest / Medium Impact |
| **Third-Party Administrators (TPAs) & Hospitals** | Issue cashless claims, bills, and surveyor assessment summaries. | Direct integration capability, standardized document categorization, and fast turnaround. | Medium Interest / High Impact |
| **Insurance Regulatory Authority (e.g. IRDAI)** | Establish regulatory guidelines, consumer protection rules, and SLA mandates. | Complete data compliance, immutable verification audit logs, and fraud prevention controls. | High Influence / Medium Interest |
| **DevOps & IT Operations Team** | Build, package, test, containerize, and maintain portal availability and CI/CD pipelines. | High reliability, idempotent server provisioning, container portability, and clean monitoring. | High Influence / High Impact |

---

## 2. Communication & Reporting Plan
- **Real-Time Operational Alerts:** Real-time web dashboard banners alerting investigators of fraudulent submissions.
- **Underwriting Review Audits:** Embedded reviewer notes and immutable timestamp logging for every status progression.
- **DevOps Telemetry:** Jenkins automated email/console build reports and Docker container health probe metrics.

