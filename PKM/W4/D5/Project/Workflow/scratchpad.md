
To build a workflow with these [resources](#resources),
1. Use a generic incident handling checklist from NIST IR.
2. Fill it in with techinical points from Google playbooks.
3. Adjust for client.

The diagram bellow is adjusted from the [SOC methodology](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D2/workflow.md#the-soc-methodology)
```
# lines begining with `#` are comments.
SOC-Organizational_Handbook (Roles, Responsibility)
      ├── SOC-EIR_handbook (Alert plans, phone#, email@, d/escalation proceedures)
      ├── SOC-Operational_handbook  (one workflow from a phishing playbook) 
      │   └── SOC Analyst 1 # <-(you are here)
      │         │ Detected IoC: No/Yes? 
      │         │ If Yes:
      │         └──> send to MSSP-->------------------------------>>[Enter : MSSP SOC framework
      └── SOC-Technical_handbook (SOC desktop/apps)
          │   #-- NOTE: likely
          ├── Linux syslogs, Windows Event logs
          └── ELK/SNMP/PRTG     # No SIEM, No SOAR, No action-integrated monitoring.
```

## EIR_handbook 
### d/escalation proceedures
Follow Alert plans, playbook processes.
### Alert plans
#### Communications:
On case of suspected breach:
- Client, Box, must receive an executive summary.
- Box Production Manager must receive information highlighting major security breach events, and listed potential impacts on company operations.
- Third-Party provider must a receive full report, with actionable items included.
### phone#, email@
- [view contacts](#case_contacts)

## Alert plans
Communications:
On case of suspected breach,
- Percy, percy@box.cat must receive an executive summary.
- Box Production Manager must receive highlighting [major security breach events](), and listed potential impacts on company operations.
    Third-Party provider must a receive full report, with actionable items included.

## SOC-Operational_handbook
## #Phishing Playbook
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

On the potential victim machine, look for and ask about:
- [ ] Did they follow any email url, produce any clicks, see any opens.
- [ ] Did they reply with sensitive informaiton/secrets/access.
- [ ] Noticed unsual processes, behaviours, CPU use (heat, sound, slowness), Bandwidth use.
continue to 1.2

1.2. Extract (embedded) URLs from email content. Resolve the URLs to IPs. Check for IP reputation.

Mark ‘true positive’ if bad IP and escalate the collected information.
- [ ] True postivie

1.3 Notify MSSP

1.3.1. As an [Intake Analyst](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/Intake%20Analyst.md) open a ticket for a potential Phishing attack, forward collected informaiton to MSSP.

<!--[ticket template](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D3/email-template/in-class-ticket-response-email.md#ticket-234)-->
```
Ticket Summary
Phishing attack at <time date>, <UI confirmed, bad ip, possible infection, >

Ticket Description
Victim opened phishing email and <opened urls with bad ip, reports performance symptoms, replied with sesitive info.>

Included:
- Reported email (screenshot,code).
- List of URL resolved IPs. (text)
- Victim email (text)

Now gathering additonal informaiton.
```
1.3.2 Send a short notice of vigiliance for phishing email to production organization members.

- [!IMPORTANT]
- Stay alert for contact from MSSP on open ticket. ASAP respond/perform provided requests/guidelines.

1.4 Gather further infomation
1.4.1  Query the email server, find other correlated emails with the reported email.

Use automated services if available. If needed, contact IT or/and Database roles. Gather the following information:
- Recipient
- Source IP, Port
- Destination IP, Port
- URLs / Embeded URLs
- Mail text content: Headers, Body

1.5. Use automation tools if available to resolve collected URLs to IPs. Check the reputation of collected source IPs, URL IPs.

- [x] Mark ‘true positive’ if bad IP and escalate the collected information


1.5 Analyze URLs in sandboxed environment by
following the


1.1 Analyze the precursors and indicators
1.2 Look for correlating information
1.3 Perform research (e.g., search engines, knowledge base)
1.4 As soon as the handler believes an incident has occurred, begin documenting
the investigation and gathering evidence
3. Prioritize handling the incident based on the relevant factors (functional impact, information
impact, recoverability effort, etc.)
#### Containment, Eradication, and Recovery
4. Report the incident to the appropriate internal personnel and external organizations
Containment, Eradication, and Recovery
5. Acquire, preserve, secure, and document evidence
6. Contain the incident
7. Eradicate the incident
6.1 Identify and mitigate all vulnerabilities that were exploited
6.2 Remove malware, inappropriate materials, and other components
6.3 If more affected hosts are discovered (e.g., new malware infections), repeat
the Detection and Analysis steps (1.1, 1.2) to identify all other affected hosts, then
contain (5) and eradicate (6) the incident for them
7.1 Return affected systems to an operationally ready state
7.2 Confirm that the affected systems are functioning normally
7.3 If necessary, implement additional monitoring to look for future related activity
#### Post-Incident Activity
8. Recover from the incident
9. Create a follow-up report
10. Hold a lessons learned meeting (mandatory for major incidents, optional otherwise

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
