Incident Playbook Case Study
Compass Activity Link W6D3
https://web.compass.lighthouselabs.ca/p/cyber/days/w06d3/activities/3053

-  Company name
- Incident Response Plan
-  Date
-  Table of contents

__Revision History__
|Date|Version|Modification|Modifier|
|-|-|-|-|

- Test & Review Cycle
- Purpose & Scope
- Purpose
- Scope
-  Authority
-  Definitions
-  Identify
-  Response Team 
__Organization Diagram__
```mermaid
graph TD;
  A[CEO]
  B[CTO]
  C[COO]
  D[Security]

  A --> B
  A --> C
  B --> D
```
- Roles (role, definition)
- Responsibilities by role
- Contact information (Role, name, title, #,@)
- External Contacts(Role, Organization, name, title, #,@)
- Other Stakeholder Contact (Role, Organization,name, title, #,@)
- Incident type(Type, Description)
- Severity Matrix

| |2|1|0|
|-|-|-|-|
|2|__H__|H|M|
|1|H|M|L|
|0|M|L|L|

- Incident Handling
- Overview (Diagram) NIST RMF 7 step || NIST IRLC 4 step

```mermaid
graph LR;
  A[preperation];
  B[Detection & Analysis];
  C[Contain,Erradicate,Recovery];
  D[Post-Incident Activity];

  A -->|Policy and Procedures| B;
  B-->C;
  C -->|SOP, Playbooks| B;
  C --> D;
  D -->|implement feedback|A;

  classDef green fill:#d4f1d4,stroke:#0f0,color:#004d00;
  classDef yellow fill:#fffacd,stroke:#ff0,color:#555;
  classDef red fill:#fdd,stroke:#f00,color:#a00;
  classDef blue fill:#e0f7fa,stroke:#00f,color:#00796b;

  linkStyle 4 stroke:#004d00,stroke-width:2px; 

  class B yellow;
  class C red;
  class D blue;
```



- Steps Explanation:
- 1,2,3,4… N
- Playbooks, workflows, SOP
- Approvals
- Incident Response Plan Resposible (Who enforces THIS document)
- Incident Handler
- Refferences
