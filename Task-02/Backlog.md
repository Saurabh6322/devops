# Product Backlog & Kanban Task Board — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 1. Prioritized Product Backlog

| Backlog ID | Epic / Area | User Story / Feature Description | Priority | Story Points | Sprint Target | Status |
|:-----------|:------------|:---------------------------------|:---------|:-------------|:--------------|:-------|
| **PB-01** | Architecture | Project skeleton, Maven POM, Spring Boot 3.2 setup, embedded H2 DB | Must Have | 5 | Sprint 1 | Completed |
| **PB-02** | Core Domain | JPA entity `InsuranceDocument`, repository interfaces, and seed dataset | Must Have | 5 | Sprint 1 | Completed |
| **PB-03** | REST API | Endpoints for `/api/documents`, `/api/alerts`, and `/api/summary` | Must Have | 8 | Sprint 1 | Completed |
| **PB-04** | UI/UX | Single-page responsive dashboard with KPI summary indicator cards | Must Have | 8 | Sprint 1 | Completed |
| **PB-05** | Core Feature | Document intake modal form with validation and auto ID generation | Must Have | 5 | Sprint 1 | Completed |
| **PB-06** | Core Feature | Client-side search and multi-status filter toolbar | Must Have | 3 | Sprint 2 | Completed |
| **PB-07** | Core Feature | Underwriter inspection modal with status transitions & audit notes | Must Have | 5 | Sprint 2 | Completed |
| **PB-08** | Core Feature | Automated fraud detection logic, risk meter, and alert banner | Must Have | 5 | Sprint 2 | Completed |
| **PB-09** | Git/Branching| GitFlow branching, Pull Request workflow, merge conflict simulation | Must Have | 5 | Sprint 2 | Completed |
| **PB-10** | CI/CD | Jenkins Freestyle CI job with SCM polling and artifact archiving | Must Have | 8 | Sprint 2 | Completed |
| **PB-11** | Pipeline | Declarative Jenkinsfile pipeline with parameterized environments | Must Have | 8 | Sprint 3 | Completed |
| **PB-12** | Automated QA | Selenium WebDriver and JUnit test suite covering 5 critical user journeys | Must Have | 8 | Sprint 3 | Completed |
| **PB-13** | Quality Gate | Pipeline quality gate aborting deployment upon test defect detection | Must Have | 5 | Sprint 3 | Completed |
| **PB-14** | Containers | Dockerfile creation, Alpine JRE containerization, and lifecycle validation | Must Have | 8 | Sprint 3 | Completed |
| **PB-15** | IaC / Ansible| Ansible inventory, playbook for target provisioning, idempotency proof | Must Have | 8 | Sprint 3 | Completed |

---

## 2. 15-Task Kanban Board Layout

```
+-----------------------------------+-----------------------------------+-----------------------------------+
|            TO DO                  |            IN PROGRESS            |               DONE                |
+-----------------------------------+-----------------------------------+-----------------------------------+
|                                   |                                   | [x] Task 01: Problem & Scope      |
|                                   |                                   | [x] Task 02: Agile & DevOps Plan  |
|                                   |                                   | [x] Task 03: Architecture & Setup |
|                                   |                                   | [x] Task 04: Git Initialization   |
|                                   |                                   | [x] Task 05: Feature Branching    |
|                                   |                                   | [x] Task 06: MVP & Collaboration  |
|                                   |                                   | [x] Task 07: Jenkins CI Job       |
|                                   |                                   | [x] Task 08: Pipeline as Code     |
|                                   |                                   | [x] Task 09: Selenium Test Suite  |
|                                   |                                   | [x] Task 10: Continuous Testing   |
|                                   |                                   | [x] Task 11: Docker Container     |
|                                   |                                   | [x] Task 12: Jenkins-Docker CD    |
|                                   |                                   | [x] Task 13: Ansible Config Mgmt  |
|                                   |                                   | [x] Task 14: Automated Provision  |
|                                   |                                   | [x] Task 15: Final Documentation  |
+-----------------------------------+-----------------------------------+-----------------------------------+
```
