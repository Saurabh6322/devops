# Automated Provisioning & Idempotency Validation (Task 14)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🔁 1. Understanding & Demonstrating Idempotency

### What is Idempotency?
**Idempotency** is a foundational principle of Infrastructure as Code (IaC). An operation is idempotent if executing it multiple times produces the exact same end state as executing it once, without making unintended changes or breaking the environment.

---

### Execution Run 1: Initial Provisioning (State Changes Applied)
```bash
ansible-playbook -i inventory.ini setup.yml
```

**Terminal Output:**
```text
PLAY [Provision and Deploy Containerized Insurance Document Verification Portal] **********
TASK [Ensure required deployment directories exist with correct permissions] **************
changed: [localhost]
TASK [Verify Docker service is active and enabled] ****************************************
ok: [localhost]
TASK [Run Containerized Insurance Verification Portal] ************************************
changed: [localhost]
TASK [Wait for application HTTP health endpoint to return UP] *****************************
ok: [localhost]

PLAY RECAP ********************************************************************************
localhost                  : ok=7    changed=2    unreachable=0    failed=0
```
*Result:* 2 items were modified (`changed=2`) as directories were created and container was launched.

---

### Execution Run 2: Idempotent Re-Execution (Zero Changes Applied)
```bash
ansible-playbook -i inventory.ini setup.yml
```

**Terminal Output:**
```text
PLAY [Provision and Deploy Containerized Insurance Document Verification Portal] **********
TASK [Ensure required deployment directories exist with correct permissions] **************
ok: [localhost]
TASK [Verify Docker service is active and enabled] ****************************************
ok: [localhost]
TASK [Run Containerized Insurance Verification Portal] ************************************
ok: [localhost]
TASK [Wait for application HTTP health endpoint to return UP] *****************************
ok: [localhost]

PLAY RECAP ********************************************************************************
localhost                  : ok=7    changed=0    unreachable=0    failed=0
```
*Result:* **`changed=0`**! The Ansible engine detects that all desired states are already satisfied, proving $100\%$ idempotency.
