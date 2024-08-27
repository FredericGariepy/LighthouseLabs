__________
Encryption:

Symmetric (Block Cipher: AES | Stream ciphers: ?)

Insecure symmetric algorithm: DES (short 56-bit key size)

Asymmetric (RSA, ECC)

RSA in linux with gpg:
https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages
________
Hashing:

https://web.compass.lighthouselabs.ca/p/14/8ddafccb-fecc-4af5-b154-03286db2d71d

Insecure Hashes: SHA-1, MD4
_______________
NIST RMF steps:

Prepare, Categorize, Select, Implement, Asses, Authorize, Monitor
_________________________
NIST CSF version 1 Steps: \
Identify, Protect, Detect, Response, Recover

NIST CSF version 2 steps: \
Govern (center), Identify, Protect, Detect, Response, Recover
_______________________
NIST CSF vs. ISO 27001:
- CSF is a guide, ISO is a compliance standard.
- ISO requires an audit for certification, CSF offers no certification as it is a guide.
- Mature organizations will tend to ISO certification, early stage organizations will tend to start with CSF.
- CSF is FREE, ISO is not.
_____________
Policy steps: \
Statement, Implementation, Compliance and Consequence, Review and Update
_________
IR steps: \
Prepare, Detection + Analysis, Containment + Eradication + Recovery, Post-Incident Activity
_____________________________________
Governance, Risk and Compliance (GRC) \
https://complianceforge.com/governance-risk-compliance-grc/

PDCA approach:
1. Plan
2. Do
3. Check
4. Act
_______________
Vulnerabilities  

https://web.compass.lighthouselabs.ca/p/cyber/days/w05d2/activities/3011

Categories of Vulnerabilities:
- People
- Network
- Hardware
- Software

TOOLS:
- Common Weakness Enumeration (CWE)
https://cwe.mitre.org/

- National Vulnerability Database (NVD)
https://nvd.nist.gov/

- Common Vulnerabilities and Exposures (CVE)
https://www.cve.org/

_______________________
Greenbone Architecture:

https://greenbone.github.io/docs/latest/architecture.html
__________________
SIEM Architecture:

https://web.compass.lighthouselabs.ca/p/14/a2906311-e2ba-4350-bd2c-10ceb315819f

SIEM Components:
- Data collection
- Data storage
- Data processing
- Event Management software
- Reporting and visualization module
- Integration with Other security tools
_______________________________
Cyber Threat Intelligence (CTI):

https://web.compass.lighthouselabs.ca/p/14/9d40f895-0ef6-4346-ac65-65216edcbb21

CTI Lifecycle:
1. Planning and Requirements
2. Information Collection
3. Processing
4. Analysis
5. Dissemination

Types of CTI:
- Strategic Intelligence
- Operational Threat Intelligence
- Tactical Threat Intelligence
_______________
Threat Hunting:

https://web.compass.lighthouselabs.ca/p/cyber/days/w08d1/activities/3117

Threat Hunting Steps:
1. Hypothesis
2. Collect and process data
3. Trigger
4. Investigation
5. Response & Resoluton
_____
CVSS:

https://www.first.org/cvss/v3.1/specification-document

The Common Vulnerability Scoring System (CVSS) is: \
 an open framework for communicating the characteristics and severity of software vulnerabilities.

CVSS 3 Metric groups:
- Base
- Temporal
- Environmental. 
_____________
MITRE ATT&CK:
- Tactics: What attackers are trying to achieve
- Techniques: How they accomplish those steps or goals.

Tactics List:
- Reconnaissance
- Resource Development
- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Command and Control
- Exfiltration
- Impact
_______________________________________
Lockheed Martin Cyber kill chain steps:

Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control C2, Action on Objectives.
______________
Diamond Model:

https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/diamond-model-intrusion-analysis/

Diamond Model 4 components:
- Adversary
> The attacker or group responsible for a cyber incident.
- Infrastructure
> The technical resources or assets the adversary uses during the attack (e.g., servers, domains, and IP addresses).
- Capability
> A method, tool, or technique the adversary uses during the attack (e.g., malware or exploits).
- Victim
> The individual or organization the adversary targets during the attack.
_____________________________________________
Cybersecurity Team roles (Blue, Red, Purple):
- Red: Attacker
- Blue: Defender
- Purple: Defender learns from attacker
https://danielmiessler.com/p/red-blue-purple-teams/
_______________
Forensic steps:
1. Identification
2. Preservation
3. Collection
4. Analysis
5. Reporting

______________
TI2 ALL TOPICS
```
    Python scripts to improve cyber security
    Role of Blue, red and purple teams
    SOC Operations and Incident handling
    Security Policies - GRC requirements, GRC recommendations
    Vulnerability assessments - NVD, CVSS
    Incident response - using NIST RMF steps
    IR playbooks, remediation and mitigations
    Encryption - TBC
    Threat defense operations - using MITRE ATT&CK and Lockheed
    Martin Cyber kill chain models
    IDS Monitoring
    Using SIEM system, identify IoCs
    Forensics
    Describe role of forensics
    Investigate and analyze digital evidence
    Registry forensics
    Malware analysis
```
