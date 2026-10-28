# MVP Merge Conflict Creation & Manual Resolution (Task 6)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## ⚡ 1. Demonstration Scenario: Conflict Creation
To demonstrate collaborative Git version control proficiency, a real merge conflict was created between the integration branch `develop` and a second feature branch `feature/fraud-detection-rules`.

Both branches concurrently modified the automated fraud threshold calculation logic inside `InsuranceDocument.java`:

### Changes on `develop`:
```java
// Committed by underwriter lead on develop
public void evaluateRiskAndStatus() {
    if (this.riskScore >= 75) {
        this.verificationStatus = "FLAGGED_FRAUD";
        this.reviewerNotes = "Standard Underwriter Review: Flagged at conservative 75% score.";
    }
}
```

### Changes on `feature/fraud-detection-rules`:
```java
// Committed on feature branch for strict regulatory compliance
public void evaluateRiskAndStatus() {
    if (this.riskScore >= 70) {
        this.verificationStatus = "FLAGGED_FRAUD";
        this.reviewerNotes = "IRDAI Compliance Rule: Stricter 70% threshold enforced.";
    }
}
```

---

## ⚠️ 2. Conflict Appearance
When attempting to merge `feature/fraud-detection-rules` into `develop`:

```bash
git checkout develop
git merge feature/fraud-detection-rules
```

**Git Terminal Output:**
```text
Auto-merging src/main/java/com/insurancedoc/model/InsuranceDocument.java
CONFLICT (content): Merge conflict in src/main/java/com/insurancedoc/model/InsuranceDocument.java
Automatic merge failed; fix conflicts and then commit the result.
```

---

## 🔍 3. Conflict Markers in Code
```text
<<<<<<< HEAD
    if (this.riskScore >= 75) {
        this.verificationStatus = "FLAGGED_FRAUD";
        this.reviewerNotes = "Standard Underwriter Review: Flagged at conservative 75% score.";
    }
=======
    if (this.riskScore >= 70) {
        this.verificationStatus = "FLAGGED_FRAUD";
        this.reviewerNotes = "IRDAI Compliance Rule: Stricter 70% threshold enforced.";
    }
>>>>>>> feature/fraud-detection-rules
```

---

## 🛠️ 4. Manual Resolution Process
The team reviewed both changes and determined that the stricter regulatory standard of $70\%$ is legally mandated to protect against fraudulent claims:

```java
// Resolved code preserving strict threshold and descriptive notes
    if (this.riskScore >= 70) {
        this.verificationStatus = "FLAGGED_FRAUD";
        if (this.reviewerNotes == null || this.reviewerNotes.isEmpty()) {
            this.reviewerNotes = "Automated OCR anomaly detected: High fraud probability score.";
        }
    }
```

```bash
# Mark conflict resolved and finalize merge commit
git add src/main/java/com/insurancedoc/model/InsuranceDocument.java
git commit -m "fix(merge): Resolve merge conflict in fraud evaluation threshold adopting strict 70% cutoff"
```

---

## ✅ 5. Verification
```bash
git status
# Output: On branch develop, nothing to commit, working tree clean
```
Merge conflict successfully resolved while preserving business integrity.
