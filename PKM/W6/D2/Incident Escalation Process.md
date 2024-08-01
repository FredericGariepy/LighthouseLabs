https://www.atlassian.com/incident-management/on-call/escalation-policies#what-is-an-escalation-policy


Subject:  Actions or events that may require an escalation of an Event Ticket.
Question: How that set of events could be caught in Policy or Process?

Escalation policy

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




An escalation policy should address not only how your company will escalate incidents and to whom,
but also if there’s nuance based on the type of incident,
SEV level,
duration,
and scope of the incident.
```python
class  escalation(self)

``

``

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
    Explain how the use of escalation might be used to help inform changes to the NIST Incident Response Lifecycle.

Instruction

Prepare to discuss your findings with the class in Lecture.
Previous
Incident Response Lifecyle
How well did this activity help you to understand the content?

Let us know how we're doing
