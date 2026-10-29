# RESTful API Specifications & Data Model — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 📋 REST API Endpoints Specification

| Method | Endpoint | Description | Request Body / Parameters | Success Response |
|:-------|:---------|:------------|:--------------------------|:-----------------|
| `GET` | `/api/documents` | Retrieve all documents with optional filters | Query: `?status=VERIFIED&search=POL-` | `200 OK` (Array of Documents) |
| `GET` | `/api/documents/{id}` | Get specific document by ID | Path variable: `id` | `200 OK` (Document Object) or `404` |
| `POST` | `/api/documents` | Submit new document for verification | JSON with `policyNumber`, `claimantName`, `documentType`, `claimAmount` | `201 Created` (Saved Document) |
| `PUT` | `/api/documents/{id}/status` | Update workflow status and remarks | JSON with `status`, `notes` | `200 OK` (Updated Document) |
| `GET` | `/api/alerts` | Get all high-risk fraud alerts ($\ge 70\%$) | None | `200 OK` (Alert count + List) |
| `GET` | `/api/summary` | Get aggregated KPI summary metrics | None | `200 OK` (Summary JSON) |
| `POST` | `/api/simulate` | Trigger simulated OCR re-evaluation | None | `200 OK` (Confirmation JSON) |
| `GET` | `/api/health` | Microservice health check & metadata | None | `200 OK` (`status: "UP"`) |

---

## 🗄️ Data Model: `InsuranceDocument` Entity

```sql
CREATE TABLE insurance_documents (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    document_number VARCHAR(255) NOT NULL UNIQUE,
    policy_number VARCHAR(255) NOT NULL,
    claimant_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(255) NOT NULL,
    verification_status VARCHAR(50) NOT NULL,
    risk_score INT NOT NULL,
    authenticity_confidence DOUBLE NOT NULL,
    claim_amount DOUBLE NOT NULL,
    reviewer_notes VARCHAR(1000),
    submission_date TIMESTAMP,
    last_updated TIMESTAMP
);
```

### Sample Document JSON Payload:
```json
{
  "documentNumber": "DOC-2026-1001",
  "policyNumber": "POL-982140",
  "claimantName": "Aarav Sharma",
  "documentType": "Hospital Invoice",
  "verificationStatus": "VERIFIED",
  "riskScore": 12,
  "authenticityConfidence": 98.5,
  "claimAmount": 45000.00,
  "reviewerNotes": "Hospital seal and GST invoice number authenticated with health registry.",
  "submissionDate": "2026-10-28T10:00:00",
  "lastUpdated": "2026-10-28T10:05:00"
}
```

