
To build a workflow with these [resources](#resources),
1. Use a generic incident handling checklist from NIST IR.
2. Fill it in with techinical points from Google playbooks.
3. Adjust for client.

The diagram bellow is adjusted from the [SOC methodology](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D2/workflow.md#the-soc-methodology) diagram
```
# lines begining with `#` are comments.
SOC-Organizational_Handbook (Roles, Responsibility)
      ├── SOC-EIR_handbook (D/escalation proceedures, Alert plans, Contacts: phone#, email@)
      ├── SOC-Operational_handbook  (one workflow from a phishing playbook) 
      │   └── SOC Analyst 1 # <-(you are here)
      │         │ Detected Phishing IoC: No/Yes? 
      │         │ If Yes: Use Phishing Playbook.
      │         └──> Collect information and escalate to MSSP-->------------------------------>>[Enter : MSSP SOC framework
      └── SOC-Technical_handbook (SOC desktop/apps)
          │   #-- NOTE: likely
          ├── Linux syslogs, Windows Event logs
          └── ELK/SNMP/PRTG     # No SIEM, No SOAR, No action-integrated monitoring.
```

## EIR handbook 
#### d/escalation proceedures
Follow Alert plans and playbook processes.
#### Alert plans
On case of suspected breach:
- Client, Box, must receive an executive summary.
- Box Production Manager must receive information highlighting major security breach events, and listed potential impacts on company operations.
- Third-Party provider must a receive full report, with actionable items included.
#### contacts: 
- [phone#, email@](#case_contacts)

## SOC Operational handbook
### Phishing Playbook
Check Sent Mail for Propagation: sent mail folder for any unauthorized outgoing phishing attack spreading
Automatic Global Log-Out:Force log out of the compromised email account and potentially other associated accounts across different services.
Change of Permissions: owngrade permissions or restrict access to sensitive information and resources associated with the compromised email accoun
Change of Authentication Credentials multi-factor authentication (MFA)

Follow directives and use the check boxes:
- [ ] unchecked
- [x] checked 
#### Stage: Detection and Analysis
1. From Human or/and System detection sources, determine whether an incident has occurred.

1.1. Gather the reported email. Quickly analyze the email for precursors and indicators of [Phishing](https://www.getcybersafe.gc.ca/en/resources/real-examples-fake-emails).

If one box is checked move immediately to step 1.2
On the email, look for:
- [ ] Spoofed email address
- [ ] Pressures for action, deadlines, rewards
- [ ] Vague, typos, non-direct refferences, inconsistency

On the potential victim machine, look for and ask user about:
- [ ] Did they follow any email url, produce any clicks, see any opens.
- [ ] Noticed unsual processes, behaviours, CPU use (heat, sound, slowness), Bandwidth use.

1.2 If possible, ask user about information leakage.

Did they share/input/reply with sensitive informaiton/secrets/access ?
If yes, collect leaked information, 'Information Leak', escalate the collected information.
- [ ] Information leak
- [ ] Iformation type: ___________

2. Extract (embedded) URLs from email content. Resolve the URLs to IPs. Check for IP reputation.

Mark ‘true positive’ if bad IP and escalate the collected information.
- [ ] True postivie

3. Notify MSSP
Depending on MSSP conduct of communications, use available contacts/means/channels found in [EIR Handbook](#eir_handbook).

Use more than one contact point if needed, ensure timely reponse.

3.1. As an [Intake Analyst](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/Intake%20Analyst.md) open a ticket (with MSSP contact found in EIR handbook) for a potential Phishing attack, forward collected informaiton to MSSP.

<!--[ticket template](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/email-template/in-class-ticket-response-email.md#ticket-234)-->
```
Ticket Summary
Phishing attack at <time date>, <UI confirmed, bad ip, possible infection, >

Ticket Description
Phishing plabook currently in PLAY. Current stage 3.1
Victim opened phishing email and <opened urls with bad ip, reports performance symptoms, reported replying with sesitive info.>

Information/data included:
- Reported email (screenshot,code).
- List of bad IPs. (text)
- Victim email (text)
- Information leaked

Continuing with 3.2
```
3.2 Send a short notice of vigiliance for phishing email to production organization members.
3.3 Alert plan is now in effect, Client, Box, must receive an executive summary.

```
Email
Cybersecurity Notice: Case of suspected breach



```

> [!IMPORTANT]  
> Stay alert for contact from MSSP on new opened ticket.
> On reply/alert/contact by MSSP go to **step 6**.

4 Gather further infomation & check for phishing campaign
4.1 Query the email server, find other correlated emails with the reported email. Contact IT role if needed.
- [ ] Emails with same source address, IP.
- [ ] Contain same bad URL IPs.
- [ ] Same content (heading, body).
4.2. For each attack emails, check for victim replies or/and information leakage.

If victim leaked information/secrets/access, check 'Information leakage'
- [ ] Information leakage
Immediately forward informaiton leak to ticket, raise urgency/priority of ticket.
      
4.3. For each attack emails, gather:
- [ ] Source email, IP, Port
- [ ] Source email IP reputation
- [ ] Destination email, IP, Port
- [ ] IP Resolved URLs / Embeded URLs 
- [ ] Resolved URLs IP reputation
- [ ] email content (Headers, Body)
Forward the information collection to the ticket.

5. If possible, Analyze URLs in sandboxed environment by
following the bad IPs. Record and or report the following:
- [ ] unusual processes
- [ ] unusual performance
- [ ] unusual behaviour

6. Response from MSSP
Make sure to respond/perform provided requests/guidelines by MSSP in a timely manner. \

Communications: 
IF 

 Client, Box, must receive an executive summary.
- Box Production Manager must receive information highlighting major security breach events, and listed potential impacts on company operations.
- Third-Party provider must a receive full report, with actionable items included.



MSSP will guide organization and SOC Analyst 1 (YOU) through the next two playbook stages:
- Containment, Eradication, and Recovery
- Post-Incident Activity

>  ASAP respond/perform provided requests/guidelines.


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
