## Key Takeaways

- Blue Team members work in shifts;
> a shift usually has the following phases: Arrival and Read-in, Meeting and Consultation Write-ups, In Seat and Monitoring, and Day-end Reporting for End of Shift.
- For the purpose of the hand-off, shift reports are created.
- Shift reports are created using the SEAT-SWAP framework.
> SEAT stands for Staff, Explanation, Awareness, and Transition, while SWAP stands for Situation, Written, Accurate, and Persistent.
> 
> SEAT-SWAP form gives a general picture of the status of tasks overall, and assists in prioritizing actions.
- Incident Report form gives more detail on a specific incident.
___

[Blue Team Shifts, Changes and Reporting](https://web.compass.lighthouselabs.ca/p/cyber/days/w04d1/activities/2954)

[SANS (SysAdmin, Audit, Network, and Security) Institute](https://www.sans.org/media/analyst-program/common-practices-security-operations-centers-results-2019-soc-survey-39060.p)
> Common and Best Practices for Security Operations Centers: Results of the 2019 SOC Survey

# Day of a Cyber Security analyst. Different phases of their shift:
| time | activity |
|-|-------|
| 9:00 a.m. | [Arrival and Read-in](#arrival-and-read-in) |
| 10:00 a.m. | [Meeting and Consultation Write-ups](#meeting-and-consultation-write-ups) |
| 1:00 pm | [In Seat, Monitoring](#in-seat-monitoring) |
| 4:00 pm | [Day-End Reporting for End of Shift](#day-end-reporting-for-end-of-shift) | 

#### Arrival and Read-in 
###### 9:00 a.m. [⬆️](#day-of-a-cyber-security-analyst-different-phases-of-their-shift)
During this time, the Analyst will first check current reports for new or ongoing incidents.
This could be a direct hand-off from a night or weekend shift, and may contain incidents that are (New, Open, Closed):

- **New**: No work has yet been done, and initial identification should start
- **Open**:
    - Ongoing: Investigation has started / Initial remediation and recommendations are ongoing.
    - Escalated: Night or Weekend shifts have requested help on an initial investigation or remediation, or the status or priority of an incident has gone up.
    - Solved: An incident has been remediated and final reports have been generated, immediate incident reports have been responded to, followed by reporting of lessons learned and recommended fixes.
- **Closed**

If new, ongoing, or escalated incidents exist, the Analyst will spend time investigating those incidents.

#### Meeting and Consultation Write-ups
###### 10:00 a.m.  [⬆️](#day-of-a-cyber-security-analyst-different-phases-of-their-shift)
- If required, interviews with senior staff, organizational teams, reviews of project statuses
- If required, research incidents, vulnerabilities, threats, and risks
- If required, write-up of recommendations and findings
- Continuing work with open incidents

#### In Seat, Monitoring
###### 1:00 pm  [⬆️](#day-of-a-cyber-security-analyst-different-phases-of-their-shift)
Ongoing monitoring of security information and event management (SIEM), event logs, etc.
- Onboarding of new incidents
- Continuation of open incidents
- Closing of incidents

#### Day-End Reporting for End of Shift
###### 4:00 pm   [⬆️](#day-of-a-cyber-security-analyst-different-phases-of-their-shift)
At the end of the shift, outgoing shift members share updates with the incoming shift members. See Below:


# Shift Reports and Hand-off (SEAT-SWAP)
### [SWAT SWAP shift change report sample](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D1/Blue%20Team/SEAT-SWAP%20%5Bshift%20change%20report%5D.md)
SEAT SWAP form gives a general picture of the status of tasks overall, and assists in prioritizing actions. 
**SEAT-SWAP** is a shift handover process used in SOCs, as explained below: 

##### SEAT
||||
|-|--|-----|
|S|staff | Who is involved both coming and going|
|E|explanation | Inform on active situations|
|A|awareness | Details on specific problems - Situational awareness |
|T|transition | Make changeover seamless to all parties concerned. No individual party should have to wait for a specific person's interactions.|

##### SWAP
||||
|-|--|-----|
|S|situation | Discuss the situation in a clear and comprehensive manner.|
|W|written | Handoff is in *written form*. No information is passed that is not captured in writing.|
|A|accurate | All information is accurate; if something is a guess, it is labeled as a guess.|
|P|persistent | There is *always a report*, even if nothing has changed or there is nothing to report.|

> It should be noted that this framework talks about not just what is reported, but to what standard the item is addressed.

[Siemplify SOAR platform software solution](https://www.youtube.com/watch?v=xmusgGAxeWs&feature=youtu.be)

Common “trigger” events that lead to escalation of an incident.
Typically anything that shows a high level of effect against the CIA Triad would either escalate the incident or have it marked as “Urgent”.

Relevant Incident Reports will be examined to determine specific actions and statuses.

Playbooks will be assessed and followed. In some cases, where no specific Playbook is available, generic playbooks might be used. 




