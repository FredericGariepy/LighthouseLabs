Made with AI (ChatGpt 3.5)
<!-- Hey fancy seeing you here -->
###### Heya LHL cohort👋 right here is the response:
➡️ [Click here: Jump to task response](#response) ⬅️
🐜
# Windows Logging and Indicators Of Compromise (IoC)
## Task workflow:
[Find a Category technique For Windows](https://attack.mitre.org/matrices/enterprise/windows/) -> [Find a related windows event](https://www.socinvestigation.com/most-common-windows-event-ids-to-hunt-mind-map/) -> [explore the event](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/)

[MITRE ATT&CK](https://attack.mitre.org) here are the names of the categories:
1. Reconnaissance
2. Resource Development
3. Initial Access
4. Execution
5. Persistence
6. Privilege Escalation
7. Defense Evasion
8. Credential Access
9. Discovery
10. Lateral Movement
11. Collection
12. Command and Control
13. Exfiltration
14. Impact

Windows event Logs:

<img src="https://www.socinvestigation.com/wp-content/uploads/2021/11/f31ff3a9905b418680a4e722cc57b316-0001-1920x601.jpg" alt="Image Description" width="800" height="370">

image: [Image url](https://www.socinvestigation.com/wp-content/uploads/2021/11/f31ff3a9905b418680a4e722cc57b316-0001-1920x601.jpg)

## Key Takeaways
The Windows Logging and Indicators of Compromise are used to identify patterns of IoCs.

- IoCs are often categorized by event ID.

The categorization of event IDs represents a commensurate relationship to vulnerabilities as shown in the MITRE ATT&CK matrix.
---
## response
# 3 Examples of IoC with Event Log ID 😸
- [Example 1](#example-1) Lateral Movement (Remote Service)
- [Example 2](#example-2)


## Example 1 
## Lateral Movement (Remote Service) & Windows Security Log Event ID 4624 
The adversary is trying to move through your environment.

[Remote Service](https://attack.mitre.org/techniques/T1021/)
Adversaries may use Valid Accounts to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

Windows Event log [ID  4624: An account was successfully logged on](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4624)

This is a highly valuable event since it documents each and every successful attempt to logon to the local computer regardless of logon type, location of the user or type of account.  You can tie this event to logoff events 4634 and 4647 using Logon ID.

#### description (AI made):
Windows Security Log Event ID 4624 records successful logons to a local computer, providing crucial information for security auditing.

It includes details like logon type, process information, network information, and user account details.

The event ties to logoff events 4634 and 4647 via Logon ID. Newer Windows versions add fields like Impersonation Level, Virtual Account, and Elevated Token. Logon Type indicates the logon method, ranging from interactive logons to remote and service logons. The event helps in tracking user activities and detecting potential security incidents, making it essential for system monitoring and auditing.


## Example 2
## Persistence (Account Manipulation) & Windows Security Log Event ID 4720 
Persistence: The adversary is trying to maintain their foothold.
> Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code.

MITRE ATT&CK: [Tactics > Persistence > Account Manipulation](https://attack.mitre.org/techniques/T1098/)

Adversaries may manipulate accounts (create or modify accounts) to maintain and/or elevate access to victim systems.
Related windows event: Windows Security Log Event ID 4720

WIndows Event log [ID 4720: A user account was created](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4720)

#### description (AI made):

Windows Security Log Event ID 4720 is crucial for security monitoring as it records the creation of user accounts.

It captures comprehensive details, including the security ID, account name, and domain of both the creator and the new account.

Attributes logged include SAM account name (SAM: Security Accounts Manager), display name, and user account control settings like 'Account Disabled' and 'Password Not Required'. This event is vital for tracking changes in user account management and detecting unauthorized account creations, applicable across Windows 7 to Windows Server 2022.

Example of 4720 log
```
A user account was created.

Subject:

   Security ID:  ACME-FR\administrator
   Account Name:  administrator
   Account Domain:  ACME-FR
   Logon ID:  0x20f9d

New Account:

   Security ID:  ACME-FR\John.Locke
   Account Name:  John.Locke
   Account Domain:  ACME-FR

Attributes:

   ...
   User Principal Name: John.Locke@acme-fr.local
   Home Directory:  -
   Home Drive:  -
   Script Path:  -
   Profile Path:  -
   ...

Additional Information:

   Privileges  ...
```

