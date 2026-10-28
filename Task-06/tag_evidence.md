# Release Baseline Tagging Evidence — v1.0 (Task 6)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🏷️ 1. Git Release Tag Execution

Following the successful completion of the MVP, resolution of merge conflicts, and validation of all automated tests, the integration branch was merged into `main` and tagged with annotated release version `v1.0`:

```bash
# Switch to main branch
git checkout main

# Merge integration branch
git merge develop --no-ff -m "Release: Merge develop into main for MVP Release v1.0"

# Create annotated release tag
git tag -a v1.0 -m "Release v1.0: Complete Insurance Document Verification Portal MVP baseline"

# Verify tag details
git show v1.0
```

---

## 📜 2. Tag Verification Output (`git show v1.0`)

```text
tag v1.0
Tagger: Sourabh Shelke <23102C0029@vit.edu.in>
Date:   Wed Oct 28 14:00:00 2026 +0530

Release v1.0: Complete Insurance Document Verification Portal MVP baseline

commit 7c189b2 (HEAD -> main, tag: v1.0)
Merge: 8f4a102 e429a17
Author: Sourabh Shelke <23102C0029@vit.edu.in>
Date:   Wed Oct 28 14:00:00 2026 +0530

    Release: Merge develop into main for MVP Release v1.0
```

---

## 🚀 3. Status Baseline
- Release baseline `v1.0` locked and ready for automated Jenkins CI/CD pipeline triggers.
- Codebase contains zero unmerged conflict markers.
