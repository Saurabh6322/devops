import http.server
import socketserver
import json
import os
import re
from datetime import datetime

PORT = 8085
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FILE = os.path.join(BASE_DIR, "src", "main", "resources", "static", "index.html")

# In-memory document storage matching Spring Boot H2 seed dataset
documents = [
    {
        "id": 1,
        "documentNumber": "DOC-2026-1001",
        "policyNumber": "POL-982140",
        "claimantName": "Aarav Sharma",
        "documentType": "Hospital Invoice",
        "verificationStatus": "VERIFIED",
        "riskScore": 12,
        "authenticityConfidence": 98.5,
        "claimAmount": 45000.0,
        "reviewerNotes": "Hospital seal and GST invoice number authenticated with health registry.",
        "submissionDate": "2026-10-28T10:15:00",
        "lastUpdated": "2026-10-28T10:20:00"
    },
    {
        "id": 2,
        "documentNumber": "DOC-2026-1002",
        "policyNumber": "POL-773412",
        "claimantName": "Sneha Kulkarni",
        "documentType": "Surveyor Report",
        "verificationStatus": "UNDER_REVIEW",
        "riskScore": 42,
        "authenticityConfidence": 86.0,
        "claimAmount": 125000.0,
        "reviewerNotes": "Accident scene images uploaded; awaiting surveyor vehicle chassis confirmation.",
        "submissionDate": "2026-10-28T10:30:00",
        "lastUpdated": "2026-10-28T10:45:00"
    },
    {
        "id": 3,
        "documentNumber": "DOC-2026-1003",
        "policyNumber": "POL-651908",
        "claimantName": "Rohan Mehta",
        "documentType": "Police FIR",
        "verificationStatus": "FLAGGED_FRAUD",
        "riskScore": 88,
        "authenticityConfidence": 34.0,
        "claimAmount": 320000.0,
        "reviewerNotes": "CRITICAL: Digital tampering detected in FIR timestamp and jurisdictional station code.",
        "submissionDate": "2026-10-28T11:00:00",
        "lastUpdated": "2026-10-28T11:15:00"
    },
    {
        "id": 4,
        "documentNumber": "DOC-2026-1004",
        "policyNumber": "POL-441290",
        "claimantName": "Priya Nair",
        "documentType": "KYC Identity",
        "verificationStatus": "VERIFIED",
        "riskScore": 8,
        "authenticityConfidence": 99.2,
        "claimAmount": 0.0,
        "reviewerNotes": "National ID card digitally verified with government UID database.",
        "submissionDate": "2026-10-28T11:20:00",
        "lastUpdated": "2026-10-28T11:22:00"
    },
    {
        "id": 5,
        "documentNumber": "DOC-2026-1005",
        "policyNumber": "POL-330911",
        "claimantName": "Vikram Deshmukh",
        "documentType": "Damage Estimate",
        "verificationStatus": "SUBMITTED",
        "riskScore": 25,
        "authenticityConfidence": 91.5,
        "claimAmount": 68000.0,
        "reviewerNotes": "Initial workshop quotation received; automated OCR pre-screen passed.",
        "submissionDate": "2026-10-28T11:40:00",
        "lastUpdated": "2026-10-28T11:40:00"
    },
    {
        "id": 6,
        "documentNumber": "DOC-2026-1006",
        "policyNumber": "POL-119844",
        "claimantName": "Ananya Verma",
        "documentType": "Medical Prescription",
        "verificationStatus": "FLAGGED_FRAUD",
        "riskScore": 76,
        "authenticityConfidence": 41.2,
        "claimAmount": 54000.0,
        "reviewerNotes": "Duplicate claim bill detected across multiple third-party administrators (TPA).",
        "submissionDate": "2026-10-28T12:00:00",
        "lastUpdated": "2026-10-28T12:05:00"
    }
]

class PortalHandler(http.server.SimpleHTTPRequestHandler):
    def send_json(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(STATIC_FILE, "rb") as f:
                self.wfile.write(f.read())
            return

        if self.path.startswith("/api/documents"):
            self.send_json(200, documents)
            return

        if self.path == "/api/summary":
            total = len(documents)
            verified = sum(1 for d in documents if d["verificationStatus"] == "VERIFIED")
            under_review = sum(1 for d in documents if d["verificationStatus"] == "UNDER_REVIEW")
            flagged = sum(1 for d in documents if d["verificationStatus"] == "FLAGGED_FRAUD" or d["riskScore"] >= 70)
            submitted = sum(1 for d in documents if d["verificationStatus"] == "SUBMITTED")
            avg_risk = sum(d["riskScore"] for d in documents) / total if total > 0 else 0
            total_claims = sum(d["claimAmount"] for d in documents)

            summary = {
                "totalDocuments": total,
                "verifiedCount": verified,
                "underReviewCount": under_review,
                "flaggedFraudCount": flagged,
                "submittedCount": submitted,
                "averageRiskScore": round(avg_risk, 1),
                "totalClaimAmount": round(total_claims, 2)
            }
            self.send_json(200, summary)
            return

        if self.path == "/api/alerts":
            flagged = [d for d in documents if d["riskScore"] >= 70 or d["verificationStatus"] == "FLAGGED_FRAUD"]
            self.send_json(200, {
                "totalAlerts": len(flagged),
                "fraudThresholdScore": 70,
                "flaggedDocuments": flagged
            })
            return

        if self.path == "/api/health":
            self.send_json(200, {
                "status": "UP",
                "application": "Insurance Document Verification Portal",
                "student": "SOURABH SHELKE",
                "rollNo": "23102C0029",
                "version": "1.0.0",
                "timestamp": datetime.now().isoformat()
            })
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        if self.path == "/api/documents":
            payload = json.loads(post_data.decode("utf-8"))
            new_id = len(documents) + 1
            new_doc = {
                "id": new_id,
                "documentNumber": payload.get("documentNumber") or f"DOC-2026-{1000 + new_id}",
                "policyNumber": payload.get("policyNumber", "POL-UNKNOWN"),
                "claimantName": payload.get("claimantName", "Unknown"),
                "documentType": payload.get("documentType", "Claim Document"),
                "verificationStatus": "VERIFIED" if payload.get("riskScore", 20) < 30 else ("FLAGGED_FRAUD" if payload.get("riskScore", 20) >= 70 else "UNDER_REVIEW"),
                "riskScore": payload.get("riskScore", 20),
                "authenticityConfidence": payload.get("authenticityConfidence", 95.0),
                "claimAmount": payload.get("claimAmount", 0.0),
                "reviewerNotes": payload.get("reviewerNotes", "Intake submitted successfully."),
                "submissionDate": datetime.now().isoformat(),
                "lastUpdated": datetime.now().isoformat()
            }
            documents.insert(0, new_doc)
            self.send_json(201, new_doc)
            return

        if self.path == "/api/simulate":
            import random
            for d in documents:
                delta = random.randint(-8, 8)
                new_risk = max(5, min(95, d["riskScore"] + delta))
                d["riskScore"] = new_risk
                d["authenticityConfidence"] = round(100.0 - (new_risk * 0.75), 1)
                if new_risk >= 70:
                    d["verificationStatus"] = "FLAGGED_FRAUD"
                elif new_risk >= 30 and d["verificationStatus"] == "VERIFIED":
                    d["verificationStatus"] = "UNDER_REVIEW"
                d["lastUpdated"] = datetime.now().isoformat()

            self.send_json(200, {
                "message": "Simulated automated OCR verification & fraud scoring batch completed.",
                "processedRecords": len(documents),
                "timestamp": datetime.now().isoformat()
            })
            return

        self.send_response(404)
        self.end_headers()

    def do_PUT(self):
        match = re.match(r"^/api/documents/(\d+)/status$", self.path)
        if match:
            doc_id = int(match.group(1))
            content_length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(content_length).decode("utf-8"))

            target = next((d for d in documents if d["id"] == doc_id), None)
            if target:
                if "status" in payload:
                    target["verificationStatus"] = payload["status"]
                if "notes" in payload:
                    target["reviewerNotes"] = payload["notes"]
                target["lastUpdated"] = datetime.now().isoformat()
                self.send_json(200, target)
                return
            else:
                self.send_response(404)
                self.end_headers()
                return

        self.send_response(404)
        self.end_headers()

if __name__ == "__main__":
    print(f"==================================================================")
    print(f"  Containerized Insurance Document Verification Portal")
    print(f"  Candidate: {STUDENT_NAME} (Roll No: {ROLL_NO})")
    print(f"  Running on: http://localhost:{PORT}")
    print(f"==================================================================")
    with socketserver.TCPServer(("", PORT), PortalHandler) as httpd:
        httpd.serve_forever()
