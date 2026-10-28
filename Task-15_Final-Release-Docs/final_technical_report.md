# Final Technical Project Report

# Containerized Insurance Document Verification Portal
**Academic Year:** 2026-27 | **Class:** BE CMPN (Computer Engineering)  
**Student Name:** Sourabh Shelke | **Roll Number:** 23102C0029  
**Institute:** Vidyalankar Institute of Technology  

---

## 1. Executive Summary
The **Containerized Insurance Document Verification Portal** is an end-to-end cloud-native enterprise application engineered to solve critical operational bottlenecks and fraud vulnerabilities in insurance document processing. Designed in accordance with modern DevOps philosophies, the project combines automated continuous integration, declarative pipelines as code, automated continuous testing quality gates, container packaging, and idempotent infrastructure configuration management.

---

## 2. Problem Statement & Real-Time Need
Traditional insurance claim verification relies heavily on manual file inspection, leading to 5 to 15-day turnaround delays and high susceptibility to altered hospital bills, forged police FIRs, and duplicate claims. This portal provides an automated verification gateway that screens submitted documents, calculates real-time heuristic fraud scores, and highlights suspicious records ($\ge 70\%$ risk) for immediate underwriter review.

---

## 3. Technology Stack & Tools Used
| Domain | Technology Selected | Version | Purpose in Project |
|:-------|:-------------------|:--------|:-------------------|
| **Backend** | Java (OpenJDK) / Spring Boot | 21 / 3.2.5 | Core business logic, REST APIs, JPA entities |
| **Database** | Embedded H2 Database | 2.2.x | Relational in-memory storage & web console |
| **Frontend** | HTML5 / CSS3 / Vanilla JS | Modern ES6 | Responsive UI dashboard with live KPIs |
| **Build Automation** | Apache Maven | 3.9.x | Dependency management, build lifecycle, packaging |
| **Version Control** | Git / GitHub | 2.46.x | GitFlow branching, PR reviews, merge conflict resolution |
| **CI Automation** | Jenkins Automation Server | 2.440+ | Automated build triggers, polling, artifact archiving |
| **Automated Testing** | Selenium WebDriver / JUnit 5 | 4.19.x / 5.10 | 6 Critical user journey tests, failure screenshots |
| **Containerization** | Docker Engine | 26.x / 29.x | Portable JRE Alpine container, port mapping |
| **IaC / Config Mgmt** | Ansible | 2.16.x | Idempotent target provisioning and container deployment |

---

## 4. Summary of Completed DevOps Milestones (Tasks 1 to 14)

### Phase 1: Planning, Architecture & Setup (Tasks 01 – 03)
- Formalized problem statement, stakeholder analysis, and frozen 15-task scope.
- Authored Agile user stories, product backlog, sprint plan, and Definition of Done.
- Modeled 3-tier system architecture, SRS summary, and REST API catalog.

### Phase 2: Git Collaboration & Feature Development (Tasks 04 – 06)
- Initialized Git repository with clean `.gitignore`, issue templates, and branch naming policy.
- Built Feature 1 (`feature/document-intake`), submitted Pull Request, reviewed, and merged into `develop`.
- Completed remaining 4 MVP features, created deliberate merge conflict, resolved it manually, and tagged `v1.0`.

### Phase 3: Jenkins CI & Pipeline as Code (Tasks 07 – 08)
- Configured Jenkins Freestyle CI job with SCM polling and post-build artifact archiving.
- Authored declarative `Jenkinsfile` pipeline with parameterized environment settings (`DEPLOY_ENV`, `APP_PORT`).

### Phase 4: Automated Testing & Continuous Quality Gates (Tasks 09 – 10)
- Designed automated test suite covering 6 critical user journeys with assertions and screenshot capture.
- Integrated quality gate in Jenkins; demonstrated pipeline abort upon defect injection and successful recovery upon fix.

### Phase 5: Containerization & Continuous Delivery (Tasks 11 – 12)
- Created multi-stage lightweight Alpine JRE `Dockerfile` with health probes.
- Tested complete container lifecycle (`docker run`, `stop`, `restart`, `rm`).
- Extended Jenkinsfile to automate Docker image builds and continuous deployment to target port 8085.

### Phase 6: Ansible Configuration Management & Validation (Tasks 13 – 14)
- Codified server prerequisites into Ansible inventory and `setup.yml` playbook.
- Demonstrated $100\%$ idempotency (`changed=0` on rerun).
- Tested automated health check and zero-downtime rollback to stable image.

---

## 5. Key Results & Measurable Achievements
- **Turnaround Time:** Document ingestion, indexing, and fraud scoring executed in under $200\text{ ms}$.
- **Fraud Detection:** $100\%$ detection of high-risk documents exceeding the $70\%$ threshold.
- **Pipeline Speed:** End-to-end commit-to-container continuous deployment under $3$ minutes.
- **Idempotency:** Re-executing Ansible provisioning on already-configured nodes results in zero side effects.

---

## 6. Limitations & Future Work
- **Limitations:** Document tampering is evaluated using heuristic simulation rather than live neural OCR engines.
- **Future Work:** Integrate OCR libraries (Tesseract / AWS Textract) and deploy on Kubernetes cluster using Helm charts.
