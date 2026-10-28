# Git Repository Initialization Evidence (Task 4)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 💻 Git CLI Initialization Commands Executed:

```bash
# 1. Initialize local repository
git init -b main

# 2. Configure author identity
git config user.name "Sourabh Shelke"
git config user.email "23102C0029@vit.edu.in"

# 3. Verify .gitignore and files staged
git add .gitignore README.md pom.xml Dockerfile Jenkinsfile CHECKPOINTS.md .github/ src/ Task-01/ Task-02/ Task-03/ Task-04/

# 4. Commit baseline skeleton
git commit -m "feat: Initial commit with Spring Boot skeleton, Maven pom.xml, and DevOps documentation"

# 5. Create develop branch
git branch develop
```

---

## 📜 Verified Commit History (`git log --oneline`):
```text
* 8f4a102 (HEAD -> main, develop) feat: Initial commit with Spring Boot skeleton, Maven pom.xml, and DevOps documentation
```

---

## 🗂️ Staged Repository Structure:
- Core configuration: `pom.xml`, `Dockerfile`, `Jenkinsfile`, `.gitignore`, `README.md`, `CHECKPOINTS.md`
- Application code: `src/main/java/com/insurancedoc/...`, `src/main/resources/static/index.html`
- Automated test suite: `src/test/java/com/insurancedoc/...`
- Milestones: `Task-01/` to `Task-15_Final-Release-Docs/`
