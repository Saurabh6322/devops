# Automated Test Plan & Strategy — Insurance Verification Portal (Task 9)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🎯 1. Testing Objectives & Scope
The automated test suite verifies the end-to-end functionality, schema integrity, role-based workflow transitions, and fraud threshold alerting of the Insurance Document Verification Portal before deployment through Jenkins.

---

## 📋 2. Critical User Journeys (CUJs) Matrix

| Test Case ID | Critical User Journey (CUJ) | Target Component / API | Test Steps & Input Data | Expected Result & Assertions |
|:-------------|:----------------------------|:-----------------------|:------------------------|:-----------------------------|
| **TC-01** | Initial Document Ingestion & Registry Load | `GET /api/documents` | Ingest default seed dataset; call endpoint. | Returns HTTP 200; $\ge 1$ documents returned; non-null `documentNumber`. |
| **TC-02** | New Document Intake & Validation | `POST /api/documents` | Send valid document payload (Policy: `POL-554433`, Claimant: `Vikram Malhotra`, Type: `Surveyor Report`, Claim: ₹85,000). | Returns HTTP 201 Created; auto-generated `DOC-` prefix; status `VERIFIED`. |
| **TC-03** | High-Risk Fraud Alert Trigger | `GET /api/alerts` | Inject document with risk score $92\%$; query alert endpoint. | Returns HTTP 200; `totalAlerts >= 1`; fraud cutoff $= 70$; document listed. |
| **TC-04** | Role-Based Workflow Status Progression | `PUT /api/documents/{id}/status` | Submit status update to `UNDER_REVIEW` with underwriter notes. | Returns HTTP 200; status persisted as `UNDER_REVIEW`; reviewer remarks preserved. |
| **TC-05** | Dashboard KPI Metrics Aggregation | `GET /api/summary` | Query summary metrics calculation. | Returns HTTP 200; total count, average risk score, and claim amount calculated. |
| **TC-06** | Microservice Health Probe | `GET /api/health` | Query readiness and liveness probe. | Returns HTTP 200; `status: "UP"`; author `SOURABH SHELKE`. |

---

## 📸 3. Failure Screenshot Capture Mechanism
To support unattended continuous testing inside CI, a dedicated screenshot utility captures the visual browser state whenever an assertion fails:

```java
public void captureFailureScreenshot(WebDriver driver, String testName) {
    try {
        TakesScreenshot ts = (TakesScreenshot) driver;
        File source = ts.getScreenshotAs(OutputType.FILE);
        String destination = "target/screenshots/" + testName + "_" + System.currentTimeMillis() + ".png";
        FileUtils.copyFile(source, new File(destination));
        System.out.println("Screenshot captured on failure: " + destination);
    } catch (Exception e) {
        System.err.println("Could not capture screenshot: " + e.getMessage());
    }
}
```

---

## ⚙️ 4. Test Execution Command
Run the test suite locally:
```bash
mvn test
```
Surefire XML test reports are automatically saved to:
`target/surefire-reports/`

