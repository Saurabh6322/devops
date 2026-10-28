# Definition of Done (DoD) — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🎯 Definition of Done (DoD) Checklist

A user story, feature, or DevOps task is officially considered **"DONE"** only when it satisfies all of the following quality criteria:

### 1. Source Code & Quality Standards
- [x] Code strictly adheres to Java naming conventions and clean architecture standards.
- [x] All business logic methods include descriptive JavaDoc or header documentation.
- [x] Zero compilation warnings or unhandled runtime exceptions.
- [x] Sensitive configuration (database credentials, private keys) are excluded from source files.

### 2. Version Control & GitFlow Compliance
- [x] Feature developed in an isolated branch (`feature/<feature-name>`).
- [x] Commit messages follow conventional commit guidelines (`feat:`, `fix:`, `docs:`, `ci:`).
- [x] Code merged into `develop` or `main` exclusively through reviewed Pull Requests.
- [x] No lingering merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

### 3. Automated Testing & Quality Gates
- [x] Automated unit and integration tests written in JUnit 5 and Spring Boot Test.
- [x] All 5 Critical User Journeys (CUJs) execute and pass with $100\%$ green status.
- [x] Automated test reports generated in `target/surefire-reports/`.
- [x] Selenium screenshot-on-failure mechanism tested and operational.

### 4. Build, Packaging & Containerization
- [x] Maven packages a standalone executable Spring Boot JAR file without errors.
- [x] Docker image builds successfully using lightweight Alpine JRE base.
- [x] Container launches cleanly, exposes port 8085, and passes the internal health probe (`/api/health`).

### 5. Infrastructure & Continuous Delivery
- [x] Jenkins declarative pipeline runs all stages (Checkout $\to$ Build $\to$ Test $\to$ Package $\to$ Deploy) successfully.
- [x] Ansible playbook runs idempotently without unexpected state modifications (`changed=0` on rerun).
- [x] Rollback script tested and capable of restoring the previous stable image within 30 seconds.

### 6. Documentation & Deliverables
- [x] Task-specific markdown and PDF documentation compiled in respective `Task-XX` directory.
- [x] Screenshots captured and verified for viva evaluation.
- [x] Master `CHECKPOINTS.md` updated with completed status.
