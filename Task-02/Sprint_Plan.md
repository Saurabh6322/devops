# Sprint Plan (3 Sprints) — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🏃 Sprint Overview
The development and DevOps operationalization of the portal is executed across three focused 2-week iterations:

```
+-----------------------------------------------------------------------------------------------+
| SPRINT 1: Foundation & MVP Baseline        Tasks 01 to 06       Application Core + Git Flow   |
+-----------------------------------------------------------------------------------------------+
| SPRINT 2: CI/CD & Automated Quality Gates  Tasks 07 to 10       Jenkins + Selenium + Tests    |
+-----------------------------------------------------------------------------------------------+
| SPRINT 3: Containerization & Ansible IaC   Tasks 11 to 15       Docker + Ansible + Release    |
+-----------------------------------------------------------------------------------------------+
```

---

### Sprint 1: Architecture, Core MVP & Git Branching
- **Duration:** Days 1 to 7
- **Sprint Goal:** Establish application architecture, build Spring Boot domain model, REST endpoints, web dashboard, and GitFlow version control baseline.
- **Tasks Included:**
  - Task 01: Problem Definition & 15-Task Scope Freeze
  - Task 02: Agile User Stories, Product Backlog & DevOps Plan
  - Task 03: Architecture Diagram, SRS Summary & REST API List
  - Task 04: GitHub Repository Init, README, .gitignore & Branch Policies
  - Task 05: Feature Branch Development (`feature/document-intake`) & PR Merge
  - Task 06: Complete 5 MVP Features, Resolve Merge Conflict & Tag `v1.0`
- **Deliverables:** Working local web app on port 8085, seeded records, Git release tag `v1.0`.

---

### Sprint 2: Jenkins CI, Pipeline as Code & Automated Testing
- **Duration:** Days 8 to 14
- **Sprint Goal:** Set up Jenkins automation server, author multi-stage Jenkinsfile, build Selenium/JUnit automated test suite, and configure quality gates.
- **Tasks Included:**
  - Task 07: Jenkins Installation, JDK/Maven Tool Config & Freestyle CI Job
  - Task 08: Declarative `Jenkinsfile` Pipeline with Parameterized Deployment
  - Task 09: Automated Test Suite covering 5 Critical User Journeys with Failure Screenshots
  - Task 10: Jenkins Quality Gate Enforcement, Defect Injection, Pipeline Abort & Fix Rerun
- **Deliverables:** Automated CI pipeline, published Surefire/JUnit reports, defect recovery proof.

---

### Sprint 3: Containerization, Continuous Delivery & Ansible IaC
- **Duration:** Days 15 to 21
- **Sprint Goal:** Package the application into production-grade Docker containers, configure continuous delivery, and automate server provisioning via Ansible.
- **Tasks Included:**
  - Task 11: Multi-Stage Alpine JRE Dockerfile, Container Lifecycle & Port Mapping
  - Task 12: Jenkins-Docker CD Pipeline with Automated Versioned Image Tagging
  - Task 13: Ansible Inventory & YAML Playbook for Target Node Configuration
  - Task 14: Clean Target Provisioning, Idempotency Verification (`changed=0`), Health Checks & Rollback
  - Task 15: Final Technical Report, Viva Presentation Guide & Master PDF compilation
- **Deliverables:** Running Docker container, idempotent Ansible playbook, viva presentation deck.
