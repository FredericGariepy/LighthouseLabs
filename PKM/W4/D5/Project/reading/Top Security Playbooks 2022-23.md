
## Table of Contents
- [Reaading](https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf)
- Brute Force Attacks
- Phishing Attacks
- Ransomware
- Command-and-Control (C2) Traffic
- Insider Threat (Data Leakage)
- Impossible Travel
- Cloud Misconfigurations
- Suspicious Logins


## Glosary 
| term | def|
|-|---|
|SOAR|Security Orchestration, Automation, Response|
|SecOps |Security Operations|


## Brute Force Attacks
Generally, the attacker has either:
a. reverse engineered or
b. purchased on the dark web legitimate usernames and applies a vast library of potential passwords to gain access

Enrichment & Context
· Source IP address –is it internal or external
· Target IP and OS information

Investigation

a) If __internal IP__:
Search of any previous alerts raised on the entity (source IP). 
The machine might be already compromised and might still be compromised.
- I) If the alerts are involving a malware alert, escalate the case to Tier 2.
- II) Tier 2: Block the traffic from the source IP, disinfect the machine, verify the source of the malware and unblock the machine once no threats are found.

b) If __External IP__:
Search the IP using IP reputation sites and act accordingly (continue the next steps of this playbook to gather information for Tier 2).|


