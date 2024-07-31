The Incident Escalation Process


Incident Escalation (process SO 2.6) \
| Process ID | Procedure or Decision | Description | Role|
| - | -| -| -|


Escalation occurs when a first level responder cannot meet service level agreements (SLAs). \
__What does this mean?__ \
An SLA often outlines items like response times and times to fix.

The understanding is, given a relatively straight forward playbook, the analyst should be expected to complete the play in a known amount of time. If they can’t, then escalation should occur.

There are other causes of escalation to consider as well. The incident might be out of scope for the analyst; that is, too high a level or too damaging, though the playbook should include this and have escalation as part of its actions.

Escalation may also occur if the analyst does not have sufficient resources to handle a specific incident. This might occur if, for example, the analyst has to pass the ticket on to a data or network analyst.


Incident Escalation (process SO 2.6) \
https://docs.microfocus.com/SM/9.60/Hybrid/Content/BestPracticesGuide_PD/IncidentManagmentBestPractice/Incident_Escalation.htm \
e.g.
| Process ID | Procedure or Decision | Description | Role|
| - | -| -| -|
| SO 2.6.1   | Determine how to resolve Incident       | The Incident Coordinator gathers information from the Incident Analyst(s) about the status of the incident resolution and determines how the incident can best be resolved. The Incident Coordinator verifies that the expected resolution time matches any agreed on level, such as that specified in an SLA. | Incident Coordinator |
| SO 2.6.2   | Problem Management required?            | Is problem management required to solve the incident? If yes, continue with SO 2.6.3. If no, go to SO 2.6.4.                                                        | Incident Coordinator |
| SO 2.6.3   | Escalate to Problem                     | Go to SO 2.6.1 to determine how to resolve the Incident.                                                                                                               | Incident Coordinator |
| SO 2.6.4   | Change Management required?             | Is a change required to solve the incident? If yes, continue with SO 2.6.5. If no, go to SO 2.6.11.                                                                  | Incident Coordinator |
| SO 2.6.5   | Escalation required?                    | Determine whether escalation is required to the Incident Manager to review what action to take with the Change Request. If yes go to SO 2.6.7 to mark the Incident for escalation. If not, go to SO 2.6.9 to Register Emergency Change | Incident Coordinator |
| SO 2.6.6   | Determine expected resolution time      | The Incident Manager verifies that the expected resolution time meets SLA targets.                                                                                   | Incident Manager    |
| SO 2.6.7   | Mark Incident for Escalation            | The Incident Coordinator checks the Escalation checkbox in the incident record and marks the Incident for Escalation. A notification is sent to the Incident Manager informing him/her of escalation. | Incident Coordinator |
| SO 2.6.8   | Determine and execute escalation actions | The Incident Manager determines the actions to be performed to solve the incident within target times and designates escalation personnel to contact in the event of an escalation. This can include determining that the Service Desk is required to send an information bulletin to the affected users and stakeholders. | Incident Manager    |
| SO 2.6.9   | Register emergency change               | The Incident Coordinator registers an emergency change request and contacts the Change Manager to inform the manager about the request, thereby starting the Emergency Change Handling process. | Incident Coordinator |
| SO 2.6.10  | Emergency change needed?                | If yes, go to SO 2.6.9. If no, go to SO 2.6.1.                                                                                                                        | Incident Manager    |
| SO 2.6.11  | Service Request required?               | If yes, close the Incident. If not, go to SO 2.6.12.                                                                                                                   | Incident Coordinator |
| SO 2.6.12  | Reassignment required?                  | Is it necessary to reassign the incident to a different support group with more knowledge (that is, a functional escalation)? If yes, continue with SO 2.6.14. If no, go to SO 2.6.13. | Incident Coordinator |
| SO 2.6.13  | Enable Incident Analysts to solve incident | The Incident Coordinator enables the Incident Analyst(s) to focus solely on the resolution of the incident and provides the Incident Analyst(s) with all means necessary to speed up the resolution. Go to SO 2.4.4. | Incident Coordinator |
| SO 2.6.14  | Incident Manager required?              | Escalation may be required for the Incident Manager to agree the appropriate assignment for the Incident. This may be required where there is a dispute over which group should take ownership of the Incident. If the Incident Manager must get involved, go to SO 2.6.15. If not, go to SO 2.6.16. | Incident Coordinator |
| SO 2.6.15  | Mark Incident for Escalation            | The Incident Coordinator checks the Escalation checkbox in the incident record and marks the Incident for Escalation. A notification is sent to the Incident Manager informing him/her of escalation. Then go to SO 2.6.17. | Incident Coordinator |
| SO 2.6.16  | Reassign incident                       | The Incident Coordinator reassigns the incident to another 2nd-line or 3rd-line support group.                                                                         | Incident Coordinator |
| SO 2.6.17  | Determine/ Agree appropriate assignment  | The Incident Manager reviews the Incident to determine the appropriate Assignment Group based on the skills/ knowledge or permissions required to resolve the Incident. | Incident Manager    |
| SO 2.6.18  | Reassign incident                       | The Incident Manager reassigns the incident to another 2nd-line or 3rd-line support group.                                                                           | Incident Manager    |
