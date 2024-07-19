
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
