import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

STUDENT_NAME = "Sourabh Shelke"
ROLL_NO = "23102C0029"
PROJECT_TITLE = "Containerized Insurance Document Verification Portal"
INSTITUTE = "Vidyalankar Institute of Technology"
CLASS_NAME = "BE CMPN (Computer Engineering)"
ACADEMIC_YEAR = "2026-27"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(54, 750, f"{PROJECT_TITLE} — {STUDENT_NAME} ({ROLL_NO})")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 744, 558, 744)
        
        self.line(54, 48, 558, 48)
        self.drawString(54, 36, f"{INSTITUTE} | {CLASS_NAME}")
        self.drawRightString(558, 36, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def get_base_styles():
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle('DocH1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=colors.HexColor('#1e293b'), spaceAfter=8)
    h2 = ParagraphStyle('DocH2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#334155'), spaceBefore=8, spaceAfter=4)
    body = ParagraphStyle('DocBody', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#1f2937'), spaceAfter=5)
    bullet = ParagraphStyle('DocBullet', parent=body, leftIndent=15, firstLineIndent=-10, spaceAfter=3)
    meta = ParagraphStyle('DocMeta', parent=body, fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor('#4338ca'), spaceAfter=8)
    code = ParagraphStyle('DocCode', parent=body, fontName='Courier', fontSize=7.5, leading=9.5, textColor=colors.HexColor('#0f172a'))
    return {'h1': h1, 'h2': h2, 'body': body, 'bullet': bullet, 'meta': meta, 'code': code}

def make_table(data, col_widths=None):
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t

# 1. Problem Statement
def build_problem_statement(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Problem Statement — Insurance Document Verification Portal", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Introduction", S['h2']),
        Paragraph("In modern insurance claims processing, document verification remains the single largest operational bottleneck. Annually, insurance providers process millions of customer-submitted documents—including hospital bills, death/disability certificates, motor surveyor inspection reports, police FIRs, and KYC identity proofs.", S['body']),
        Spacer(1, 4),
        Paragraph("2. Problem Definition", S['h2']),
        Paragraph("There is currently no unified, lightweight, containerized verification platform available to insurance carriers that:", S['body']),
        Paragraph("• Ingests multi-category claim documents and policy proofs in real time.", S['bullet']),
        Paragraph("• Extracts and indexes key policy parameters (policy number, claimant identity, claimed amount).", S['bullet']),
        Paragraph("• Automatically calculates heuristic authenticity scores and flags suspicious documents (risk score &ge; 70%).", S['bullet']),
        Paragraph("• Provides a centralized, searchable registry with role-based workflow progression.", S['bullet']),
        Paragraph("• Operates reliably within an automated CI/CD pipeline ensuring zero-downtime containerized updates.", S['bullet']),
        Spacer(1, 4),
        Paragraph("3. Target Users", S['h2']),
        make_table([
            ["#", "User Persona", "Operational Role & Responsibilities"],
            ["1", "Policyholders / Claimants", "Upload policy proofs and claim bills; track real-time verification status."],
            ["2", "Underwriters / Verification Officers", "Review queued documents, inspect metadata, update workflow status with notes."],
            ["3", "Fraud Investigators (SIU)", "Receive high-risk fraud alerts (risk score &ge; 70%) and quarantine fraudulent files."],
            ["4", "DevOps Engineers", "Automate CI/CD pipelines, container images, test suites, and target node provisioning."]
        ], [20, 140, 344]),
        Spacer(1, 6),
        Paragraph("4. Measurable Success Criteria", S['h2']),
        make_table([
            ["#", "Criteria", "Target Benchmark"],
            ["1", "Automated Intake & Triage Time", "Under 2 seconds per document"],
            ["2", "Fraud Detection Accuracy", "100% of documents with risk score &ge; 70% flagged"],
            ["3", "System Availability & Uptime", "99.9% uptime during testing cycles"],
            ["4", "CI/CD Deployment Cycle", "Under 3 minutes from commit to running container"],
            ["5", "Automated Test Coverage", "100% pass rate across 6 critical user journeys"]
        ], [20, 200, 284])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 2. Scope
def build_scope(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Approved MVP Scope & Objectives", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Core 5 MVP Features Frozen Scope", S['h2']),
        Paragraph("<b>1. Document Intake / Event Entry:</b> Interactive submission modal and REST endpoint (/api/documents) capturing policy number, claimant name, document type, and claim amount.", S['body']),
        Paragraph("<b>2. Searchable Registry Dashboard:</b> Real-time filterable grid enabling multi-field search and status filtering (Submitted, Under Review, Verified, Flagged Fraud, Rejected).", S['body']),
        Paragraph("<b>3. Summary KPI Indicators:</b> Live statistical cards tracking Total Submissions, Verified rate, Under Review count, Flagged Fraud incidents, and Claim volume.", S['body']),
        Paragraph("<b>4. Underwriter Status Drill-Down:</b> Inspection modal for underwriting officers to inspect confidence scores, record remarks, and progress workflow state.", S['body']),
        Paragraph("<b>5. Automated Risk Scoring & Fraud Alerts:</b> Automated heuristic risk scoring engine highlighting suspicious documents (risk score &ge; 70%) with immediate visual banners.", S['body']),
        Spacer(1, 6),
        Paragraph("2. 15-Task Milestone Breakdown", S['h2']),
        make_table([
            ["Task ID", "DevOps Milestone Scope Summary"],
            ["Task 01", "Problem definition, stakeholder analysis, objectives, constraints, MVP scope freeze"],
            ["Task 02", "User stories, product backlog, 15-task Kanban plan, Definition of Done, DevOps lifecycle diagram"],
            ["Task 03", "SRS summary, UML use-case diagram, 3-tier architecture diagram, REST API list, local setup"],
            ["Task 04", "Git repo setup, README, .gitignore, branch policy, issue templates, initial commit skeleton"],
            ["Task 05", "Feature branch (feature/document-intake), commits, pull request, peer review, merge to develop"],
            ["Task 06", "Complete MVP, second feature branch, merge conflict creation and resolution, tagging v1.0"],
            ["Task 07", "Jenkins installation, Freestyle CI job with SCM polling, Maven build, artifact archiving"],
            ["Task 08", "Declarative Jenkinsfile pipeline with parameterized environments (DEPLOY_ENV, APP_PORT)"],
            ["Task 09", "Selenium test suite with 6 critical user journeys, assertions, and screenshot capture"],
            ["Task 10", "Jenkins continuous testing quality gate, deliberate defect injection, build failure & fix rerun"],
            ["Task 11", "Multi-stage Dockerfile, container image build, port mapping, and full lifecycle execution"],
            ["Task 12", "Jenkins-Docker CD pipeline: automated build, Docker Hub tagging, and containerized deployment"],
            ["Task 13", "Configuration management spec, Ansible inventory, and YAML playbook for target provisioning"],
            ["Task 14", "Target provisioning, idempotency proof (changed=0), HTTP health check, and rollback demo"],
            ["Task 15", "Comprehensive technical report, presentation guide, viva defense Q&A, and master documentation"]
        ], [80, 424])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 3. Stakeholders
def build_stakeholders(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Stakeholder Analysis Matrix", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Stakeholder Classification & Expectations", S['h2']),
        make_table([
            ["Stakeholder Group", "Key Responsibilities", "Primary Value Expected", "Impact"],
            ["Policyholders", "Submit genuine claims & policy proofs.", "Fast verification; rapid payouts.", "High"],
            ["Underwriters", "Validate records, review notes, progress status.", "Automated pre-screening & risk scores.", "High"],
            ["Fraud Officers (SIU)", "Investigate high-risk anomalies (&ge; 70%).", "Instant alert triggers & audit trails.", "High"],
            ["TPAs & Hospitals", "Issue bills, discharge summaries, reports.", "Direct integration & fast turnaround.", "Med"],
            ["Insurance Regulators", "Establish compliance rules & SLAs.", "Data privacy & immutable audit logs.", "High"],
            ["DevOps Engineers", "Manage CI/CD pipelines & containers.", "Idempotent deploys & zero downtime.", "High"]
        ], [90, 140, 204, 70]),
        Spacer(1, 8),
        Paragraph("2. Governance & Communication Channels", S['h2']),
        Paragraph("• <b>Real-Time Alerts:</b> Automated visual banners alerting underwriter leads within 2 seconds of high-risk detection.", S['bullet']),
        Paragraph("• <b>Underwriter Audit Records:</b> Every status transition logs reviewer identity, timestamp, and notes.", S['bullet']),
        Paragraph("• <b>DevOps Telemetry:</b> Automated Jenkins build consoles and Docker container health endpoints.", S['bullet'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 4. User Stories
def build_user_stories(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Agile User Stories & Acceptance Criteria", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("User Story 1: Real-Time Verification Registry & KPIs", S['h2']),
        Paragraph("<b>As an</b> Underwriting Officer, <b>I want to</b> view a real-time dashboard displaying key verification metrics and document listings, <b>So that</b> I can instantly understand processing backlogs.", S['body']),
        Paragraph("<i>Acceptance Criteria:</i> Dashboard renders within 1.5 seconds displaying Total Documents, Verified Count, Under Review Count, and Flagged Fraud Count with colored risk bars.", S['body']),
        Spacer(1, 4),
        Paragraph("User Story 2: High-Risk Fraud Alert Trigger", S['h2']),
        Paragraph("<b>As a</b> Fraud Investigator, <b>I want to</b> be automatically alerted when an ingested document has a risk score &ge; 70%, <b>So that</b> I can intercept forged claims before approval.", S['body']),
        Paragraph("<i>Acceptance Criteria:</i> System displays prominent warning banner when high-risk documents are present; clicking banner filters registry to flagged fraud cases.", S['body']),
        Spacer(1, 4),
        Paragraph("User Story 3: Digital Document Intake & Registration", S['h2']),
        Paragraph("<b>As a</b> Policyholder or Intake Clerk, <b>I want to</b> submit new insurance document details via a web modal, <b>So that</b> the document enters the verification pipeline.", S['body']),
        Paragraph("<i>Acceptance Criteria:</i> Modal validates Policy Number, Claimant Name, and Claim Amount; system generates sequential ID (DOC-2026-XXXX) and persists to H2 database.", S['body']),
        Spacer(1, 4),
        Paragraph("User Story 4: Search & Multi-Status Filtering", S['h2']),
        Paragraph("<b>As an</b> Underwriter, <b>I want to</b> search documents by policy number or claimant name and filter by status, <b>So that</b> I can locate specific customer claim records immediately.", S['body']),
        Paragraph("<i>Acceptance Criteria:</i> Instant search on keystroke input; status dropdown filters by SUBMITTED, UNDER_REVIEW, VERIFIED, FLAGGED_FRAUD, and REJECTED.", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 5. Backlog
def build_backlog(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Product Backlog & Kanban Task Board", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Prioritized Product Backlog", S['h2']),
        make_table([
            ["ID", "Feature / User Story Description", "Priority", "Points", "Sprint", "Status"],
            ["PB-01", "Spring Boot 3.2 skeleton, Maven pom.xml, H2 database", "Must Have", "5", "Sprint 1", "Completed"],
            ["PB-02", "JPA entity InsuranceDocument, repository, seed data", "Must Have", "5", "Sprint 1", "Completed"],
            ["PB-03", "REST endpoints for /documents, /alerts, /summary", "Must Have", "8", "Sprint 1", "Completed"],
            ["PB-04", "Responsive single-page web dashboard with KPI cards", "Must Have", "8", "Sprint 1", "Completed"],
            ["PB-05", "Document intake modal form with validation", "Must Have", "5", "Sprint 1", "Completed"],
            ["PB-06", "Search and multi-status filter toolbar", "Must Have", "3", "Sprint 2", "Completed"],
            ["PB-07", "Underwriter inspection modal with status transitions", "Must Have", "5", "Sprint 2", "Completed"],
            ["PB-08", "Automated fraud scoring, risk meter, alert banner", "Must Have", "5", "Sprint 2", "Completed"],
            ["PB-09", "GitFlow branching, PR workflow, merge conflict demo", "Must Have", "5", "Sprint 2", "Completed"],
            ["PB-10", "Jenkins Freestyle CI job with SCM polling", "Must Have", "8", "Sprint 2", "Completed"],
            ["PB-11", "Declarative Jenkinsfile pipeline with parameters", "Must Have", "8", "Sprint 3", "Completed"],
            ["PB-12", "Selenium & JUnit test suite covering 6 CUJs", "Must Have", "8", "Sprint 3", "Completed"],
            ["PB-13", "Quality gate aborting deployment on defect detection", "Must Have", "5", "Sprint 3", "Completed"],
            ["PB-14", "Alpine JRE Dockerfile & container lifecycle validation", "Must Have", "8", "Sprint 3", "Completed"],
            ["PB-15", "Ansible inventory & playbook for target provisioning", "Must Have", "8", "Sprint 3", "Completed"]
        ], [35, 230, 60, 40, 55, 60]),
        Spacer(1, 6),
        Paragraph("2. Definition of Done (DoD) Summary", S['h2']),
        Paragraph("All 15 tasks adhere to strict DoD: zero compilation errors, 100% test pass rate, peer-reviewed Git merge, successful Docker health probe, and verified Ansible idempotency.", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 6. Sprint Plan
def build_sprint_plan(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Sprint Execution Plan (3 Sprints)", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("Sprint 1: Architecture, Core MVP & Git Branching (Tasks 01 – 06)", S['h2']),
        Paragraph("• <b>Scope:</b> Project initialization, Spring Boot 3.2 skeleton, JPA entities, REST APIs, responsive web dashboard, GitFlow branching, Pull Requests, merge conflict resolution, and release baseline tagging v1.0.", S['body']),
        Paragraph("• <b>Deliverables:</b> Functional local application running on port 8085 with 5 core MVP features and tagged Git history.", S['body']),
        Spacer(1, 4),
        Paragraph("Sprint 2: Continuous Integration & Automated Testing (Tasks 07 – 10)", S['h2']),
        Paragraph("• <b>Scope:</b> Jenkins server setup, JDK 21 / Maven 3.9 configuration, Freestyle CI job with SCM polling, declarative Jenkinsfile pipeline, Selenium WebDriver test suite, quality gate defect injection, and recovery.", S['body']),
        Paragraph("• <b>Deliverables:</b> Configured Jenkins pipeline, archived artifacts, Surefire JUnit XML reports, defect correction proof.", S['body']),
        Spacer(1, 4),
        Paragraph("Sprint 3: Containerization & Ansible IaC (Tasks 11 – 15)", S['h2']),
        Paragraph("• <b>Scope:</b> Multi-stage Alpine JRE Dockerfile, container lifecycle testing, Jenkins-Docker continuous deployment, Ansible inventory and setup.yml playbook, idempotency proof, and final technical report compilation.", S['body']),
        Paragraph("• <b>Deliverables:</b> Versioned Docker image, idempotent target provisioning, viva slide deck, and master documentation.", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 7. Diagram
def build_diagram(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("DevOps Lifecycle Architecture Diagram", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. End-to-End DevOps Delivery Flow", S['h2']),
        Paragraph("The project operationalizes an automated 8-stage continuous delivery lifecycle:", S['body']),
        Paragraph("1. <b>Plan:</b> Agile product backlog tracking 15 user stories and tasks.", S['bullet']),
        Paragraph("2. <b>Code:</b> Java Spring Boot microservice versioned in Git using GitFlow.", S['bullet']),
        Paragraph("3. <b>Build:</b> Apache Maven cleans, compiles source bytecode, and packages JAR.", S['bullet']),
        Paragraph("4. <b>Test:</b> Selenium and JUnit execute 6 Critical User Journeys acting as quality gate.", S['bullet']),
        Paragraph("5. <b>Package:</b> Standalone executable JAR archived in Jenkins artifact store.", S['bullet']),
        Paragraph("6. <b>Release:</b> Docker container image built, tagged with build number and latest.", S['bullet']),
        Paragraph("7. <b>Deploy:</b> Ansible playbook provisions target node and launches container.", S['bullet']),
        Paragraph("8. <b>Operate & Monitor:</b> Automated HTTP /api/health probes monitor liveness.", S['bullet']),
        Spacer(1, 6),
        Paragraph("2. Architectural Quality Assurance", S['h2']),
        Paragraph("If any test fails during Stage 4, the Jenkins quality gate halts immediately, preventing defective software from ever progressing to packaging or production deployment.", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 8. API List
def build_api_list(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("RESTful API List & Data Specifications", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Complete REST API Catalog", S['h2']),
        make_table([
            ["Method", "Endpoint", "Function & Description", "Status Code"],
            ["GET", "/api/documents", "Retrieve all documents (supports ?status= &search=)", "200 OK"],
            ["GET", "/api/documents/{id}", "Fetch specific document details by numeric ID", "200 OK / 404"],
            ["POST", "/api/documents", "Submit new document; validates & computes risk", "201 Created"],
            ["PUT", "/api/documents/{id}/status", "Update status (VERIFIED, FLAGGED_FRAUD) & notes", "200 OK"],
            ["GET", "/api/alerts", "Retrieve high-risk fraud alerts (risk score &ge; 70%)", "200 OK"],
            ["GET", "/api/summary", "Retrieve aggregated KPI summary statistics", "200 OK"],
            ["POST", "/api/simulate", "Trigger automated OCR risk scoring simulation", "200 OK"],
            ["GET", "/api/health", "Microservice health probe returning status & metadata", "200 OK"]
        ], [55, 140, 225, 84]),
        Spacer(1, 6),
        Paragraph("2. Data Model: InsuranceDocument", S['h2']),
        Paragraph("Fields: <code>id</code> (BIGINT), <code>documentNumber</code> (VARCHAR), <code>policyNumber</code> (VARCHAR), <code>claimantName</code> (VARCHAR), <code>documentType</code> (VARCHAR), <code>verificationStatus</code> (VARCHAR), <code>riskScore</code> (INT), <code>authenticityConfidence</code> (DOUBLE), <code>claimAmount</code> (DOUBLE), <code>reviewerNotes</code> (VARCHAR), <code>submissionDate</code> (TIMESTAMP).", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 9. Architecture Diagram
def build_architecture_diagram(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("3-Tier System Architecture Design", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Architectural Overview", S['h2']),
        Paragraph("The portal is designed as a cloud-native 3-tier microservice:", S['body']),
        Paragraph("• <b>Tier 1: Presentation Layer:</b> Single-page responsive web dashboard (index.html) with CSS custom properties, KPI summary cards, filter bars, and underwriter audit modals.", S['body']),
        Paragraph("• <b>Tier 2: Business & Application Layer:</b> Spring Boot 3.2 REST controllers (DocumentApiController) providing validation, heuristic fraud scoring, and workflow state management.", S['body']),
        Paragraph("• <b>Tier 3: Persistence Layer:</b> Spring Data JPA repository backed by an embedded H2 relational database ensuring zero-dependency local execution.", S['body']),
        Paragraph("• <b>Tier 4: DevOps & Infrastructure Layer:</b> Production Alpine JRE Docker container (port 8085), Jenkins CI/CD pipeline (port 8080), and Ansible configuration playbooks.", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 10. Local Setup Guide
def build_local_setup_guide(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Local Development Setup Guide", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Prerequisites & Toolchains", S['h2']),
        Paragraph("Ensure Java JDK 17, 21, or 23, Apache Maven 3.8+, and Docker Desktop are installed on the local workstation.", S['body']),
        Spacer(1, 4),
        Paragraph("2. Build and Execution Steps", S['h2']),
        Paragraph("<b>Clone Repository:</b><br/><code>git clone https://github.com/sourabhshelke/insurance-document-verification-portal.git</code>", S['body']),
        Paragraph("<b>Compile & Run Application:</b><br/><code>mvn clean spring-boot:run</code>", S['body']),
        Paragraph("<b>Access Interactive Endpoints:</b><br/>• Portal UI: http://localhost:8085<br/>• Health Check: http://localhost:8085/api/health<br/>• H2 Database Console: http://localhost:8085/h2-console", S['body']),
        Paragraph("<b>Execute Automated Tests:</b><br/><code>mvn test</code>", S['body'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 11. SRS Summary
def build_srs_summary(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Software Requirements Specification (SRS) Summary", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Functional Requirements (FR)", S['h2']),
        Paragraph("• <b>FR-01 (Intake):</b> Ingest document metadata and generate formatted unique IDs (DOC-2026-XXXX).", S['bullet']),
        Paragraph("• <b>FR-02 (Search):</b> Provide real-time keystroke search and multi-status filtering toolbar.", S['bullet']),
        Paragraph("• <b>FR-03 (Summary KPIs):</b> Calculate live metrics for Total, Verified, Under Review, and Flagged counts.", S['bullet']),
        Paragraph("• <b>FR-04 (Fraud Engine):</b> Automatically quarantine records with risk score &ge; 70% as FLAGGED_FRAUD.", S['bullet']),
        Paragraph("• <b>FR-05 (Underwriting):</b> Enable underwriter inspection, status transition, and audit notes logging.", S['bullet']),
        Spacer(1, 4),
        Paragraph("2. Non-Functional Requirements (NFR)", S['h2']),
        Paragraph("• <b>NFR-01 (Performance):</b> Sub-second REST response times and UI load time under 1.5 seconds.", S['bullet']),
        Paragraph("• <b>NFR-02 (Portability):</b> Packaged in self-contained Alpine JRE Docker container on port 8085.", S['bullet']),
        Paragraph("• <b>NFR-03 (Reliability):</b> Liveness/readiness health probes reporting application status.", S['bullet']),
        Paragraph("• <b>NFR-04 (Quality):</b> Automated test suite covering 6 critical user journeys with 100% pass rate.", S['bullet'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 12. Branch Policy
def build_branch_policy(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Git Branching Strategy & Contribution Policy", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. GitFlow Branch Structure", S['h2']),
        Paragraph("• <b>main:</b> Production-ready code. Locked against direct commits; tagged with releases (e.g. v1.0).", S['bullet']),
        Paragraph("• <b>develop:</b> Integration branch for ongoing feature aggregation.", S['bullet']),
        Paragraph("• <b>feature/*:</b> Isolated branches for individual user stories (e.g. feature/document-intake).", S['bullet']),
        Paragraph("• <b>hotfix/*:</b> Critical production patch branches originating from main.", S['bullet']),
        Spacer(1, 4),
        Paragraph("2. Pull Request & Quality Policies", S['h2']),
        Paragraph("• Direct pushes to main and develop are strictly prohibited.", S['bullet']),
        Paragraph("• PRs require at least one peer code review before merge approval.", S['bullet']),
        Paragraph("• All automated tests must pass before merging.", S['bullet']),
        Paragraph("• Merge conflicts must be resolved manually preserving strict compliance rules.", S['bullet'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 13. URL Document
def build_url_doc(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Git Repository URL & Metadata", S['h1']),
        Paragraph(f"Student: <b>{STUDENT_NAME}</b> | Roll No: <b>{ROLL_NO}</b> | Class: <b>{CLASS_NAME}</b>", S['meta']),
        Spacer(1, 6),
        Paragraph("1. Repository Coordinates", S['h2']),
        Paragraph("• <b>Repository Name:</b> insurance-document-verification-portal", S['bullet']),
        Paragraph("• <b>GitHub URL:</b> https://github.com/sourabhshelke/insurance-document-verification-portal", S['bullet']),
        Paragraph("• <b>Default Production Branch:</b> main", S['bullet']),
        Paragraph("• <b>Active Integration Branch:</b> develop", S['bullet']),
        Paragraph("• <b>Release Version Baseline:</b> v1.0 (annotated Git tag)", S['bullet']),
        Spacer(1, 4),
        Paragraph("2. Active GitHub Issues", S['h2']),
        Paragraph("• Issue #1: [FEATURE] Implement document intake REST API and web modal for policyholders", S['bullet']),
        Paragraph("• Issue #2: [FEATURE] Create underwriter drill-down modal with status progression workflow", S['bullet']),
        Paragraph("• Issue #3: [BUG] Fix automated fraud scoring threshold comparison for duplicate medical bills", S['bullet']),
        Paragraph("• Issue #4: [CI/CD] Implement multi-stage Jenkinsfile with automated quality gate and Docker CD", S['bullet']),
        Paragraph("• Issue #5: [CONFIG] Create Ansible playbook for idempotent provisioning of target host", S['bullet'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# 14. Master Document (Main_Doc.pdf)
def build_main_doc(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=64, bottomMargin=54)
    S = get_base_styles()
    story = [
        Paragraph("Containerized Insurance Document Verification Portal", S['h1']),
        Paragraph(f"Master DevOps Project Technical Report & Portfolio (Academic Year {ACADEMIC_YEAR})", S['h2']),
        Paragraph(f"Candidate: <b>{STUDENT_NAME}</b> | Roll Number: <b>{ROLL_NO}</b><br/>Class: <b>{CLASS_NAME}</b> | Institute: <b>{INSTITUTE}</b>", S['meta']),
        Spacer(1, 8),
        Paragraph("1. Executive Summary", S['h2']),
        Paragraph("The Containerized Insurance Document Verification Portal is a production-grade enterprise microservice designed to automate the intake, validation, heuristic risk assessment, and fraud detection of insurance claim documents. Operating on a modern cloud-native stack (Java 21, Spring Boot 3.2, Maven, Selenium, Jenkins, Docker, Ansible), the system eliminates manual verification delays and prevents fraudulent payouts.", S['body']),
        Spacer(1, 4),
        Paragraph("2. Technology Stack & DevOps Toolchain", S['h2']),
        make_table([
            ["Layer", "Tool / Framework", "Purpose & Role in Project"],
            ["Backend", "Java 21 / Spring Boot 3.2", "Core business logic, REST controllers, JPA data access"],
            ["Database", "Embedded H2 Database", "In-memory relational persistence with web console"],
            ["Frontend", "HTML5 / CSS3 / Vanilla JS", "Responsive portal with live KPI analytics & audit modals"],
            ["Build Tool", "Apache Maven 3.9", "Dependency management, bytecode compilation, fat JAR assembly"],
            ["Version Control", "Git & GitHub", "GitFlow branching, PR reviews, conflict resolution, tagging v1.0"],
            ["CI Server", "Jenkins Automation Server", "Freestyle CI job, SCM polling, declarative Jenkinsfile pipeline"],
            ["Automated Testing", "Selenium WebDriver & JUnit", "6 Critical user journey tests acting as CI quality gate"],
            ["Containers", "Docker & Alpine JRE", "Lightweight container image, port 8085 binding, lifecycle testing"],
            ["Config Management", "Ansible Playbooks", "Automated target node provisioning and idempotent execution"]
        ], [90, 140, 274]),
        PageBreak(),
        Paragraph("3. Summary of 15 Completed DevOps Tasks", S['h2']),
        make_table([
            ["Task ID", "Milestone Summary", "Verified Deliverable"],
            ["Task 01", "Problem definition, stakeholders, scope freeze", "Problem_Statement.md, Scope.md, Stakeholders.md"],
            ["Task 02", "User stories, backlog, sprint plan, DoD, diagram", "User_Stories.md, Backlog.md, Sprint_Plan.md, Diagram.md"],
            ["Task 03", "SRS summary, architecture, REST API list, setup", "srs_summary.md, architecture_diagram.md, API_List.md"],
            ["Task 04", "Git repo init, README, .gitignore, branch policy", "branch_policy.md, url.md, git_init_evidence.md"],
            ["Task 05", "Feature branch (doc intake), PR, review, merge", "feature_branch_workflow.md, pr_review_evidence.md"],
            ["Task 06", "MVP completion, merge conflict resolution, v1.0", "merge_conflict_resolution.md, tag_evidence.md (v1.0)"],
            ["Task 07", "Jenkins installation, Freestyle CI job, artifacts", "jenkins_ci_guide.md, build_console_log.txt"],
            ["Task 08", "Declarative Jenkinsfile pipeline with parameters", "pipeline_doc.md, pipeline_execution_log.txt"],
            ["Task 09", "Selenium test suite with 6 CUJs & screenshot tool", "test_plan.md, test_execution_report.md"],
            ["Task 10", "Jenkins continuous testing gate, defect fix rerun", "quality_gate_docs.md, defect_and_fix_evidence.md"],
            ["Task 11", "Docker container lifecycle & Alpine JRE image", "docker_commands.md, container_lifecycle_log.txt"],
            ["Task 12", "Jenkins-Docker CD commit-to-container pipeline", "docker_cd_pipeline.md, cd_pipeline_log.txt"],
            ["Task 13", "Ansible inventory & playbook for server config", "config_spec.md, inventory.ini, setup.yml"],
            ["Task 14", "Automated provisioning, idempotency, rollback demo", "idempotency_validation.md, rollback_demo.md"],
            ["Task 15", "Technical report, viva presentation guide, master doc", "final_technical_report.md, viva_presentation_guide.md"]
        ], [55, 235, 214]),
        Spacer(1, 8),
        Paragraph("4. Key Results & Viva Preparedness", S['h2']),
        Paragraph("• <b>Processing Speed:</b> Automated intake and fraud assessment in under 200 ms.", S['bullet']),
        Paragraph("• <b>Quality Gate:</b> 100% test pass rate across all 6 critical user journeys; defective code automatically halted.", S['bullet']),
        Paragraph("• <b>Continuous Delivery:</b> Full commit-to-container pipeline executes in under 3 minutes.", S['bullet']),
        Paragraph("• <b>Idempotent Provisioning:</b> Ansible playbook produces changed=0 on subsequent executions.", S['bullet'])
    ]
    doc.build(story, canvasmaker=NumberedCanvas)

# Main generation routine
if __name__ == '__main__':
    base_dir = r"c:\Users\ACER\OneDrive\Desktop\devops"
    
    print("Building Task-01 PDFs...")
    build_problem_statement(os.path.join(base_dir, "Task-01", "Problem_Statement.pdf"))
    build_scope(os.path.join(base_dir, "Task-01", "Scope.pdf"))
    build_stakeholders(os.path.join(base_dir, "Task-01", "Stakeholders.pdf"))
    
    print("Building Task-02 PDFs...")
    build_user_stories(os.path.join(base_dir, "Task-02", "User_Stories.pdf"))
    build_backlog(os.path.join(base_dir, "Task-02", "Backlog.pdf"))
    build_sprint_plan(os.path.join(base_dir, "Task-02", "Sprint_Plan.pdf"))
    build_diagram(os.path.join(base_dir, "Task-02", "Diagram.pdf"))
    
    print("Building Task-03 PDFs...")
    build_api_list(os.path.join(base_dir, "Task-03", "API_List.pdf"))
    build_architecture_diagram(os.path.join(base_dir, "Task-03", "architecture_diagram.pdf"))
    build_local_setup_guide(os.path.join(base_dir, "Task-03", "local_setup_guide.pdf"))
    build_srs_summary(os.path.join(base_dir, "Task-03", "srs_summary.pdf"))
    
    print("Building Task-04 PDFs...")
    build_branch_policy(os.path.join(base_dir, "Task-04", "branch_policy.pdf"))
    build_url_doc(os.path.join(base_dir, "Task-04", "url.pdf"))
    
    print("Building Main_Doc.pdf...")
    build_main_doc(os.path.join(base_dir, "Main_Doc.pdf"))
    
    print("ALL 14 PDFs COMPILED SUCCESSFULLY!")
