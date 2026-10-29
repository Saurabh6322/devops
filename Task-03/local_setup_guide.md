# Local Development Setup Guide — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 💻 1. System Requirements & Prerequisites
Ensure your local host or virtual workstation satisfies the following requirements:
- **Operating System:** Windows 10/11, macOS, or Ubuntu Linux 22.04 LTS
- **Java Development Kit:** Java SE 17, 21, or 23 (OpenJDK / Eclipse Temurin)
- **Build Tool:** Apache Maven 3.8+ (or Maven Wrapper `mvnw`)
- **Container Engine:** Docker Desktop or Docker CE Engine
- **Memory & Storage:** 8 GB RAM minimum, 10 GB free disk space

---

## ⚙️ 2. Verification of Installed Toolchains

```bash
# Verify Java Compiler and Runtime
java -version

# Verify Apache Maven
mvn -version

# Verify Docker Daemon
docker version

# Verify Git
git --version
```

---

## 🚀 3. Step-by-Step Local Execution

### Step 1: Clone Repository
```bash
git clone https://github.com/sourabhshelke/insurance-document-verification-portal.git
cd insurance-document-verification-portal
```

### Step 2: Compile & Run Locally via Maven
```bash
mvn clean spring-boot:run
```

### Step 3: Access Application Endpoints
- **Web Dashboard:** Open `http://localhost:8085` in Google Chrome or Edge.
- **Microservice Health Check:** `http://localhost:8085/api/health`
- **H2 Database Console:** `http://localhost:8085/h2-console`
  - JDBC URL: `jdbc:h2:mem:insurancedb`
  - User: `sa`
  - Password: *(leave blank)*

### Step 4: Run Automated Tests
```bash
mvn test
```
Reports are automatically generated and saved in `target/surefire-reports/`.

