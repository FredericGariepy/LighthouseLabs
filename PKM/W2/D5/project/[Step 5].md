Workflow:
1. ~~List assets, describe OS / software versions~~
2. ~~List labeled assets in descending priority, based on category.~~
3. ~~Assign CIA value to asset~~
4. ~~Assign SIL value to asset~~
5.  [Assets](#assets) ~~Add related vulnerabilties (search MITRE, CVE , NVD)~~ Difficult part
6. Calculate(vuln + asset SIL) to get CVSS Scores
___
5. Add related vulnerabilties.
Resources
- [NIST NVD](https://nvd.nist.gov/vuln/search)
- [CVSS](https://www.first.org/cvss/calculator/3.1)
- [MITRE CVE & ATT&CK](https://attack.mitre.org/)
- [Cyber Kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)
___
## Network Asset sensors

- | Sensor: Bandwidth Usage Sensor [SNMP Traffic Sensor](https://www.paessler.com/manuals/prtg/snmp_traffic_sensor)
- | Description: The SNMP Traffic sensor monitors traffic on a device via the Simple Network Management Protocol (SNMP). Monitors network bandwidth usage.
- |	System : All. Router Interface. 
- | IoCs:[Network Denial of Service](https://attack.mitre.org/techniques/T1498/), [Exfiltration](https://attack.mitre.org/tactics/TA0010/)
- | Associated Rationale: Network bandwith baselines is a vital sign of a network. Indicating potential DDoS attacks, Exfiltration of data and other unusal network events.
- |	Priority (SIL): 
- |	Thresholds / Assumptions : Thresholds: Traffic In, Traffic Out : 0.03mbits Upper bound. Total Traffic 0.43mbits Upper Bound.





## OS specific sensors

### Windows


- | Sensor: [WMI Security Center Sensor](https://www.paessler.com/manuals/prtg/wmi_security_center_sensor)
- | Description: Status Sensor	Monitors antivirus software status.	The WMI Security Center sensor monitors the security status of a Windows client system via Windows Management Instrumentation (WMI). It can monitor all security products that are controlled by Windows Security Center / Windows Action Center.
- |	System : [Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | Known as: version 23H2, Sun Valley 3](https://en.wikipedia.org/wiki/Windows_11,_version_23H2#:~:text=The%20Windows%2011%202023%20Update,22631.)
- | IoCs : [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)
- | Associated Rationale: Ensuring that antivirus 
- |	Priority (SIL) : High
- |	Thresholds / Assumptions :


- | Sensor: [WMI Event Log Sensor](https://www.paessler.com/manuals/prtg/wmi_event_log_sensor)
- | Description: Monitors Windows event logs. The WMI Event Log sensor monitors a Windows log file via Windows Management Instrumentation (WMI).
- |	System :[Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | Known as: version 23H2, Sun Valley 3](https://en.wikipedia.org/wiki/Windows_11,_version_23H2#:~:text=The%20Windows%2011%202023%20Update,22631.)
- | IoCs: [Indicator Removal: Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/), [Brute Force](https://attack.mitre.org/techniques/T1110/)
- | Associated	Rationale : Use the sensor to monitor event logs. 
- |	Priority (SIL) : High. Event logs are the bedrock of reconnaissance & intrusion detection.
- |	Thresholds / Assumptions : Narrow down to event down to any attribute (type, Event ID, user, message, etc). Additonally Set-up (trap) Task related to important events. Use event ID 104/1102 for Indicator Removal: Clear Windows Event Logs. Use Event ID 33205 for Brute Force attempts.

  
### Linux
- | Sensor: [File Content Sensor](https://www.paessler.com/manuals/prtg/file_content_sensor)
- | Description: Monitors changes to files and directories. The File Content sensor checks a text file (for example, a log file) for certain strings.
- |	Systems : Kali GNU/Linux (debian) version 2024.2 (kali-rolling). Ubuntu Linux (debian) 22.04.4 LTS (Jammy Jellyfish).
- | IoCs: [Indicator Removal: Clear Linux or Mac System Logs](https://attack.mitre.org/techniques/T1070/002/) ,
- | Associated	Rationale: Logs are the bedrock of reconnaissance and intrusion detection. Linux machines on the network contain IP and System information data.
- |	Priority (SIL) : High.
- |	Thresholds / Assumptions : Monitoring of specific files will be in place, this can include syslog file, Access log files, application log files. 


## Specific Information Asset Sensors

### Marketing (P)
> Microsoft Windows 11, version 23H2, (Sun Valley 3)
>
> Marketing SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
>
> Marketing SIL = High

- | Sensor:
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

- [Phishing for Information](https://attack.mitre.org/techniques/T1598/)
- [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)


### Sales (F) & (P)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
>
> Sales SIL = High

- | Sensor:
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

- [Phishing for Information](https://attack.mitre.org/techniques/T1598/)
- [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)

 
### Developer Machines (IP)
> Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
>
> IT Developer Machines SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> IT Developer Machines SIL = Moderate 
>
> Services with LISTENING PORTS:
> | Service      | Port            |
> |--------------|-----------------|
> | apache2      | *:80            |
> | mysqld       | 33060 \| 3306    |


- | Sensor: [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)
- | Description:  sensor monitors a database on a MySQL server and executes a query.
- |	System : Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
- | IoCs: https://attack.mitre.org/techniques/T1210/
- | Associated	Rationale : 
- |	Priority (SIL) ; 
- |	Thresholds / Assumptions :  (State Threshold Change)


- | Sensor:
- | Description:  sensor monitors a database on a MySQL server and executes a query.
- |	System : Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
- | IoCs: Check if query 
- | Associated	Rationale : 
- |	Priority (SIL) ; 
- |	Thresholds / Assumptions :
- 



> Developer Machines SC = {(confidentiality, High), (integrity, Moderate), (availability, Low)}
>
>  Developer Machines SIL = High

### *default sensor
- | Sensor: HTTP Load Time
- | Description: Monitors the time it takes for the page to load.
- |	System: Linux
- | IoCs: Malicious Redirects, DDoS Attacks, Content Injection	Unexpected changes in load time can indicate anomalies or performance-related issues that could indicate a security breach or compromise.
- | Associated	Rationale : Linux web server being internal and outward facing (Assumption)
- |	Priority (SIL): Medium (SIL of high, see assumptions)
- |	Thresholds / Assumptions: SIL based on the fact that *BIG DOG does NOT have a large Web Presence*, the Low impact on availability, higher chance of compromise. 




- | Sensor: 
- | Description: 
- |	System
- | IoCs: [Password spraying](https://attack.mitre.org/techniques/T1110/003/)
- | Associated	Rationale: Password spraying "Commonly targeted services [...] MySQL (3306/TCP)" 
- |	Priority (SIL)
- |	Thresholds / Assumptions


- [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
- [Service Stop](https://attack.mitre.org/techniques/T1489/)



### Management functions (A)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Management SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>
> Management SIL = High
- | Sensor:
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions


### PRTG Network Monitor (SM)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> 
> PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315
> PRTG Network Monitor SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> PRTG Network Monitor SIL = Moderate
- | Sensor:
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

- [Compromise Infrastructure: Server](https://attack.mitre.org/techniques/T1584/004/)
- [Application Log](https://attack.mitre.org/datasources/DS0015/)


### SQL database (S)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)
-  SQL database SC = {(confidentiality, Low), (integrity, low), (availability, Moderate)}
-  SQL database SIL = Moderate

- | Sensor:  [Ping](https://www.paessler.com/manuals/prtg/ping_sensor)
- | Sensor:  [Port](https://www.paessler.com/manuals/prtg/port_sensor)
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

Typically, management services over commonly used ports are used when password spraying. Commonly targeted services include the following:

SSH (22/TCP)
Telnet (23/TCP)
FTP (21/TCP)
NetBIOS / SMB / Samba (139/TCP & 445/TCP)
LDAP (389/TCP)
Kerberos (88/TCP)
RDP / Terminal Services (3389/TCP)
HTTP/HTTP Management Services (80/TCP & 443/TCP)
MSSQL (1433/TCP)
Oracle (1521/TCP)
MySQL (3306/TCP)"


- | Sensor: 
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

### Internet Information Services (IIS) webserver (S)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> 
> IIS Version 10.0 | IIS webserver SIL = Moderate

- | Sensor: FTP Sensor
- | Description: Monitors FTP access and usage. Monitors specified TCP/IP port request response time and status (accepted).
- |	System: Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
- | IoCs: [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/) higher response time as machine is sprayed by password attempts.
- | Associated	Rationale : Port 22 is used for remote ssh login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unsual SSh attempts.
Brute forcing attacks could occur since Test Systems might not be as a thoroughly configured (passwords, IDs, default settings) hence opening them up for attacks.
- |	Priority (SIL) : Moderate SIL (low Integrity, low Availability)
- |	Thresholds / Assumptions : Upper bound thresholds response time < 80ms. This sensor is likely used less often and so the baseline should be tigher in order notice disturbances. Test Services may contain key strategic informaiton for future planning of attackers. 

- | Sensor: [Windows IIS Application Sensor](https://www.paessler.com/manuals/prtg/wmi_iis_application_sensor)
- | Description: Motonitors IIS server via Windows Management Instrumentation (WMI). Sensor gives insights into the performance, availability, and usage of the IIS server.
- |	System : Microsoft Windows 11 Home, 23H2: IS Version 10.0
- | IoCs : [Server Software Component: IIS Components](https://attack.mitre.org/techniques/T1505/004/)
- | Associated	Rationale : 
- |	Priority (SIL) : Moderate
- |	Thresholds / Assumptions : The IIS server serves up the website. IIS server may be used for FTP
  


-  [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
-  [Server Software Component: IIS Components](https://attack.mitre.org/techniques/T1505/004/)
-  Denial of Service (DoS) Attacks
   - PRTG Sensor: QoS (Quality of Service) Round Trip Sensor
   > IoC: Sudden increase in network latency or packet loss
- Port Scanning and Unauthorized Access Attempts
   - PRTG Sensor: Port Sensor, SNMP Traffic Sensor
   > IoC: Unusual number of connection attempts on multiple ports
  
  Windows VM running services:
  ```cmd
   ProcessName FileVersion LocalPort  State
    ----------- ----------- ---------  -----
    services                    49669 Listen
    spoolsv                     49668 Listen
    wininit                     49665 Listen
    lsass                       49664 Listen
    System                        445 Listen
    svchost                       135 Listen
  ```

  #### Recomendations:

### Test System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> Test System SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>
> Test System SIL = Moderate

- | Sensor:
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

- | Sensor: SSH Sensor
- | Description: Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).
- |	System: Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
- | IoCs: [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/) higher response time as machine is sprayed by password attempts.
- | Associated	Rationale : Port 22 is used for remote ssh login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unsual SSh attempts.
Brute forcing attacks could occur since Test Systems might not be as a thoroughly configured (passwords, IDs, default settings) hence opening them up for attacks.
- |	Priority (SIL) : Moderate SIL (low Integrity, low Availability)
- |	Thresholds / Assumptions : Upper bound thresholds response time < 80ms. This sensor is likely used less often and so the baseline should be tigher in order notice disturbances. Test Services may contain key strategic informaiton for future planning of attackers. 


### IT System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> IT System SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> IT System SIL = Moderate


- | Sensor: SSH Sensor
- | Description: Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).
- |	System: Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
- | IoCs: [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/) higher response time as machine is sprayed by password attempts.
- | Associated	Rationale : Port 22 is used for remote ssh login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unsual SSh attempts.
- |	Priority (SIL) : Moderate SIL
- |	Thresholds / Assumptions : Upper bound thresholds response time < 100ms. This sensor is 

IoC: 


- | Sensor:
- | Description: 
- |	System
- | IoCs
- | Associated	Rationale
- |	Priority (SIL)
- |	Thresholds / Assumptions

___







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
