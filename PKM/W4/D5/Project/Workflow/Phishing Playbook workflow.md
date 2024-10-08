
This workflow was built with [NIST IR and Google playbooks](#resources), the idea is;
1. Use a generic incident handling checklist from NIST IR.
2. Fill it in with techinical points from Google playbooks.
3. Adjust for client.

The diagram bellow is adjusted from the [SOC methodology](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D2/workflow.md#the-soc-methodology) diagram

EIR handbook 
SOC Operational handbook

```
Box                                                            # lines begining with `#` are comments.
└─SOC-constitution 
   └─SOC-Organizational_Handbook (Roles, Responsibility)
      ├── SOC-EIR_handbook (D/escalation proceedures, Alert plans, Contacts: phone#, email@)
      ├── SOC-Operational_handbook  (one workflow from a phishing playbook) 
      │   └── SOC Analyst 1 # <-(you are here)
      │         │ Detected Phishing IoC: No/Yes? 
      │         │ If Yes: Use Phishing Playbook.
      │         └──> Collect information and escalate to MSSP-->--------->>[Enter : MSSP SOC framework
      └── SOC-Technical_handbook (SOC desktop/apps)
          │   #-- NOTE: likely
          ├── Linux syslogs, Windows Event logs
          └── ELK/SNMP/PRTG     # No SIEM, No SOAR, No action-integrated monitoring.
```

## EIR handbook 
#### D/escalation proceedures
Follow Alert plans and playbook processes.
#### Alert plans
Send message to recepient if conditions are met.

1. On case of _suspected_ breach: 
- Box Day-time Production Manager:
    1. Send an executive summary.
    2. Send information highlighting major security breach events, and listed potential impacts on company operations.

2. On case _escalated_ or _urgent_ item:
- Box CEO
    1. receives executive summary.

3. On case of _48H+ unresolved_ breach:
- Box CEO
    1. receive executive summary.

On use of __playbook__:
Third-Party MSSP must a receive full report, with actionable items included.

#### contacts: [phone#, email@](#case_contacts)

## SOC Operational handbook
### Phishing Playbook
This is a manual process playbook.

Follow directives and use the check boxes:
- [ ] unchecked
- [x] checked

#### 1. Detection and Analysis
1.0 From Human or/and System detection sources, determine whether an incident has occurred.

1.1. Gather the reported email. Collect and attach email information.
- [ ] Date and time of received email
- [ ] recepient, sender email adresses
- [ ] content (code as text)
Do you have immediate and authorized access to email server? If Yes, collect it.
- [ ] reported email SRC and DST IP/port.

1.2 Quickly analyze the email for precursors and indicators of [Phishing](https://www.getcybersafe.gc.ca/en/resources/real-examples-fake-emails).

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

<!--[ticket template](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/email-template/in-class-ticket-response-email.md#ticket-234)-->
```
Ticket Summary
Suspected Phishing attack <date time, reported leaked information, bad ip confirmed, UI confirmed>

Ticket Description
Box Phishing playbook currently in PLAY. Current stage 3.1

First reported victim received phishing email at <date time>
Victim opened phishing email and <opened urls with bad ip, reported leaked sensitive information>

Information/data included:
- Time & Date received/openned 
- <List of bad IPs, information leaked>
- Victim, attacker emails/addresses.
- Reported email (screenshot, code).

Continuing with Phishing playbook, stage 3.2
```
3.2 [Alert plan](#alert-plans) are triggered.
Day-time Production Manager, receive same executive summary.

```
Header: Notice: Suspected case of cybersecurity breach. Phishing attack.
Body: To Box Day-time Production Manager,

At <date time> occured a suspected phishing indident.
Suspected phishing victim <interacted, leaked sensitive information> with potential attacker.
We are currently in cooperation with third-party security provider (MSSP).

No operational changes currently required.

Continue as normal with raised vigilance on emails.

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
3.3 Send a generic short notice of vigiliance for phishing email to production organization members. In order pre-emptively stop/slow propagation. Reinforce employee risk awareness.

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

4.1 Check step 1.1 at 'reported email SRC and DST IP/port', if unchecked, gather it now, and attach to ticket.

4.2 Query the email server, find other correlated emails with the reported email. Contact IT role if needed.

Collect:
- [ ] Emails with same source address, IP.
- [ ] Contain same bad URL IPs.
- [ ] Same content (heading, body).

- [ ] Attach collection to ticket.

4.3 For each attack emails, check for victim replies or/and information leakage.

If victim leaked sensitive information/secrets/access, check 'Information leakage'
- [ ] Information leakage

- [ ] Immediately forward leak to ticket, raise urgency/priority of ticket by leak severity.

4.4 For each attack emails, gather:
- [ ] Source email, IP, Port
- [ ] Source email IP reputation
- [ ] Destination email, IP, Port
- [ ] IP Resolved URLs / Embeded URLs 
- [ ] Resolved URLs IP reputation
- [ ] email content (Headers, Body)

- [ ] Forward the information collection to the ticket.


#### 5. If possible, Analyze URLs in sandboxed environment by
following the bad IPs. Record and or report the following:
- [ ] unusual processes
- [ ] unusual performance
- [ ] unusual behaviour

- [ ] Forward report to the ticket.

### 6. Response from MSSP
Make sure to respond/perform provided requests/guidelines by MSSP in a timely manner.

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
> Follow MSSP, directives and guidelines.
>
> Continue to 6.2, with priority to incoming MSSP directives and guidelines.

6.2 Gather information for report on relevant MSSP directives and guidelines.
- [ ] Severity of incident
- [ ] Impact of incident
- [ ] Relevance of incident on operations (effects, durration) 
- [ ] Effects of MSSP directives on operations.
- [ ] Brief on the current stage of incident response.


6.3 On breach, [EIR handbook Alert plan](#alert-plans) is now in effect.

Use the Following message templates and send them to the indicated recepient(s).

- [ ] Send Executive summary to Box CEO
```Executive summary
Header: Notice: Confirmed case of cybersecurity breach. Phishing attack.
Body: To Box CEO,

<Incident name> was confirmed to take place at <date time>.

Victim <leaked sensitive information, > 
with potential attacker.
We are currently in cooperation with third-party security provider (MSSP).

No operational changes currently required.

Continue as normal with raised vigilance on emails.

Further confirmations or descalations to come.



```
Box Production Manager.
```
Box Production Manager must receive information highlighting major security breach events, and listed potential impacts on company operations.
```

```
On case of 48H+ unresolved breach:
```


7. MSSP will guide organization and SOC Analyst 1 (YOU) through the next two playbook stages:
- Containment, Eradication, and Recovery
- Post-Incident Activity




---
#### Resources
- [NIST IR Playbook p.42](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf)
- [Google Playbook p.7](https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf)

#### case_contacts
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

#### potential stuff a SOAR could do/ MSSP resonpse actions 
Check Sent Mail for Propagation: sent mail folder for any unauthorized outgoing phishing attack spreading
Automatic Global Log-Out:Force log out of the compromised email account and potentially other associated accounts across different services.
Change of Permissions: owngrade permissions or restrict access to sensitive information and resources associated with the compromised email accoun
Change of Authentication Credentials multi-factor authentication (MFA)
