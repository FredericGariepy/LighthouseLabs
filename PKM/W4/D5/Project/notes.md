# Menu:
- [Glossary](#glossary)
- [Project deliverables](#deliverables)

##### Diargam/Charts:
- [Case: Group and roles Diagrams](#case-groups-and-roles)
- [Generic: SOC Methodology Diagram:](#soc-methodology-diagram)
##### Resources:
- Google Cloud:  [Top Security Playbooks 2022-2023. Google Cloud](https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf)
- CISA [Federal Government Cybersecurity Incident & Vulnerability Response Playbooks](https://www.cisa.gov/sites/default/files/2024-03/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf)
- NIST [Incident Response](https://csrc.nist.gov/Projects/incident-response)

## Glossary
|term| def|
|-|-|
|Playbook | A documented set of procedures for responding to cybersecurity incidents.|
|SOP| Standard Operating Procedure, Standardized instructions for routine operations in cybersecurity|
|Client Playbook| Tailored guidelines for clients to detect, prevent, and respond to cybersecurity threats.|

## Deliverables

- Technical letter to 3rd party provider

- Non-technical letter to client

- List of trigger items that might affect incident response workflow

- Rationale escalaiton (MSSP); factors that push decision making.
  > At SOC Lvl 1, decision = requesting additional resources and individuals, i.e. escalation.

- Stretch: create a flowchart of your workflow.


Percy F., CEO: Contact IFF item is: escalated, urgent, >= 48 hours unresolved.

## Case groups and roles
Casse Groups and occupied roles:
```
Box Inc.
  │
  ├── CEO: Percy F., Contact IFF item is: escalated, urgent, >= 48 hours unresolved.
  │                  email@: percy@box.cat
  │                  phone#: N/A
  ├── Production
  │      ├── Manager: Misha F. 9AM - 5PM AST
  │      │            email@:  mesha@box.cat Phone 902-9836
  │      │            phone#:  902-9836
  │      │           
  │      └── Manager: Minka F. 5PM - 9AM AST + weekends
  │                   email@:  minka@box.cat
  │                   phone#:  562-7658     
  ├───── IT
  │      ├───── IT support specialist. Lucky:  (assumed 9AM - 5PM AST)
  │      │                             email@: lucky@box.cat
  │      │                             phone#: 269-5466
  │      │
  │      ├───── Network administratot. Ned:    (assumed 9AM - 5PM AST)
  │      │                             email@: ned@box.cat
  │      │                             phone#: 877-4332
  │      │
  │      └───── Database specialist.   Dusty:  (assumed 9AM - 5PM AST)
  │                                    email@: dusty@box.cat
  │                                    phone#: 462-8952
  └──── SOC
         └────── Analyst 1.─────────> YOU:    (assumed Unknown / AST)
                                      email@: SELF@box.cat
                                      phone#: xxx-xxxx 

External MSSP
3rd party
  │
  ├──Consultant: Cat. (assumed 24/7 / AST)
  │              email@:            cat@soc.cat 
  │              Phone# on-site:    905-4616
  │              Phone# Cell#:      902-4321
  ├── ...
  │
  └──SOC
       ├── Analyst 2
       ├── Analyst 2+
       └── ...
```


## SOC Methodology Diagram:
Source: [SOC Methodology](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D2/workflow.md#the-soc-methodology)
```
SOC-constitution (Justify existence of SOC & SOC position in organization)
  │
  └── SOC-Organizational_Handbook (Roles, Responsibility, Org. structure, glossary)
      │
      ├── SOC-EIR_handbook (Alert plans, phone#, email@, d/escalation proceedures)
      │
      ├── SOC-Operational_handbook  (Shift, handover, workflows, tiers, event handling,
      │   │                         intructions, policies, procedures, processes,
      │   ├── Tier_1                timing, forms, SOC dictionary)
      │   ├── Tier_2
      │   └── Tier_2+               Each tier has event handling instructions
      │       └──> send to CSIRT-->-(CSIRT = Last resort)----------------------------->>[Enter : CSIRT framework
      │
      └── SOC-Technical_handbook (Theater setup, SOC desk/apps/infra)
          │
          └── SIEM-Technical_Infrastructure_handbook (Tech info SIEM, use case, alert, threshold)
              ├── Asset_1 
              ├── Asset_2    Each asset has a tech & infra handbook
              └── Asset_3    Each asset feeds into SIEM
                             Data used to trigger use cases
```
## NIST incident response life cycle model
[Incident response life cycle model](https://csrc.nist.gov/Projects/incident-response), Created February 29, 2024
<img src="https://csrc.nist.gov/csrc/media/Projects/incident-response/images-media/life%20cycle.png" alt="Incident Response Life Cycle" style="width: 60vw;"/>
