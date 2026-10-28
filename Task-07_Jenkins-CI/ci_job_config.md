# Jenkins Freestyle Job Specification (Task 7)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 📋 XML Configuration Summary for `insurance-verification-ci`

```xml
<project>
  <actions/>
  <description>Automated CI build job for Containerized Insurance Document Verification Portal</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.plugins.git.GitSCM">
    <configVersion>2</configVersion>
    <userRemoteConfigs>
      <hudson.plugins.git.UserRemoteConfig>
        <url>https://github.com/sourabhshelke/insurance-document-verification-portal.git</url>
      </hudson.plugins.git.UserRemoteConfig>
    </userRemoteConfigs>
    <branches>
      <hudson.plugins.git.BranchSpec>
        <name>*/main</name>
      </hudson.plugins.git.BranchSpec>
    </branches>
  </scm>
  <triggers>
    <hudson.triggers.SCMTrigger>
      <spec>H/5 * * * *</spec>
    </hudson.triggers.SCMTrigger>
  </triggers>
  <builders>
    <hudson.tasks.Maven>
      <targets>clean package</targets>
      <mavenName>Maven 3.9</mavenName>
      <usePrivateRepository>false</usePrivateRepository>
    </hudson.tasks.Maven>
  </builders>
  <publishers>
    <hudson.tasks.ArtifactArchiver>
      <artifacts>target/*.jar</artifacts>
      <allowEmptyArchive>false</allowEmptyArchive>
      <fingerprint>true</fingerprint>
      <onlyIfSuccessful>true</onlyIfSuccessful>
    </hudson.tasks.ArtifactArchiver>
    <hudson.tasks.junit.JUnitResultArchiver>
      <testResults>target/surefire-reports/*.xml</testResults>
    </hudson.tasks.junit.JUnitResultArchiver>
  </publishers>
</project>
```
