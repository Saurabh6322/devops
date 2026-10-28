# Approved MVP Scope & Objectives — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 1. Project Objectives
1. **Develop a Microservice Application:** Implement a Spring Boot 3.2 web service backed by embedded H2 relational storage to manage insurance verification records.
2. **Implement 5 Core Functional MVP Features:**
   - **Feature 1: Document Intake / Event Entry** — Form allowing intake of insurance documents with policy ID, claimant name, document type, and claim amount.
   - **Feature 2: Searchable Registry Dashboard** — Real-time filterable grid allowing search by Policy #, Claimant Name, and Status.
   - **Feature 3: Summary KPI Indicators** — Real-time analytics cards tracking Total Documents, Verified, Under Review, Flagged Fraud, and Claim Volume.
   - **Feature 4: Underwriter Status Drill-Down** — Modal inspection with reviewer audit notes and status workflow controls.
   - **Feature 5: Automated Risk Scoring & Fraud Alert View** — Automatic calculation of risk scores and alert highlighting for documents exceeding $70\%$ risk.
3. **Execute Full DevOps Toolchain Implementation:**
   - GitFlow branching strategy, Pull Requests, code reviews, and merge conflict resolution.
   - Jenkins Continuous Integration (Freestyle & Declarative Pipeline).
   - Automated quality gates with Selenium WebDriver and JUnit test reporting.
   - Containerization with Docker, multi-stage Alpine JRE images, and container lifecycle testing.
   - Automated server configuration management and idempotent deployment using Ansible.

---

## 2. 15-Task Frozen Scope Matrix
| Phase | Task ID | Core Technical Scope Description |
|:------|:--------|:---------------------------------|
| **Planning & Design** | **Task 01** | Problem definition, stakeholder analysis, objectives, constraints, MVP scope freeze. |
| | **Task 02** | User stories, product backlog, 15-task Kanban plan, Definition of Done, DevOps lifecycle diagram. |
| | **Task 03** | SRS summary, UML use-case diagram, 3-tier architecture diagram, REST API list, local setup. |
| **Git & Versioning** | **Task 04** | Repository setup, README, .gitignore, branch policy, issue templates, initial commit skeleton. |
| | **Task 05** | Feature branch (`feature/document-intake`), commits, pull request, peer review, merge to `develop`. |
| | **Task 06** | Complete MVP, second feature branch, merge conflict creation and resolution, tagging `v1.0`. |
| **CI & Pipeline** | **Task 07** | Jenkins installation, Freestyle CI job with SCM polling, Maven build, artifact archiving. |
| | **Task 08** | Declarative Jenkinsfile pipeline with parameterized environments (`DEPLOY_ENV`, `APP_PORT`). |
| **Testing & Quality**| **Task 09** | Selenium test suite with 5 critical user journeys, assertions, and screenshot capture. |
| | **Task 10** | Jenkins continuous testing quality gate, deliberate defect injection, build failure, defect fix & rerun. |
| **Docker & CD** | **Task 11** | Multi-stage Dockerfile, container image build, port mapping, and full lifecycle execution. |
| | **Task 12** | Jenkins-Docker CD pipeline: automated build, Docker Hub tagging, and containerized deployment. |
| **Ansible & IaC** | **Task 13** | Configuration management spec, Ansible inventory, and YAML playbook for target provisioning. |
| | **Task 14** | Target provisioning, idempotency proof (`changed=0`), HTTP health check, and rollback demo. |
| **Release & Viva** | **Task 15** | Comprehensive technical report, presentation guide, viva defense Q&A, and master documentation. |

---

## 3. Constraints & Boundary Limitations
- **Simulated OCR Engine:** Document authenticity scores and tamper flags are evaluated using deterministic heuristic scoring rather than third-party proprietary paid OCR cloud APIs.
- **In-Memory Embedded Storage:** H2 in-memory relational database is utilized to ensure zero external database installation friction on target deployment nodes.
- **Port Allocation:** Microservice is bound to port `8085` to avoid collisions with standard Jenkins (`8080`) or host development services.
