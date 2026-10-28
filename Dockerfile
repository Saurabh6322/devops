# Production Lightweight JRE base image for Containerized Insurance Document Verification Portal
FROM eclipse-temurin:21-jre-alpine

LABEL maintainer="Sourabh Shelke <23102C0029>"
LABEL description="Containerized Insurance Document Verification Portal - Production Image"

WORKDIR /app

# Copy the pre-built Spring Boot executable JAR
COPY target/insurance-verification-portal.jar app.jar

# Expose microservice port (8085 avoids standard Jenkins 8080 collision)
EXPOSE 8085

# Microservice health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8085/api/health || exit 1

# Execute standalone Spring Boot application
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/app.jar"]
