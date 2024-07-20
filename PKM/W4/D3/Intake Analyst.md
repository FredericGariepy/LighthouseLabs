## Resources
- [x] [Data Classification Overview](https://cybersecurity.uillinois.edu/data_classification)
- [ ] [NIST Computer Security Incident Handling Guide ](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf) See Page 42.
- [ ] [Data Classification for Compliance with PCI DSS, NIST, HIPAA and More](https://blog.netwrix.com/2023/12/01/data-classification-for-compliance/)

## Glossary
| term | def|
|-|--|
|Intake Analyst|log a new incident/open ticket/Follow SOP or playbook|
|PII|Personally Identifiable Information|
| PCI|Payment Card Industry (data)
|PHI|Protected Health Information |

#### Generic SOP (example)
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
|Item |	Yes |	No|
|-|-|-|
|Is there an ongoing attack?||| 		
|Is PII PHI PCI at risk? |||
|Is IP data at risk? |||

If ANY of these items is marked Yes, enter the item as Urgent.
Items High and Urgent are in most cases escalated. 

If in your research you find immediate recommendations for stopping an attack, check your playbook. There might be occasions where monitoring and securing data from exfiltration come first.

####  Generic SOP ABOVE follows this guideline BELOW.
#### [NIST Incident Handling Checklist](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf) **p.42**

|Step|Action|Completed|
|-|---------|-|
||__Detection and Analysis__||
|1.| Determine whether an incident has occurred||
|1.1| Analyze the precursors and indicators||
|1.2| Look for correlating information||
|1.3 |Perform research (e.g., search engines, knowledge base).||
|1.4 |As soon as the handler believes an incident has occurred, begin documenting the investigation and gathering evidence.||
||||
|2| Prioritize handling the incident based on the relevant factors (functional impact, information impact, recoverability effort, etc.).||
||||
|3|Report the incident to the appropriate internal personnel and external organization’s Containment, Eradication, and Recovery.||
||||
||__Contianment, Eradication, and Recovery__||
|4.|Acquire, preserve, secure, and document evidence.||
|5.|Contain the incident.||
||||
|6.|Eradicate the incident:||
|6.1| Identify and mitigate all vulnerabilities that were exploited.||
|6.2|Remove malware, inappropriate materials, and other components.||
|6.3|If more affected hosts are discovered (e.g., new malware infections), repeat the Detection and Analysis steps (1.1, 1.2) to identify all other affected hosts, then contain (step 5) and eradicate (step 6) the incident for them.||
||||
|7.|Recover from the incident:||
|7.1| Return affected systems to an operationally ready state.||
|7.2| Confirm that the affected systems are functioning normally.||
|7.3| If necessary, implement additional monitoring to look for future related activity.||
||||
||__Post-Incident Activity__||
|8.|Create a follow-up report.||
|9.|Hold a lessons learned meeting (mandatory for major incidents, optional otherwise).||








