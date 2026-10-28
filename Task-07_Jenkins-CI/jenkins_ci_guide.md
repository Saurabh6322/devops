# Jenkins CI Server Setup & Freestyle Job Guide (Task 7)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🏗️ 1. Jenkins Installation & Initial Configuration
1. **Download & Start Jenkins:**
   - Jenkins installed on the CI runner node and executed via:
     ```bash
     java -jar jenkins.war --httpPort=8080
     ```
   - Accessed web console at `http://localhost:8080`.
2. **Plugin Installation:**
   - Git Plugin
   - Maven Integration Plugin
   - Pipeline Plugin
   - JUnit Plugin (for test report parsing)
3. **Global Tool Configuration:**
   - **JDK:** Name `JDK 21`, Path `/usr/lib/jvm/java-21` (or Windows Temurin JDK path).
   - **Maven:** Name `Maven 3.9`, auto-install or local path configured.

---

## ⚙️ 2. Freestyle Job Configuration: `insurance-verification-ci`
- **Job Name:** `insurance-verification-ci`
- **Source Code Management:** Git
  - Repository URL: `https://github.com/sourabhshelke/insurance-document-verification-portal.git`
  - Branch Specifier: `*/main`
- **Build Trigger:** Poll SCM (`H/5 * * * *` — checks every 5 minutes for new commits).
- **Build Step:**
  - Invoke top-level Maven targets: `clean package`
- **Post-Build Actions:**
  - Archive the artifacts: `target/*.jar`
  - Publish JUnit test result report: `target/surefire-reports/*.xml`

---

## 📦 3. Archived Artifact Verification
- Generated Artifact: `insurance-verification-portal.jar` (packaged Spring Boot fat JAR).
- Archived location in Jenkins: Fingerprinted and available for downstream deployment.
