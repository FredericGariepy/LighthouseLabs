

With the addition of workflows to an SOC, you now have more to take care of than just finding whether an incident or a ticket is open or closed. 
You now have to consider at what stage a specific ticket is within a workflow, what triggers have been pulled, so to speak, and what must be the next steps.

This type of information can be obtained by analyzing the incident history and comments from other analysts. 
However, this would be a slow and ineffective method.
It’s better that you inform the current state of the incident by effectively bookmarking
where you are in a specific workflow.

Note: you should also be aware that more than one workflow may be in process as you work on a specific ticket.
All incidents will fall under the SOC standard operating procedures (SOP) workflow. 
This workflow is often monitored by the SOC Manager and may include items that are time-triggered
(i.e., alerts for incidents that have been open too long or that have stalled).

process:
->

worfklow:

p2
|
p0---p1



In  SOP: case-specific, generic workflows, Playbooks (PLAY)
e.g.
-standard playbook for Ransomware
-playbooks customized for client specific (internal, external) needs).


Incident specific or client specific playbook is started (PLAY)

The workflow can then look like this:

    An incident is initiated and first level research is conducted:
        Incident is Prioritized; if High and Urgent, it may be assigned to a Tier 2 team member.
        Incident specific or client specific playbook is started (PLAY).
    SOP events continue to run, PLAY steps are run. If either SOP or PLAY triggers fire, an event occurs that is listed in the PLAY, the incident may be further escalated (i.e., more resources are brought to PLAY).
    PLAY ends. That is, the client-specific or case-specific playbook completes.
    SOP continues. This means that other PLAYs may be enacted or that the incident goes through a standard closing procedure.

This flow may, for larger or more complex incidents, reiterate within the SOP; start and close several times. That said, there should only be one OPEN and one CLOSE on the incident within the SOP.
Roles of Preparation and Lessons Learned

Roles of Preparation and Lessons Learned are the two areas involve us in ways that are more like a consultant's role, than the Identification, Containment, Eradication, and Recovery roles (as per NIST Incident Response Lifecycle, as shown below) that are more relevant to an SOC seat.

Four phases of the NIST Incident Response Cycle

Image source: TechTarget

You must remember many of the former items, such as Identification, Containment, etc. are often part of an incident response plan (IRP). This IRP can be generic or very customized, and must be integrated with our incident handling.
Key Takeaways

    If a playbook is implemented in an SOC, it becomes a workflow. In other words, workflows are executed as per playbooks—they are playbooks in action.
    In addition to finding if a ticket for an incident is open or close, you must also look for what stage the ticket is at in a workflow and what steps have been taken as per the workflow.
    A playbook could either be a standard/generic playbook or it could be customized as per the needs of the case or the client (case-specific playbook or client-specific playbook).

Conclusion

In this reading, you learned how to assign playbooks, execute workflows, and handle escalations. In the next reading, you will learn how to intake a new Cyber Security incident and enter it into the system.
Further Readings

    “Standard Operating Procedures (Sops) - Definition & Overview.” Sumo Logic. Accessed January 11, 2023.
    “Does Your SOC Have a Security Playbook?” Security Intelligence, October 8, 2018.
    “6 Steps to Making an Incident Response Plan.” SecurityMetrics, December 23, 2022.

Previous
Feedback on Building SOC Team & Reporting Structure
Next
Logging a New Incident into the System and Escalation
How well did this activity help you to understand the content?

Let us know how we're doing
