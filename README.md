# 🛡️ Containerized Insurance Document Verification Portal

**Author:** Sourabh Shelke  
**Roll No:** 23102C0029  
**Class:** BE CMPN (Vidyalankar Institute of Technology)  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 📖 Overview
The **Containerized Insurance Document Verification Portal** is an enterprise-grade DevOps demonstration system designed to streamline and automate the ingestion, verification, risk assessment, and fraud detection of insurance claim documents (such as Hospital Bills, KYC Proofs, Surveyor Inspection Reports, Police FIRs, and Damage Estimates).

The system integrates modern CI/CD automation, declarative infrastructure as code, container lifecycle management, automated quality gates, and automated configuration management using **Java 21/23, Spring Boot 3.2, Maven, Selenium, Jenkins, Docker, and Ansible**.

---

## 🛠️ DevOps Technology Stack
| Layer | Technology | Purpose |
|:------|:-----------|:--------|
| **Backend Framework** | Java (OpenJDK 21/23), Spring Boot 3.2.x | REST API, Business Logic, Validation Engine |
| **Data Persistence** | Embedded H2 Database, Spring Data JPA | In-memory relational storage with H2 Web Console |
| **Frontend UI** | HTML5, CSS3 Custom Properties, Vanilla JavaScript | Responsive single-page dashboard with real-time KPIs |
| **Build & Dependency** | Apache Maven 3.9+ | Build lifecycle, compilation, packaging, testing |
| **Version Control** | Git, GitHub | GitFlow branching, PR reviews, merge conflict resolution |
| **Continuous Integration** | Jenkins (Freestyle & Declarative Pipeline) | Automated webhook/polling builds, artifact archiving |
| **Quality Gate & Testing** | Selenium WebDriver 4.x, JUnit 5, MockMvc | Automated E2E testing, failure screenshot capture |
| **Containerization** | Docker, Dockerfile (Alpine JRE) | Port mapping, resource isolation, zero-downtime updates |
| **Config Management** | Ansible Playbooks & Inventories | Automated node provisioning, idempotency validation |

---

## 🚀 Quick Start (Local Run)

### Prerequisites:
- Java JDK 17, 21, or 23 installed
- Apache Maven 3.8+ (or Maven Wrapper)

### 1. Build and Run:
```bash
# Clone the repository
git clone https://github.com/sourabhshelke/insurance-document-verification-portal.git
cd insurance-document-verification-portal

# Build and start via Maven
mvn clean spring-boot:run
```

Access the interactive dashboard in your browser:  
👉 **`http://localhost:8085`**

Access the H2 Database Console:  
👉 **`http://localhost:8085/h2-console`** (JDBC URL: `jdbc:h2:mem:insurancedb`, User: `sa`, Password: *(empty)*)

---

## 🐳 Containerized Run (Docker)

```bash
# 1. Package the JAR file
mvn clean package -DskipTests

# 2. Build the Docker image
docker build -t sourabhshelke/insurance-verification:v1.0 .

# 3. Run the container
docker run -d -p 8085:8085 --name insurance-app sourabhshelke/insurance-verification:v1.0

# 4. Check microservice health
curl http://localhost:8085/api/health
```

---

## 📋 5 Core MVP Features
1. **Document Intake & Event Entry:** Comprehensive form to submit insurance documents with policy number, claimant identity, document type, and claim amount.
2. **Searchable Registry Dashboard:** Real-time search across policy numbers, claimants, and document IDs with status filtering (Submitted, Under Review, Verified, Flagged Fraud, Rejected).
3. **Summary KPI Indicators:** Live statistical cards tracking Total Submissions, Verified Clean rate, Under Review count, Flagged Fraud incidents, and Claim volume.
4. **Role-Based Status Drill-Down & Audit:** Detail inspection modal for underwriting officers to review authenticity confidence, update status, and log remarks.
5. **Automated OCR Risk Scoring & Fraud Alert:** Automated heuristic risk scoring engine highlighting suspicious documents (risk score &ge; 70%) with instant compliance alerts.

---

## 🔄 End-to-End DevOps Lifecycle
```
[Plan] ──> [Code (Git)] ──> [Build (Maven)] ──> [Test (Selenium/JUnit)] ──> [Package (JAR)] ──> [Dockerize] ──> [Deploy (Ansible)] ──> [Monitor]
```

---

## 📂 Project Structure
```
insurance-verification-portal/
├── Task-01/                        # Problem Statement, Stakeholders, Scope Docs & PDFs
├── Task-02/                        # User Stories, Product Backlog, Sprint Plan, DevOps Diagram
├── Task-03/                        # Architecture Diagram, SRS Summary, API Specifications
├── Task-04/                        # Git Initialization, Branch Policy, Repo Metadata
├── Task-05/                        # Feature Branching, Pull Request & Merge Review Evidence
├── Task-06/                        # MVP Completion, Merge Conflict Resolution & v1.0 Release Tag
├── Task-07_Jenkins-CI/             # Jenkins CI Freestyle Build Job, Artifact Archiving
├── Task-08_Pipeline-Deployment/    # Declarative Jenkinsfile Pipeline & Multi-Environment Deploy
├── Task-09_Selenium-Tests/         # Test Plan, 5 Critical User Journeys, Failure Screenshots
├── Task-10_Continuous-Testing/     # Quality Gate Enforcement, Defect Injection & Fix Rerun
├── Task-11_Docker-Container/       # Dockerfile, Image Tagging & Container Lifecycle Log
├── Task-12_Jenkins-Docker-CD/      # Automated Jenkins-Docker Registry & Continuous Delivery
├── Task-13_Config-Management/      # Ansible Inventory & Playbook for Target Server Setup
├── Task-14_Provisioning-Validation/# Idempotency Demonstration, Health Checks & Rollback Test
├── Task-15_Final-Release-Docs/     # Final Technical Report, Viva Presentation Guide & Q&A
├── src/                            # Full Java Spring Boot Application Source Code
├── Dockerfile                      # Production JRE Docker Container Configuration
├── Jenkinsfile                     # Multi-Stage Declarative CI/CD Pipeline as Code
├── CHECKPOINTS.md                  # Master 15-Task Verification Checkpoint Tracker
└── README.md                       # Master Project Readme & Technical Reference
```
