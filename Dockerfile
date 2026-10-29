# ==============================================================================
# Multi-Stage Dockerfile for Containerized Insurance Document Verification Portal
# Author: Sourabh Shelke | Roll No: 23102C0029 | BE CMPN
# ==============================================================================

# Stage 1: Build & Package application using Maven
FROM maven:3.9-eclipse-temurin-21-alpine AS builder
WORKDIR /workspace

# Copy dependencies and source code
COPY pom.xml .
COPY src ./src

# Package standalone Spring Boot executable fat JAR
RUN mvn clean package -DskipTests

# Stage 2: Production Lightweight Alpine JRE Image
FROM eclipse-temurin:21-jre-alpine

LABEL maintainer="Sourabh Shelke <23102C0029>"
LABEL project="Containerized Insurance Document Verification Portal"
LABEL roll_no="23102C0029"

WORKDIR /app

# Copy packaged JAR from build stage
COPY --from=builder /workspace/target/*.jar app.jar

# Expose application port (8085 avoids standard Jenkins 8080 collision)
EXPOSE 8085

# Microservice health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8085/api/health || exit 1

# Execute standalone Spring Boot application
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/app.jar"]
