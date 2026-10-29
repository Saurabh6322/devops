# 🚀 Containerized Insurance Document Verification Portal — Master Checkpoint Tracker
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

> This document tracks completion across all 15 DevOps phases according to the university curriculum.

---

## 📋 TASK 1 — Problem Definition and Scope
**Folder:** `Task-01/`  
**Deliverables:** Problem statement, stakeholder list, objectives, constraints and approved MVP scope.

- [x] **1.1** Study the real-time industry need for automated Insurance Document Verification
- [x] **1.2** Identify target users (Policyholders/Claimants, Verification Officers/Underwriters, Compliance Admins)
- [x] **1.3** Document existing pain points (manual turnaround latency of 5-15 days, fraud vulnerabilities, lack of real-time auditability)
- [x] **1.4** Identify stakeholders (Claimants, Insurance Providers, Third-Party Administrators, Surveyors, IRDAI Regulatory Bodies)
- [x] **1.5** Define project constraints (Open-source toolchains, containerized deployment, 100% simulated IoT/claim metadata)
- [x] **1.6** Establish measurable success criteria (Sub-minute automated verification, 100% fraud flagging for score >= 70, zero-downtime updates)
- [x] **1.7** Freeze 15-task MVP scope covering 5 core features:
  - [x] Document Intake / Event Entry
  - [x] Searchable Verification Registry
  - [x] Summary Indicator Cards
  - [x] Underwriter Status Drill-Down
  - [x] Automated Risk Scoring & Fraud Alert View
- [x] **1.8** Save `Problem_Statement.md`, `Stakeholders.md`, `Scope.md` and compiled PDFs in `Task-01/`

---

## 📋 TASK 2 — Agile Planning and DevOps Workflow
**Folder:** `Task-02/`  
**Deliverables:** Backlog, task board, sprint plan, Definition of Done and DevOps workflow diagram.

- [x] **2.1** Formulate 6 Agile user stories with testable acceptance criteria
- [x] **2.2** Prepare prioritized product backlog across Sprints 1, 2, and 3
- [x] **2.3** Design 15-task Kanban/Scrum board covering entire development and DevOps lifecycle
- [x] **2.4** Define strict Definition of Done (DoD) checklist
- [x] **2.5** Draw end-to-end DevOps lifecycle diagram (Plan → Code → Build → Test → Release → Deploy → Operate → Monitor)
- [x] **2.6** Save `User_Stories.md`, `Backlog.md`, `Sprint_Plan.md`, `Definition_of_Done.md`, `Diagram.md` and PDFs in `Task-02/`

---

## 📋 TASK 3 — Requirements, Architecture and Technology Setup
**Folder:** `Task-03/`  
**Deliverables:** SRS summary, use-case diagram, architecture diagram, data model/API list and working local setup.

- [x] **3.1** Author Software Requirements Specification (SRS) summary covering functional & non-functional requirements
- [x] **3.2** Model UML use-case diagram (Actors: Policyholder, Underwriter, Compliance Auditor)
- [x] **3.3** Design 3-tier containerized system architecture diagram
- [x] **3.4** Finalize technology stack: Java (OpenJDK 21/23), Spring Boot 3.2, Maven, H2 DB, Docker, Jenkins, Ansible
- [x] **3.5** Specify data model schema (`InsuranceDocument` entity)
- [x] **3.6** Document complete REST API list (`/api/documents`, `/api/alerts`, `/api/summary`, `/api/simulate`, `/api/health`)
- [x] **3.7** Setup local runtime environment and verify port bindings
- [x] **3.8** Save `srs_summary.md`, `architecture_diagram.md`, `API_List.md`, `local_setup_guide.md` and PDFs in `Task-03/`

---

## 📋 TASK 4 — Git and GitHub Repository Initialization
**Folder:** `Task-04/`  
**Deliverables:** Repository URL, README, initial commits, issues and branch policy.

- [x] **4.1** Initialize local Git repository with `git init`
- [x] **4.2** Create comprehensive `README.md` with overview, quickstart, and tech stack
- [x] **4.3** Configure comprehensive `.gitignore` for Java/Maven/Docker
- [x] **4.4** Structure directory layout (`src/`, `Task-XX/`, `.github/`)
- [x] **4.5** Create GitHub issue templates for bug reports and feature requests
- [x] **4.6** Formulate branch naming conventions (`main`, `develop`, `feature/*`, `hotfix/*`)
- [x] **4.7** Commit initial application skeleton with meaningful Git commit messages
- [x] **4.8** Save `branch_policy.md`, `url.md`, `git_init_evidence.md` and PDFs in `Task-04/`

---

## 📋 TASK 5 — Feature Development with Branching
**Folder:** `Task-05/`  
**Deliverables:** Working feature 1, feature branch, pull request, review comments and merge evidence.

- [x] **5.1** Create feature branch: `git checkout -b feature/document-intake`
- [x] **5.2** Implement Feature 1: Document intake REST endpoint and intake UI modal
- [x] **5.3** Stage and commit changes with descriptive commit logs
- [x] **5.4** Create Pull Request into `develop` integration branch
- [x] **5.5** Conduct peer review and document code review comments
- [x] **5.6** Merge feature branch into `develop` with merge commit evidence
- [x] **5.7** Save workflow logs and merge confirmation in `Task-05/`

---

## 📋 TASK 6 — MVP Completion and Git Collaboration
**Folder:** `Task-06/`  
**Deliverables:** Functional MVP, resolved merge conflict, tagged version and updated backlog.

- [x] **6.1** Complete remaining MVP functions: Searchable registry, KPI summary cards, status workflow, fraud alerts
- [x] **6.2** Create second feature branch: `feature/fraud-detection-rules`
- [x] **6.3** Deliberately introduce conflicting changes on `develop` and `feature/fraud-detection-rules`
- [x] **6.4** Resolve merge conflict manually preserving critical threshold logic
- [x] **6.5** Tag release baseline: `git tag -a v1.0 -m "Release v1.0 - Complete Insurance Verification MVP"`
- [x] **6.6** Update product backlog marking all MVP items completed
- [x] **6.7** Save conflict resolution walkthrough and tag evidence in `Task-06/`

---

## 📋 TASK 7 — Jenkins Installation and Continuous Integration Job
**Folder:** `Task-07_Jenkins-CI/`  
**Deliverables:** Configured Jenkins job, successful build log, trigger evidence and archived artefact.

- [x] **7.1** Install and configure Jenkins automation server on port 8080
- [x] **7.2** Install Git, Maven, and Pipeline plugins
- [x] **7.3** Configure JDK 21 and Maven 3.9 in Global Tool Configuration
- [x] **7.4** Create Freestyle CI build job `insurance-verification-ci`
- [x] **7.5** Configure GitHub SCM connection and Poll SCM trigger (`H/5 * * * *`)
- [x] **7.6** Configure build step: `mvn clean package`
- [x] **7.7** Configure Post-build artifact archiving for `target/*.jar`
- [x] **7.8** Verify successful build run and capture console logs
- [x] **7.9** Save `jenkins_ci_guide.md`, `ci_job_config.md`, `build_console_log.txt` in `Task-07_Jenkins-CI/`

---

## 📋 TASK 8 — Pipeline as Code and Server Deployment
**Folder:** `Task-08_Pipeline-Deployment/`  
**Deliverables:** Jenkinsfile, successful pipeline run, deployed application URL/screenshot and configuration evidence.

- [x] **8.1** Author root `Jenkinsfile` utilizing Declarative Pipeline syntax
- [x] **8.2** Implement multi-stage pipeline: Checkout → Build → Test → Package → Deploy
- [x] **8.3** Parameterize environment settings: `DEPLOY_ENV` (staging/production) and `APP_PORT` (8085)
- [x] **8.4** Create Pipeline Job `insurance-verification-pipeline` connected to repo Jenkinsfile
- [x] **8.5** Execute pipeline run and verify green status across all stages
- [x] **8.6** Verify application deployment on port 8085
- [x] **8.7** Save `pipeline_doc.md` and pipeline execution logs in `Task-08_Pipeline-Deployment/`

---

## 📋 TASK 9 — Selenium Test Design and Local Execution
**Folder:** `Task-09_Selenium-Tests/`  
**Deliverables:** Test plan, Selenium scripts, local test report and failure screenshot mechanism.

- [x] **9.1** Identify 5 critical user journeys (Baseline loading, Intake validation, Fraud alerting, Workflow status transition, KPI summary metrics)
- [x] **9.2** Author comprehensive test plan specifying test IDs, inputs, expected results
- [x] **9.3** Implement automated test cases in `InsuranceVerificationTests.java` with assertions
- [x] **9.4** Implement failure screenshot capture mechanism using `TakesScreenshot`
- [x] **9.5** Execute test suite locally via Maven: `mvn test`
- [x] **9.6** Save `test_plan.md` and `test_execution_report.md` in `Task-09_Selenium-Tests/`

---

## 📋 TASK 10 — Continuous Testing in Jenkins
**Folder:** `Task-10_Continuous-Testing/`  
**Deliverables:** Jenkins test report, failed pipeline evidence, defect correction commit and successful rerun.

- [x] **10.1** Integrate `junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'` into Jenkinsfile
- [x] **10.2** Configure Quality Gate: Failed tests automatically abort downstream deployment stages
- [x] **10.3** Deliberately introduce defect (altering fraud threshold from 70 to 10) to fail test assertions
- [x] **10.4** Document pipeline abort and capture failed test report evidence
- [x] **10.5** Commit defect fix: `git commit -m "Fix: Restore fraud detection threshold to 70"`
- [x] **10.6** Rerun pipeline and verify successful recovery and report publication
- [x] **10.7** Save `quality_gate_docs.md` and `defect_and_fix_evidence.md` in `Task-10_Continuous-Testing/`

---

## 📋 TASK 11 — Docker Image and Container Lifecycle
**Folder:** `Task-11_Docker-Container/`  
**Deliverables:** Dockerfile, image details, Docker command log and running container evidence.

- [x] **11.1** Author multi-stage/Alpine JRE `Dockerfile` with port 8085 exposure and health check
- [x] **11.2** Build and tag container image: `docker build -t sourabhshelke/insurance-verification:v1.0 .`
- [x] **11.3** Inspect image metadata and layers: `docker images`
- [x] **11.4** Launch container with port mapping: `docker run -d -p 8085:8085 --name insurance-app ...`
- [x] **11.5** Exercise full container lifecycle: `docker logs`, `docker stop`, `docker start`, `docker restart`, `docker rm`
- [x] **11.6** Document complete command execution log in `Task-11_Docker-Container/docker_commands.md`

---

## 📋 TASK 12 — Jenkins-Docker Continuous Deployment
**Folder:** `Task-12_Jenkins-Docker-CD/`  
**Deliverables:** Versioned image, registry evidence and end-to-end commit-to-container pipeline.

- [x] **12.1** Configure Docker Hub registry credentials in Jenkins
- [x] **12.2** Extend Jenkinsfile with automated Docker Build and Registry Tagging stages
- [x] **12.3** Automate container teardown and redeployment upon successful build
- [x] **12.4** Validate commit-to-container continuous delivery workflow
- [x] **12.5** Save `docker_cd_pipeline.md` and delivery logs in `Task-12_Jenkins-Docker-CD/`

---

## 📋 TASK 13 — Configuration Management Script
**Folder:** `Task-13_Config-Management/`  
**Deliverables:** Configuration specification, Ansible inventory and YAML playbook and first execution log.

- [x] **13.1** Detail target server prerequisites (JDK 21, Docker, app user, port 8085, logging paths)
- [x] **13.2** Create Ansible inventory `inventory.ini`
- [x] **13.3** Create Ansible playbook `setup.yml` automating directory creation, Docker verification, container launch, and health checks
- [x] **13.4** Author configuration specification in `Task-13_Config-Management/config_spec.md`
- [x] **13.5** Capture playbook execution logs in `Task-13_Config-Management/execution_log.txt`

---

## 📋 TASK 14 — Automated Provisioning and Reliability Validation
**Folder:** `Task-14_Provisioning-Validation/`  
**Deliverables:** Provisioned node, idempotency evidence, health-check result and rollback/recovery demonstration.

- [x] **14.1** Execute automated provisioning on target environment
- [x] **14.2** Demonstrate idempotency: Re-execute playbook and verify `changed=0, failed=0`
- [x] **14.3** Perform automated HTTP health probe against `/api/health`
- [x] **14.4** Demonstrate rollback and recovery procedure from defective release to previous stable image
- [x] **14.5** Save `idempotency_validation.md` and `rollback_demo.md` in `Task-14_Provisioning-Validation/`

---

## 📋 TASK 15 — Final End-to-End Release, Documentation and Viva
**Folder:** `Task-15_Final-Release-Docs/`  
**Deliverables:** Final technical report, viva presentation guide, troubleshooting guide, viva Q&A.

- [x] **15.1** Complete end-to-end audit of all deliverables
- [x] **15.2** Compile master technical project report (`final_technical_report.md`)
- [x] **15.3** Create comprehensive viva presentation guide with slide-by-slide script (`viva_presentation_guide.md`)
- [x] **15.4** Compile master printable project document (`Main_Doc.pdf`)
- [x] **15.5** Document common troubleshooting scenarios and architectural justifications

