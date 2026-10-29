# Server Configuration Specification (Ansible) (Task 13)

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🖥️ 1. Target Server Infrastructure Specification
Before the Insurance Document Verification Portal can run on target production nodes, the host environment must be configured with exact prerequisites:

| Component Type | Resource Name | Specification / Parameters | Purpose |
|:---------------|:--------------|:---------------------------|:--------|
| **System Packages** | `docker.io`, `curl`, `git` | Latest stable releases | Container execution engine and health checks |
| **System User** | `appuser` | UID: 1001, GID: `docker`, shell: `/bin/bash` | Non-root principle of least privilege execution |
| **Directories** | `/opt/insurance-verification/` | Mode `0755`, owner `appuser` | Application configuration and data directory |
| | `/var/log/insurance-portal/` | Mode `0755`, owner `appuser` | Operational audit logging directory |
| **Firewall / Ports**| `8085/tcp` | Allowed ingress | Microservice web portal and REST API |
| | `8080/tcp` | Optional ingress | Jenkins CI server access |
| **System Services**| `docker` | State: `started`, enabled on boot | Background daemon for container lifecycle |

---

## 🛠️ 2. Ansible Playbook Design
The configuration is fully codified into an Infrastructure as Code (IaC) Ansible playbook (`setup.yml`) executing against hosts defined in `inventory.ini`.

