 ## Glossary
| term | def|
|-|--|
|Intake Analyst|log a new incident/open ticket/Follow SOP or playbook|

Source of the Incident: System and Human.

- System: SIEM, SOAR, IDS, IPS, Was an IoC found?
> any and all logs or captures—should be retained.
>
> Don’t let them be cycled out or get overwritten.

- Human: client or other third-party agent?
> get any and all contact information possible.
> 
> complete description of the event, including its effects and scope.

Check for access to any client-specific playbooks.
  -> Some clients might have immediate contact requests very early in the SOC process
  -> might contain specific information that will support your investigation.

Ask troubleshooting questions.

Ask Chronological question: eatablish timeline (for logs and network captures)

Ask Demographic questions: determine which log and network items.

Based on the initial information, select a likely set of IoCs.
a) If it is a network call, check for traffic irregularities
b) if it is a system call, check for unusually high/low system utilization, logs for any common IoCs.
  -> common network and system IoCs should be in your SOC SOP playbook
  
Call in might be a more visible symptom of a larger, or more hidden problem.

Make a clear entry of any IoCs found.

Map findings against known attacks and against **Mitre framework***, **Lockheed Martin Kill Chain/Cyber Kill Chain**
> helping predict other IoCs to look for, and position your current findings in the framework.

|Type|| 		Severity||
|-|-|-|-|
|Confidentiality| 	High 	|Medium| 	Low|
|Integrity |	High| 	Medium| 	Low|
|Availability |	High |	Medium |	Low|

If from your initial findings, any item is High, then the incident impact is High.
Item 	Yes 	No
Is there an ongoing attack? 		
Is PII PHI PCI at risk? 		
Is IP data at risk? 		

If ANY of these items is marked Yes, enter the item as Urgent.










