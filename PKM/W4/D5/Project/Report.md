> [!NOTE]
> This project was accepted.
>
> Enhancement suggested:
> 1. Create a visual for workflow. For Visuals use [https://app.diagrams.net/](https://app.diagrams.net/)
> 
> 2. Add short executive summary at the start.
# Playbook for Cat & Box Scenario 
Date: 07/23/2024
## Contents
- [About this case](#about-this-case)
- [SOC organizational chart](#soc-organizational-chart)
- [SOC EIR handbook](#eir-handbook)
- [SOC operational handbook](#soc-operational-handbook)
- [Conclusion](#conclusion)
<!--- -->
- [References](#references)

## About this case
The case has [two organizations](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D5/Project/notes.md#case-groups-and-roles), Box and a third-party MSSP.

You, working at Box, are the sole security operations center (SOC) analyst. \
The SOC you operate has _limited resources and capabilities_. \
So, your senior management has contracted an MSSP for all risks needing escalation.

This case first presents an SOC organizational chart. 

In this chart, you can find the analyst and two handbooks. \
One handbook is the EIR handbook which contains: alert plans, contacts, and d/escalation proceedures. \
The second, Operational handbook, contains a workflow from a phishing playbook.

In the Operational handbook, you can follow phishing playbook procedures, to the extent afforded by the SOC, \
meaning, up until MSSP response. 

For communication, templates and directives are found as required along the workflow.

The playbook was build with a generic incident handling checklist from NIST IR (NIST, n.d.), populated with procedures from Google cloud's phishing playbook (Google Cloud, n.d.), and adjusted for the client (Box). 

To try and make this case enjoyable, imagine that you are an analyst in an 'old-school' SOC. \
Find your location in the organizational chart, look at your EIR handbook, \
follow the proceedures in the phishing playbook.

## SOC organizational chart
This SOC organizational chart at the Box company, is based on the [SOC methodology](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D2/workflow.md#the-soc-methodology) by [Andreas Wagner](https://secureglobal.de/the-soc-methodology) (Wagner, n.d.).
###### Find your location in the organizational chart
```
Box                                                            # lines begining with `#` are comments.
└─SOC-constitution 
   └─SOC-Organizational_Handbook (Roles, Responsibility)
      ├── SOC-EIR_handbook (D/escalation proceedures, Alert plans, Contacts: phone#, email@)
      ├── SOC-Operational_handbook  (one workflow from a phishing playbook) 
      │   └── SOC Analyst 1 # <-(you are here)
      │         │ Suspect Phishing IoC: No/Yes? 
      │         │ If Yes: Use Phishing Playbook.
      │         └──> Collect information and escalate to MSSP-->--------->>[Enter : MSSP SOC framework
      └── SOC-Technical_handbook (SOC desktop/apps)
          │   # No SIEM, SOAR. Hence reliance on MSSP.
          ├── Linux syslogs, Windows Event logs # assumed
          └── ELK/SNMP/ PRTG(free 100 sensors) (Paessler, n.d.) # assumed
```

## SOC EIR handbook 
#### D/escalation proceedures
Follow Alert plans and playbook processes.
#### Alert plans
Send message to recepient if conditions are met.

1. On case of _suspected_ breach: \
Contact: Box Day-time Production Manager:
    1. Send an executive summary.
    2. Send information highlighting major security breach events, and listed potential impacts on company operations.

2. On case _escalated_ or _urgent_ item: \
Contact: Box CEO
    1. Send executive summary.

3. On case of _48H+ unresolved_ breach: \
Contact: Box CEO
    1. Send executive summary.

On use of __playbook__:
Third-Party MSSP must a receive full report, with actionable items included.

#### Contacts:
```
    Box Manufacturing
    Percy: percy@box.cat
    Misha: mesha@box.cat Phone 902-9836
    Minka: minka@box.cat Phone 562-7658
    YOU: SOCAnalyst1@box.cat Phone 562-7658
    Dusty: dusty@box.cat Phone 462-8952
    Lucky: lucky@box.cat Phone 269-5466
    Ned: ned@box.cat Phone 877-4332

    MSSP & SOC Security Oversight (3rd party) *Think SOC 2,2+, and full SOC*
    Cat: cat@soc.cat Phone 905-4616 or cell 902-4321
```
## SOC Operational handbook
### Phishing Playbook
This is a manual process playbook.

Follow directives and use the check boxes:
- [ ] unchecked
- [x] checked

#### 1. Detection and Analysis
1.0 From Human or/and System detection sources, determine whether an incident has occurred.

1.1. Gather the reported email. Collect email information:
- [ ] Date and time of received email
- [ ] recepient, sender email adresses
- [ ] content (code as text)

Do you have immediate and authorized access to email server? If Yes, collect:
- [ ] Source and Destination IP/port of reported email.

1.2 Quickly analyze the email for indicators of [Phishing](https://www.getcybersafe.gc.ca/en/resources/real-examples-fake-emails) (Government of Canada, n.d.).

If one box is checked move immediately forward to step 1.3
On the email, look for:
- [ ] Spoofed email address
- [ ] Pressures for action, deadlines, rewards
- [ ] Vague, typos, non-direct refferences, inconsistency

On the potential victim machine, look for and ask user about:
- [ ] Did they follow any email url, produce any clicks, see any opens.
- [ ] Noticed unsual processes, behaviours, CPU use (heat, sound, slowness), Bandwidth use.

1.3 If available, ask user about information leakage.

Did they share/input/reply with sensitive information/secrets/access ?

If yes, mark 'Information Leak', collect leaked information, escalate the collected information.
- [ ] Information leak

#### 2. Extract all URLs (embeded) from email content. Resolve the URLs to IPs. Check for all collected IP reputations.

Mark ‘true positive’ if bad IP and escalate the collected information.
- [ ] True postivie

#### 3. Notify MSSP

Depending on MSSP conduct of communications, use appropriate and available contacts/channels found in [EIR Handbook](#eir_handbook).
- [ ] Chose MSSP contact
- [ ] Chose a communication channel
###### Note: Use more than one contact point if needed, ensure timely reponse.
Continue to 3.1

3.1 As an [intake analyst](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/Intake%20Analyst.md) open a ticket (with MSSP contact, communication channel) for a suspected Phishing attack, forward collected informaton to MSSP.

> [!NOTE]
> Item is currently a __suspected breach__.
> 
> Analyst level 1 __does not confirm the incident__.

Use the [ticket template](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/email-template/in-class-ticket-response-email.md#ticket-234) below, fill-in and attach required information.
- [ ] Send completed ticket to MSSP
```
Ticket Summary
Suspected Phishing attack <date time, reported leaked information, bad ip confirmed, UI confirmed>

Ticket Description
Box Phishing playbook currently in PLAY. Current stage 3.1

First reported victim received phishing email at <date time>
Victim received phishing email and <followed urls with bad ip, reported to have leaked sensitive information>

Information/data included:
- Time & Date phishing email received/openned 
- <List of bad IPs>
- <information leaked>
- Victim, attacker emails/addresses.
- Reported email (screenshot, code).

Continuing with Phishing playbook, stage 3.2
```
3.2 [Alert plan](#alert-plans) are triggered.

Use the 'Suspected phishing' executive summary template below, fill-in required information.
- [ ] Find Day-time Production Manager contact in EIR Handbook
- [ ] Send completed executive summary to Day-time Production Manager
```Suspected phishing
Header: Notice: Suspected case of cybersecurity breach. Phishing attack.
Body: To Box Day-time Production Manager,

At <date time> occured a suspected phishing indident.
Suspected phishing victim <may have been compromised, leaked sensitive information> with potential attacker.
We are currently in cooperation with third-party security provider (MSSP).

No operational changes currently required.

Continue as normal with raised vigilance.

Further confirmations or descalations to come.
Sending vigilance notice to employees.

If you have any doubts about the legitimacy of an email, please contact for Support for guidance.
Thank you for your attention to this matter.
Best regards,

[Your Name]
Box SOC Analyst 1
SOCAnalyst1@box.cat
Phone 777-6699
```
3.3 Raise organization vigilance for phishing.
Use the generic short notice template. Send it to production organization members. \
In order pre-emptively stop/slow propagation. Reinforce employee risk awareness.
- [ ] Fill-in required information.
- [ ] Send to relevant production organization employees in EIR handbook.
```Message made with AI (Chat Gpt 3.5)
Header: Suspected phishing email circulating within our network
Body: To Box Production Organization Members,

We have recently identified a suspected phishing email circulating within our network. 
Phishing emails appear legitimate but contains links or attachments designed to compromise our systems.
To safeguard our organization's security, please exercise caution:

    - Do not click on suspicious links or download attachments from unknown or unexpected sources.
    - Verify the sender's email address before responding or taking any action.
    - Report any suspicious emails to our IT Security team immediately.

If you have any doubts about the legitimacy of an email, please contact Support for guidance.
Thank you for your attention to this matter.
Best regards,

[Your Name]
Box SOC Analyst 1
SOCAnalyst1@box.cat
Phone 777-6699
```

> [!IMPORTANT]
> On reply/alert/contact by MSSP, mark down current working stage, go to **step 6**.

#### 4. Gather further infomation & check for phishing campaign with access to webserver.

4.1 Check step 1.1 for 'reported email SRC and DST IP/port', if unchecked:
- [ ] Gather SRC and DST IP/port on reported email.
- [ ] Forward gathered IP/port information to ticket.

4.2 Query the email server, find other correlated emails with the reported email. Contact IT role if needed.

Collect:
- [ ] Emails with same source address, IP.
- [ ] Contain same bad URL IPs.
- [ ] Same content (heading, body).

When collection is complete.
- [ ] Attach collection to ticket.

4.3 For each attack emails, check for victim replies or/and information leakage.

If victim leaked sensitive information/secrets/access, check 'Information leakage'
- [ ] Information leakage

If 'Information leakage' is checked,
- [ ] Collect leaked information.
- [ ] Immediately forward leak to ticket, raise urgency/priority of ticket by leak severity.

4.4 Check for phishing campaign \
For each attack emails, gather:
- [ ] Source email, IP, Port
- [ ] Destination email, IP, Port
- [ ] IP Resolved URLs / Embeded URLs 
- [ ] email content (Headers, Body)

For all IPs gathered, check reputation.
- [ ] Resolved URLs IP reputation
- [ ] Source email IP reputation

Collect phishing campaign analysis and forward it.
- [ ] Forward the information collection to the ticket.


#### 5. If possible, Analyze URLs in sandboxed environment by
following the bad IPs. Record for the following:
- [ ] unusual processes
- [ ] unusual performance
- [ ] unusual behaviour
- [ ] Collect findings and create report.
- [ ] Forward report to the ticket.

#### 6. Response from MSSP
Make sure to respond/perform provided requests/guidelines by MSSP in a timely manner. \
The MSSP responce on the incident will eventually be one of two outcomes, a or b.

a) MSSP declares that no incident is in place.
- [ ] Follow MSSP descalations directives and guidelines.
- [ ] Provide descaltion email to contacted members, *if needed*.
- [ ] Close the Phishing Playbook.
- [ ] Report learnings in opperational handbook.

b) Incident named and confirmed by MSSP.

If MSSP confirms incident, mark 'Incident confirmed'.
- [ ] Incident confirmed

Write date time.
- [ ] Incident confirmed on _____

Write named attack.
- [ ] Incident name _____

Continue to 6.1.

6.1 MSSP communicates directives and guidelines. 
> [!IMPORTANT]
> MSSP is now leading.
>
> Follow MSSP directives and guidelines.
>
> Continue on this playbook's processes, __with priority to incoming MSSP directives and guidelines.__

6.2 Gather information for report on relevant MSSP directives and guidelines.
- [ ] Severity of incident [(SVE Lvl.)](https://www.splunk.com/en_us/blog/learn/incident-severity-levels.html) (Splunk, n.d.)
- [ ] Impact of incident
- [ ] Relevance of incident on operations (effects, durration) 
- [ ] Effects of MSSP directives on operations.
- [ ] Brief on the current stage of incident response.

6.3 On breach, [EIR handbook Alert plan](#alert-plans) is now in effect.

Use the Following message templates and send them to the indicated recepient(s).

Confirmed incident executive summary template, below.
- [ ] Find CEO contact in EIR Handbook.
- [ ] Send completed executive summary to Box CEO.
```Executive summary
Header: Notice: Confirmed case of cybersecurity breach. Phishing attack.
Body: To Box CEO,

<Incident name> was confirmed to take place at <date time> by MSSP.
Victim <leaked sensitive information, was compromised>. 

The incident is <severity level> and <impact level>.
The incident will <relevance of incident on operations, effects, durration>.

We are currently in cooperation with third-party security provider (MSSP).
Following procedures with MSSP will <effects of MSSP directives on operations>.

We are now in <brief on the current stage of incident response>.

[Your Name]
Box SOC Analyst 1
SOCAnalyst1@box.cat
Phone 777-6699
```
6.4 Notify operations in case of production impact.

Does the incident pose a potential impact on production? \
Mark 'Production impact' if Yes.
- [ ] Production impact

If production impact is checked, fill out the following:
- [ ] Changes to operations ______
- [ ] Estimated duration of operation changes ______

Operation Impacts template, below.
- [ ] Find Production manager in EIR Handbook.
- [ ] Send completed Operation Impacts to Box Production manager.
```Operation Impacts
Header: Notice: Confirmed case of cybersecurity breach. Operational impacts.
Body: To Box Production manager,

An <Incident name> was confirmed to take place in the organization.
The incident will have <Production impact> on operations.

This will result in the following:
- <list of Changes to operations>.

These changes are <Estimated duration of operation changes>.
Observe these changes until resolution of incident.

Reach out for clarifications or questions.

[Your Name]
Box SOC Analyst 1
SOCAnalyst1@box.cat
Phone 777-6699
```
6.5 Notify executive in case of 48 hours unresolved breach.

Has 48 hours have elapsed since response from MSSP (step 6)? \
If yes, mark '48 Hour elapsed'
- [ ] 48 Hour elapsed

Is the breach still active/open ? \
If yes, mark 'Breach Unresolved'
- [ ] Breach Unresolved

Note changes to the following, since MSSP initial response:
- [ ] Severity of incident: increased / decreased / no change
- [ ] Impact of incident:   increased / decreased / no change
- [ ] Current stage of incident response: _______ / no change

If Both '48 Hour elapsed' and 'Breach Unresolved' are checked, \
Use 48 hours unresolved breach template, below.
- [ ] Find CEO contact in EIR Handbook.
- [ ] Send completed template to Box CEO.
```48 hours+ unresolved breach
Header: Notice: Unresolved cybersecurity breach.
Body: To Box CEO,

<Incident name> was confirmed to take place at <date time> by MSSP.
The breach has now been unresolved for 48 hours.

The incident severity has <current severity status>.
The indicent impact has <current impact status>.

We are still in cooperation with the third-party security provider (MSSP).
In the <current stage of incident response>.

Reach out for clarifications or questions.

[Your Name]
Box SOC Analyst 1
SOCAnalyst1@box.cat
Phone 777-6699
```
#### 7. The MSSP will provide the next stages and processes to follow.

Follow the MSSP directives and guidance.
- [ ] Containment
- [ ] Eradication
- [ ] Recovery
- [ ] Post-Incident Activity

If 'Post-Incident Activity' is checked,
- [ ] Close the phishing playbook.
- [ ] Report learnings in opperational handbook
## Conclusion 
Lacking in senior leadership, tools, fictional lack of funds, \
the SOC is at mercy of a significant incident without contact to an MSSP. \
For the SOC in this case, timely communication with the right type of information, \
allows the MSSP to use its knowledge and technology in order to mitigate client risk. \
Therefore, the single analyst SOC was most reliant on communication.

Further, a vast majority of the phishing playbook process could have been automated (Google Security Operations, 2019). \
SOAR tools make it developer friendly to import/export playbooks and automate specific incident response workflows.

To close, here are three automations for a phishing playbook (besides SOPs, such as blocking IP): \
Global Log-Out; Force log out of the compromised email account and potentially other associated accounts across different services. \
Change of Permissions: downgrade permissions or restrict access to sensitive information and resources associated with the compromised email account. \
Check Mail for Internal Propagation: Automatically block insider phishing attacks or campaigns spreading from inside the organization.

## References
Google Cloud. (n.d.). Top Security Playbooks 2022-2023. Retrieved July 23, 2024, from [https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf](https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf)

Google Security Operations. (2019, August 28). How SOAR Playbooks Can Implement Predictable Workflows for Alert Handling [Video]. YouTube. Retrieved July 23, 2024, from [https://www.youtube.com/watch?v=g0sWx_9o_6I](https://www.youtube.com/watch?v=g0sWx_9o_6I)

Government of Canada. (n.d.). Real Examples of Fake Emails. Get Cyber Safe. Retrieved July 23, 2024, from [https://www.getcybersafe.gc.ca/en/resources/real-examples-fake-emails](https://www.getcybersafe.gc.ca/en/resources/real-examples-fake-emails)

National Institute of Standards and Technology (NIST). (n.d.). Computer Security Incident Handling Guide (NIST Special Publication 800-61 Revision 2). Retrieved July 23, 2024, from [https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf)

Paessler. (n.d.). How to use 100 sensors to keep an eye on critical points in your IT – at no cost. Retrieved July 23, 2024, from https://www.paessler.com/howto-free-network-monitoring

Splunk. (n.d.). Incident severity levels 1-5 explained. Retrieved July 23, 2024, from https://www.splunk.com/en_us/blog/learn/incident-severity-levels.html

Wagner, A. (n.d.). The SOC Methodology. Retrieved July 23, 2024, from [https://secureglobal.de/the-soc-methodology](https://secureglobal.de/the-soc-methodology)
