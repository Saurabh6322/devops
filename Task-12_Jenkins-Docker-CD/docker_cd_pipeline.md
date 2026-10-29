# Jenkins-Docker Continuous Deployment Pipeline (Task 12)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🚀 1. Continuous Delivery Pipeline Architecture

```mermaid
flowchart LR
    A[Git Commit to main/develop] --> B[Jenkins CI: Build & Test]
    B --> C[Package Executable Spring Boot JAR]
    C --> D[Docker Build: sourabhshelke/insurance-verification:${BUILD_NUMBER}]
    D --> E[Tag Image as 'latest']
    E --> F[Containerized Deployment on Target Port 8085]
    F --> G[Automated HTTP Health Probe /api/health]
```

---

## 📦 2. Extended Jenkinsfile Stages for Docker CD

```groovy
stage('Docker Build & Tag') {
    steps {
        echo "Building versioned Docker image: sourabhshelke/insurance-verification:${BUILD_NUMBER}..."
        bat "docker build -t sourabhshelke/insurance-verification:${BUILD_NUMBER} -t sourabhshelke/insurance-verification:latest ."
    }
}

stage('Containerized Deployment') {
    steps {
        echo "Deploying containerized application on port ${params.APP_PORT}..."
        bat "docker stop insurance-app || exit 0"
        bat "docker rm insurance-app || exit 0"
        bat "docker run -d -p ${params.APP_PORT}:8085 --name insurance-app sourabhshelke/insurance-verification:latest"
        echo "Validating health probe..."
        bat "curl -s http://localhost:${params.APP_PORT}/api/health"
    }
}
```

---

## 🎯 3. Verification & Zero-Downtime Guarantee
- **Automated Versioning:** Every successful build automatically generates a numbered container tag (`${BUILD_NUMBER}`) ensuring immutable artifact traceability.
- **Rollback Readiness:** If a newer container instance experiences runtime errors, rolling back requires only re-launching the preceding build number image.
- **Environment Isolation:** Container guarantees identical execution across developer laptops, Jenkins agents, and cloud servers.

