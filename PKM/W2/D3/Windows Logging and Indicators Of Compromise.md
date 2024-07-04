Made with AI (ChatGpt 3.5)
# Windows Logging and Indicators Of Compromise

[MITRE ATT&CK Tour](https://attack.mitre.org)

here are the names of the categories:
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


## Task workflow:
[Find a Category technique](https://attack.mitre.org/) -> [Find a related windows event](https://www.socinvestigation.com/most-common-windows-event-ids-to-hunt-mind-map/) -> [explore the event](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/)


## Account Manipulation & indows Security Log Event ID 4720 
MITRE ATT&CK: [Tactics > Persistence > Account Manipulation](https://attack.mitre.org/techniques/T1098/)
> Adversaries may manipulate accounts to maintain and/or elevate access to victim systems.
Related windows event: Windows Security Log Event ID 4720
> 
[4720: A user account was created](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4720)
> The user identified by Subject: created the user identified by New Account:.
> Attributes show some of the properties that were set at the time the account was created.
>  Notice account is initially disabled.

Examples of 4720
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



