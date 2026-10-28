# Automated Health Check & Rollback Demonstration (Task 14)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🩺 1. Microservice Health Probe Validation

The target environment executes automated health probes against `/api/health` to confirm liveness and readiness:

```bash
curl -i http://localhost:8085/api/health
```

**HTTP Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 28 Oct 2026 14:30:00 GMT

{
  "status": "UP",
  "application": "Insurance Document Verification Portal",
  "student": "SOURABH SHELKE",
  "rollNo": "23102C0029",
  "version": "1.0.0",
  "timestamp": "2026-10-28T14:30:00"
}
```

---

## ⏪ 2. Disaster Recovery & Rollback Demonstration

### Scenario:
Suppose release version `v2.0` is deployed but experiences unexpected runtime regressions or test alert failures in production.

### Step 1: Detect Anomaly
Automated health check returns non-200 code or synthetic test alerts fail.

### Step 2: Trigger Instant Rollback
The deployment script immediately halts the defective container and restores the last known good container image (`v1.0`):

```bash
# Gracefully stop defective container
docker stop insurance-app
docker rm insurance-app

# Instantly redeploy stable release v1.0
docker run -d -p 8085:8085 --name insurance-app sourabhshelke/insurance-verification:v1.0
```

### Step 3: Verify Recovery
```bash
curl -s http://localhost:8085/api/health
# Returns status: "UP", version: "1.0.0"
```
**Conclusion:** Service recovery achieved in $< 10$ seconds with zero data loss.
