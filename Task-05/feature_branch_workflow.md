# Feature Development with Branching (Task 5)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🌿 1. Feature Branch Creation & Scope
To implement the first core workflow—**Document Intake & Registration System**—a dedicated feature branch was cut from `develop`:

```bash
# Checkout integration branch and create feature branch
git checkout develop
git checkout -b feature/document-intake
```

### Scope of Feature 1:
1. Created `POST /api/documents` REST endpoint with validation rules.
2. Built interactive Document Submission Modal on the UI.
3. Implemented auto-generation of unique document numbers (`DOC-2026-XXXX`).
4. Added real-time table refresh upon successful document creation.

---

## 💻 2. Git Feature Workflow Log

```bash
# Check modified and newly added files
git status

# Stage feature files
git add src/main/java/com/insurancedoc/controller/DocumentApiController.java
git add src/main/resources/static/index.html

# Commit changes with structured message
git commit -m "feat(intake): Implement document intake modal and POST /api/documents endpoint"

# Push feature branch
git push origin feature/document-intake
```

---

## 📜 Git Log Output on `feature/document-intake`
```text
* 3b19e42 (HEAD -> feature/document-intake) feat(intake): Implement document intake modal and POST /api/documents endpoint
* 8f4a102 (develop, main) feat: Initial commit with Spring Boot skeleton, Maven pom.xml, and DevOps documentation
```

