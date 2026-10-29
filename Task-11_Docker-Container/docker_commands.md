# Docker Container Lifecycle Log & Documentation (Task 11)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🐳 1. Dockerfile Architecture

```dockerfile
FROM eclipse-temurin:21-jre-alpine
LABEL maintainer="Sourabh Shelke <23102C0029>"
LABEL description="Containerized Insurance Document Verification Portal - Production Image"
WORKDIR /app
COPY target/insurance-verification-portal.jar app.jar
EXPOSE 8085
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8085/api/health || exit 1
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/app.jar"]
```

---

## 🛠️ 2. Build Docker Image
```bash
# Package application fat JAR
mvn clean package -DskipTests

# Build versioned Docker image
docker build -t sourabhshelke/insurance-verification:v1.0 .
```

---

## 🔍 3. Inspect Docker Image
```bash
docker images | findstr insurance-verification
```

---

## 🚀 4. Run Container with Port Mapping
```bash
docker run -d -p 8085:8085 --name insurance-app sourabhshelke/insurance-verification:v1.0
```

Access portal in browser:  
👉 **`http://localhost:8085`**

---

## 📋 5. Complete Container Lifecycle Operations
```bash
# Inspect container logs
docker logs insurance-app

# Inspect running process status
docker ps | findstr insurance-app

# Stop container
docker stop insurance-app

# Restart container
docker restart insurance-app

# Remove container
docker rm -f insurance-app
```

