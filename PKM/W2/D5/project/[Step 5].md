Workflow:
1. ~~List assets, describe OS / software versions~~
2. ~~List labeled assets in descending priority, based on category.~~
3. ~~Assign CIA value to asset~~
4. ~~Assign SIL value to asset~~
5.  [Assets](#assets) ~~Add related vulnerabilties (search MITRE, CVE , NVD)~~
6. Calculate(vuln + asset SIL) to get CVSS Scores
___
5. Add related vulnerabilties.
Resources
- [NIST NVD](https://nvd.nist.gov/vuln/search)
- [CVSS](https://www.first.org/cvss/calculator/3.1)
- [MITRE CVE & ATT&CK](https://attack.mitre.org/)
- [Cyber Kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)
___
## assets
# Asset Vulnerabilities 

### Marketing (P)
> [Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | Known as: version 23H2, Sun Valley 3](https://en.wikipedia.org/wiki/Windows_11,_version_23H2#:~:text=The%20Windows%2011%202023%20Update,22631.)
> 
- Marketing SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
- Marketing SIL = High
- [Phishing for Information](https://attack.mitre.org/techniques/T1598/)
- [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)


### Sales (F) & (P)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
- Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
- Sales SIL = High
- [Phishing for Information](https://attack.mitre.org/techniques/T1598/)
- [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)
 
### Developer Machines (IP)
> Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
> Services with LISTENING PORTS:
> | Service      | Port            |
> |--------------|-----------------|
> | apache2      | *:80            |
> | mysqld       | 33060 \| 3306    |
- Developer Machines SC = {(confidentiality, High), (integrity, Moderate), (availability, Low)}
- Developer Machines SIL = High
- [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
- [Service Stop](https://attack.mitre.org/techniques/T1489/)

### Management functions (A)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
- Management SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
- Management SIL = High

### PRTG Network Monitor (SM)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> 
> PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315
- PRTG Network Monitor SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
- PRTG Network Monitor SIL = Moderate
- [Compromise Infrastructure: Server](https://attack.mitre.org/techniques/T1584/004/)
- [Application Log](https://attack.mitre.org/datasources/DS0015/)


### SQL database (S)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)
-  SQL database SC = {(confidentiality, Low), (integrity, low), (availability, Moderate)}
-  SQL database SIL = Moderate


### Internet Information Services (IIS) webserver (S)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> 
> IIS Version 10.0
-  IIS webserver SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, low)}
-  IIS webserver SIL = Moderate
-  [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
-  [Server Software Component: IIS Components](https://attack.mitre.org/techniques/T1505/004/)

### Test System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
-  Test System SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
-  Test System SIL = Moderate


### IT System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
-  IT System SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
-  IT System SIL = Moderate


___

Denial of Service (DoS) Attacks

PRTG Sensor: QoS (Quality of Service) Round Trip Sensor
IoC: Sudden increase in network latency or packet loss


Port Scanning and Unauthorized Access Attempts

PRTG Sensor: Port Sensor, SNMP Traffic Sensor
IoC: Unusual number of connection attempts on multiple ports


Bandwidth Saturation (potential DDoS)

PRTG Sensor: SNMP Traffic Sensor, NetFlow Sensor
IoC: Sudden spike in network traffic volume


Abnormal System Resource Usage

PRTG Sensor: Windows CPU Load Sensor, Linux CPU Load Sensor
IoC: Unusually high CPU or memory usage, which could indicate malware or cryptomining


Unauthorized File System Changes

PRTG Sensor: Folder Sensor
IoC: Unexpected changes in critical system folders


Suspicious Process Activity

PRTG Sensor: Windows Process Sensor
IoC: Appearance of unknown processes or unexpected behavior of known processes


DNS Query Anomalies (potential DNS tunneling)

PRTG Sensor: DNS Query Sensor
IoC: Unusual volume or pattern of DNS queries


SSL Certificate Issues

PRTG Sensor: SSL Security Check Sensor
IoC: Expired certificates, weak encryption, or untrusted CAs


Email Server Anomalies

PRTG Sensor: IMAP Sensor, POP3 Sensor
IoC: Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns


Database Performance Issues

PRTG Sensor: Microsoft SQL Server Sensor
IoC: Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts


Unusual Network Connections

PRTG Sensor: Ping Sensor, Port Sensor
IoC: New connections to unfamiliar IP addresses or on unexpected ports


Web Server Vulnerabilities

PRTG Sensor: HTTP Advanced Sensor, HTTP Full Web Page Sensor
IoC: Unusual response codes, increased error rates, or changes in response time
