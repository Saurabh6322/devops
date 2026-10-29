# Continuous Testing Quality Gate Specification (Task 10)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🛡️ 1. Jenkins Quality Gate Concept & Mechanism
In a modern DevOps pipeline, automated tests serve as an unyielding **Quality Gate**. If any regression or defect causes even a single unit or integration test assertion to fail:
1. Maven exits with a non-zero status code (`ERRORLEVEL != 0`).
2. Jenkins immediately flags the `Automated Tests` stage as **FAILED** (Red).
3. The pipeline halts instantly, aborting downstream `Package Artifact`, `Docker Build`, and `Deploy Application` stages.
4. Defective code is prevented from contaminating staging and production environments.

---

## ⚙️ 2. Jenkinsfile Quality Gate Configuration

```groovy
stage('Automated Tests') {
    steps {
        echo 'Executing JUnit & Selenium test suite (Quality Gate)...'
        bat 'mvn test'
    }
    post {
        always {
            // Publishes XML test results regardless of pass or fail
            junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'
        }
        failure {
            echo 'Quality Gate Failed: One or more critical user journey tests failed! Halting pipeline.'
        }
    }
}
```

