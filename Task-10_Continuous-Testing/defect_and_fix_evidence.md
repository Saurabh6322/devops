# Defect Injection, Pipeline Abort & Fix Rerun Evidence (Task 10)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 💥 1. Deliberate Defect Injection
To test and validate the automated Quality Gate, an intentional bug was introduced in `DocumentApiController.java`:

### Broken Code:
```java
// BUG: Defectively inverted fraud threshold logic returning threshold score of 10 instead of 70
@GetMapping("/alerts")
public Map<String, Object> getFraudAlerts() {
    List<InsuranceDocument> highRiskDocs = repository.findByRiskScoreGreaterThanEqual(10); // BUG!
    Map<String, Object> response = new HashMap<>();
    response.put("totalAlerts", highRiskDocs.size());
    response.put("fraudThresholdScore", 10); // BUG: Fails assertion expecting 70
    response.put("flaggedDocuments", highRiskDocs);
    return response;
}
```

```bash
git commit -am "test(defect): Intentionally alter fraud threshold to test CI quality gate abort"
git push origin develop
```

---

## 🚫 2. Failed Pipeline Evidence (Build #5)
When Jenkins Build #5 ran, `TC-03` failed during the `Automated Tests` stage:

```text
[ERROR] Failures: 
[ERROR]   InsuranceVerificationTests.testFraudAlertDetection:81 
  JSON path "$.fraudThresholdScore" 
  Expected: is <70>
       got: <10>

[INFO] Tests run: 6, Failures: 1, Errors: 0, Skipped: 0
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:test
[Pipeline] junit
Recording test results
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage (Package Artifact) - SKIPPED
[Pipeline] stage (Docker Build & Tag) - SKIPPED
[Pipeline] stage (Containerized Deployment) - SKIPPED
Finished: FAILURE
```

**Quality Gate Result:** Deployment was completely blocked! Defective software did not reach the target server.

---

## 🛠️ 3. Defect Correction & Successful Rerun (Build #6)
The bug was fixed, restoring the correct $70$ threshold score:

```java
// FIXED: Restored correct 70% threshold
    List<InsuranceDocument> highRiskDocs = repository.findByRiskScoreGreaterThanEqual(70);
    response.put("fraudThresholdScore", 70);
```

```bash
git commit -am "fix: Correct fraud threshold comparison back to 70%"
git push origin develop
```

### Jenkins Build #6 Console Output:
```text
[INFO] Running com.insurancedoc.InsuranceVerificationTests
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 3.712 s
[INFO] BUILD SUCCESS
[Pipeline] junit
Recording test results
[Pipeline] stage (Package Artifact) - SUCCESS
[Pipeline] stage (Docker Build & Tag) - SUCCESS
[Pipeline] stage (Containerized Deployment) - SUCCESS
Finished: SUCCESS
```
**Verification Complete:** The pipeline recovered automatically, proving the reliability of continuous testing quality gates.

