# Git Branching Strategy & Contribution Policy

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🌿 1. GitFlow Branching Model

Our team follows an industry-standard **GitFlow** branching strategy tailored for automated CI/CD:

```
main (Production Releases) ───────● [v1.0] ───────────────────────● [v1.1]
                                 /                               /
develop (Integration) ──────────●────────●────────●────────●────●
                               /        /          \      /
feature/* ────────────────────●────────●            ●────● (Conflict Resolved)
                        feature/doc-intake     feature/fraud-detection
```

---

## 📌 2. Branch Hierarchy & Conventions

| Branch Name | Purpose & Stability Level | Direct Push Allowed? | CI/CD Action Triggered |
|:------------|:--------------------------|:---------------------|:-----------------------|
| `main` | Production-ready, stable releases. Tagged with version numbers (e.g. `v1.0`). | NO (PR with 1 review required) | Automated container release build & Docker deployment |
| `develop` | Integration branch for aggregating tested features. | NO (PR from feature branch) | Automated build & quality gate test suite execution |
| `feature/<name>` | Independent branch for building isolated features (e.g. `feature/document-intake`). | YES (by feature author) | Local Maven tests & PR validation |
| `hotfix/<name>` | Urgent production bug fixes branching directly from `main`. | NO (Emergency PR) | Immediate build & patch deployment |

---

## 💬 3. Git Commit Message Standards
Commits must follow the **Conventional Commits** specification:
- `feat: <description>` — A new feature (e.g., `feat: Add underwriter review modal`)
- `fix: <description>` — A bug fix (e.g., `fix: Correct fraud threshold comparison`)
- `docs: <description>` — Documentation updates (e.g., `docs: Add API specification`)
- `ci: <description>` — Changes to CI/CD files (e.g., `ci: Add Docker packaging stage to Jenkinsfile`)
- `test: <description>` — Adding or modifying automated tests (e.g., `test: Add CUJ-3 Selenium test case`)

