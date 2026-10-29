# System Architecture & Component Design — Insurance Verification Portal

**Project:** Containerized Insurance Document Verification Portal  
**Student:** Sourabh Shelke | **Roll No:** 23102C0029 | **Class:** BE CMPN  
**Subject:** DevOps Project (Academic Year 2026-27)  

---

## 🏛️ 3-Tier Layered Architecture

```mermaid
flowchart TD
    subgraph Presentation_Tier ["1. Presentation Layer (Frontend UI)"]
        UI1[Responsive Single Page App - index.html]
        UI2[Summary KPI Analytics Cards]
        UI3[Search & Multi-Status Filter Bar]
        UI4[Document Submission & Audit Modals]
    end

    subgraph Application_Tier ["2. Application & Business Layer (Spring Boot Microservice)"]
        C1[DocumentApiController - REST Endpoints]
        C2[Validation & Heuristic Fraud Engine]
        C3[Risk Scoring & Status Progression Logic]
        C4[Microservice Health Probe Service]
    end

    subgraph Data_Tier ["3. Data Persistence Layer (In-Memory Database)"]
        D1[Spring Data JPA - DocumentRepository]
        D2[In-Memory H2 Relational Database]
        D3[H2 Web Console /h2-console]
    end

    subgraph DevOps_Environment ["4. Deployment & Infrastructure Layer"]
        DOC[Docker Container - Alpine JRE :8085]
        JENK[Jenkins CI/CD Automation Server :8080]
        ANS[Ansible Configuration Management & Idempotency]
    end

    Presentation_Tier <-->|JSON over HTTP / REST| Application_Tier
    Application_Tier <-->|Hibernate / JPA ORM| Data_Tier
    DevOps_Environment -.->|Build, Test & Provision| Application_Tier
```

---

## 🧩 Architectural Highlights
1. **Separation of Concerns:** Loose coupling between the UI client, REST controllers, domain business logic, and repository layer.
2. **Stateless REST Services:** The Spring Boot backend exposes stateless REST endpoints allowing seamless horizontal scaling inside container clusters.
3. **Embedded Relational Persistence:** Embedded H2 database ensures lightning-fast boot times, zero external setup friction, and high operational reliability during automated tests.
4. **Isolated Microservice Containerization:** The application compiles into an executable fat JAR packaged into a lightweight Alpine Linux Docker container.

