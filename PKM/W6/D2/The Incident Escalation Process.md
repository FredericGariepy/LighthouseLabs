# The Incident Escalation Process
https://www.atlassian.com/incident-management/on-call/escalation-policies#what-is-an-escalation-policy

Subject:  Actions or events that may require an escalation of an Event Ticket.
Question: How that set of events could be caught in Policy or Process?

An escalation policy
- Processes,
- Roles involved,
- Type of incident,
- SEV level,
- Duration,
- Scope 

[Voccabulary matrix](https://www.splunk.com/en_us/blog/learn/incident-severity-levels.html): \
__Imapact / Likelihood__ = I/L
|I/L|2|1|0|
|-|-|-|-|
|2| __Critial__ |Significant|Moderate|
|1| Significant| Moderate| minor |
|0|Moderate|minor |low-level|

|I/L|2|1|0|
|-|-|-|-|
|2| __SVE 1__ |_SVE 2_|SVE 3|
|1| _SVE 2_| SVE 3| SVE 4|
|0|SVE 3|SVE 4|SVE 5|

# :rabbit: :hole: 
- [Rabbit hole: SRE](https://www.atlassian.com/incident-management/devops/sre#the-devops-incident-management-process)
SRE teams have service-level agreement (SLA), error budget
- minutes of downtime
Error budget can be spent
- SREs and developers have a strong incentive to work together to minimize the number of errors.
```python
uptime = sys.arg[1] # some vital feed
development =  sys.arg[2] # errors introduced

error_margin = 0.01  # e.g. 1% error: OK
tolerance = 1 - error_margin

budget = uptime - tolerance # this is the clincher

def spend(development): # we can pend 
    uptime -= development.error # new errors, lower uptime
    budget = uptime - tolerance # new budget
    return feature # we get feature shipped

def run(budget): # we're in operation
    while budget >= 0: 
        spend(development)
    fix()

def fix(budget):
    while budget < 0
        development.feature.launch.stop()
        uptime = fix(uptime) # get rid of errors
    run()
```
 



 “An escalation policy answers the question of how your organization handles these handoffs.
 It outlines who should be notified when an incident alert comes in,
 who an incident should escalate to if the first responder isn’t available,
 who should take over if or when the responder can’t resolve the issue on their own,
 and how those handoffs should happen.”

They further go on to explain that an escalation policy is used to address how a company will escalate incident, and to whom.
Instructions

    Read the blog from Atlassian entitled, “Escalation policies for effective incident management".

Focus on Atlassian’s Best Practices for Developing Escalation Policies as well as their Types of Escalation Policies.

Use this as a starting point in your research and answer the following questions. Be prepared to discuss these in Lecture:

    List five best practices in Escalation Policy
    List five events that might require escalation
    List three reasons why an Escalation Policy should be established as a clear process in a playbook.
    Explain how the use of escalation might be used to help inform changes to 
### Key points:
Escalation occurs when a first level responder cannot meet service level agreements (SLAs). \
- Escalation normal. part of playbook, workflows.
- Escalations can take many forms and often not due to a particular urgency, but can be simply dependent on job specialization or team member function that is required.
- Escalations are not a sign of the inability to achieve a goal, but can be a normal and required step in the process of completing a particular procedure.

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
