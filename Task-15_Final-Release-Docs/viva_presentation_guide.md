# Viva Presentation Guide & Comprehensive Q&A (Task 15)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🎤 1. Viva Presentation Slide Deck Outline (14 Slides)

| Slide # | Slide Title | Speaking Points & Key Content to Emphasize |
|:--------|:------------|:-------------------------------------------|
| **1** | Title Slide | Project Name: *Containerized Insurance Document Verification Portal*, Sourabh Shelke, Roll No: 23102C0029, BE CMPN. |
| **2** | Problem Statement | Traditional manual insurance document processing takes 5–15 days with high fraud vulnerability. |
| **3** | Proposed Solution | Automated Spring Boot microservice with heuristic fraud scoring, containerized and managed via DevOps CI/CD. |
| **4** | Architecture Diagram | 3-tier model: Frontend UI $\to$ Spring Boot Microservice $\to$ Embedded H2 Database. |
| **5** | DevOps Lifecycle Workflow | End-to-end flow: Git $\to$ Jenkins $\to$ Selenium/JUnit $\to$ Docker $\to$ Ansible. |
| **6** | 5 Core MVP Features | 1. Document Intake, 2. Searchable Registry, 3. Summary KPIs, 4. Underwriter Drill-Down, 5. Fraud Alert Engine. |
| **7** | Git & Collaboration | GitFlow branching, Pull Requests, merge conflict creation and manual resolution, tagging release `v1.0`. |
| **8** | Continuous Integration | Jenkins Freestyle job with SCM polling, automated Maven compilation, and artifact archiving. |
| **9** | Pipeline as Code | Declarative `Jenkinsfile` with parameterized environments (`DEPLOY_ENV`, `APP_PORT`). |
| **10** | Continuous Testing & Quality Gate | 6 Critical User Journeys tested. Injected intentional defect; Jenkins stopped deployment. Restored and passed. |
| **11** | Docker Containerization | Alpine JRE Dockerfile, container lifecycle testing, and port 8085 mapping. |
| **12** | Continuous Deployment | Automated commit-to-container pipeline building versioned tags and deploying fresh containers. |
| **13** | Ansible Configuration Management | Automated server setup, idempotency validation (`changed=0`), and rollback demonstration. |
| **14** | Conclusion & Q&A | Summary of results: sub-second intake, 100% fraud flagging, repeatable zero-downtime deployment. |

---

## 💡 2. Top Viva Questions & Model Answers

### Q1: What is the difference between Continuous Integration (CI), Continuous Delivery (CD), and Continuous Deployment?
> **Answer:**  
> - **Continuous Integration (CI):** Developers merge code regularly into a shared branch. Automated builds and unit tests verify each commit to detect integration bugs early.
> - **Continuous Delivery (CD):** Extends CI by automatically packaging artifacts and deploying them to staging/test environments so software is always in a release-ready state, with production release triggered manually.
> - **Continuous Deployment:** Removes the manual approval step; every change that passes all automated tests and quality gates is automatically deployed to production.

### Q2: What is a Declarative Jenkinsfile and why is it preferred over Freestyle jobs?
> **Answer:**  
> A Declarative Jenkinsfile implements **Pipeline as Code**. Instead of configuring jobs manually through the Jenkins web GUI (which is difficult to version or audit), the entire pipeline definition is stored as a text file in the Git repository alongside the application code. This enables version tracking, branch-specific pipelines, automated peer review, and disaster recovery.

### Q3: What is the concept of a Quality Gate in your pipeline?
> **Answer:**  
> A Quality Gate is a condition or checkpoint that code must satisfy before progressing to subsequent pipeline stages. In my pipeline, the `Automated Tests` stage serves as the Quality Gate. If any of the 6 Selenium/JUnit test assertions fail, Maven exits with an error code, Jenkins halts immediately, and the packaging, Docker build, and deployment stages are blocked.

### Q4: What is Idempotency in Ansible and why is it essential?
> **Answer:**  
> Idempotency is the property of an operation where executing it multiple times leaves the system in the exact same state as executing it once, without causing redundant actions or side effects. In my Task 14, the initial playbook run showed `changed=2`, while re-running the exact same playbook showed `changed=0`. This ensures that applying configuration management does not accidentally overwrite running configurations or cause downtime.

### Q5: What is the difference between a Docker image and a Docker container?
> **Answer:**  
> A **Docker image** is an immutable, read-only template or snapshot containing the application code, runtime libraries, and environment settings (defined by the `Dockerfile`). A **Docker container** is a runnable, isolated instance of an image with a writable container layer executed by the Docker engine.

### Q6: How does your application prevent insurance fraud?
> **Answer:**  
> The portal implements heuristic fraud risk scoring evaluating submission metadata, claim amounts, and document tamper parameters. Any document with a risk score $\ge 70\%$ is automatically quarantined with status `FLAGGED_FRAUD`, triggering high-priority visual alert banners and requiring dedicated investigation by an underwriter before any payment can be authorized.

