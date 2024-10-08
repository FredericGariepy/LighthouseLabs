Workflow:
1. ~~List assets, describe OS / software versions~~
2. ~~List labeled assets in descending priority, based on category.~~
3. ~~Assign CIA value to asset~~
4. ~~Assign SIL value to asset~~
5.  [Assets](#assets) ~~Add related vulnerabilties (search MITRE, CVE , NVD)~~ Difficult part
6.  Calculate(vuln + asset SIL) to get CVSS Scores
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

- | Sensor:  [Ping](https://www.paessler.com/manuals/prtg/ping_sensor)
- | Description: The Ping sensor sends an Internet Control Message Protocol (ICMP) echo request ("ping") from the probe system to the parent device to monitor its availability.
- |	System : ALL
- | IoCs : DDoS.
- | Associated Rationale: This is simple, low resource use and reliable PING sensor. It is a default sensor and is used to test network connectivity.
- |	Priority (SIL): Low
- |	Thresholds / Assumptions : Device Downtime, Packet Loss, Ping time. Although ping is not a cornerstone of cyber security is helps establish a reliable baseline of network connectivity and can detect interuptions and unusual downtime on the network.



## OS specific sensors

### Windows


- | Sensor: [WMI Security Center Sensor](https://www.paessler.com/manuals/prtg/wmi_security_center_sensor)
- | Description: Status Sensor	Monitors antivirus software status.	The WMI Security Center sensor monitors the security status of a Windows client system via Windows Management Instrumentation (WMI). It can monitor all security products that are controlled by Windows Security Center / Windows Action Center.
- |	System : [Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | Known as: version 23H2, Sun Valley 3](https://en.wikipedia.org/wiki/Windows_11,_version_23H2#:~:text=The%20Windows%2011%202023%20Update,22631.)
- | IoCs : [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)
- | Associated Rationale: Ensuring that antivirus is Up to date and Running is enssential for the security of a Windows machine.
- |	Priority (SIL) : High
- |	Thresholds / Assumptions: Statuses: Up (Running & Up To Date), Warning (Running & Out Of Date), Down (Not Running &  Out Of Date). 


- | Sensor: [WMI Event Log Sensor](https://www.paessler.com/manuals/prtg/wmi_event_log_sensor)
- | Description: Monitors Windows event logs. The WMI Event Log sensor monitors a Windows log file via Windows Management Instrumentation (WMI).
- |	System :[Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | Known as: version 23H2, Sun Valley 3](https://en.wikipedia.org/wiki/Windows_11,_version_23H2#:~:text=The%20Windows%2011%202023%20Update,22631.)
- | IoCs: [Indicator Removal: Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/), [Brute Force](https://attack.mitre.org/techniques/T1110/), [Application Log](https://attack.mitre.org/datasources/DS0015/)
- | Associated	Rationale : Use the sensor to monitor event logs. 
- |	Priority (SIL) : High. Event logs are the bedrock of reconnaissance & intrusion detection.
- |	Thresholds / Assumptions : Narrow down to event down to any attribute (type, Event ID, user, message, etc). Additonally Set-up (trap) Task related to important events. Use event ID 104/1102 for Indicator Removal: Clear Windows Event Logs. Use Event ID 33205 for Brute Force attempts.


- | Sensor: Sensitivie folder sensor [Folder Sensor](https://www.paessler.com/manuals/prtg/folder_sensor)
- | Description: The Folder sensor monitors a folder via Server Message Block (SMB). You can monitor file changes and file ages.
- |	System : Microsoft Windows 11 Home, version 23H2 (Sun Valley 3)
- | IoCs : [File and Directory Permissions Modification: Windows File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222/001/)
- | Associated	Rationale : Detect unexpected changes in critical system folders.
- |	Priority (SIL) : Moderate
- |	Thresholds / Assumptions: File Count, Folder Size, file modifications.

  
### Linux
- | Sensor: Sensitive file sensor: [File Content Sensor](https://www.paessler.com/manuals/prtg/file_content_sensor)
- | Description: Monitors changes to files and directories. The File Content sensor checks a text file (for example, a log file) for certain strings.
- |	Systems : Kali GNU/Linux (debian) version 2024.2 (kali-rolling). Ubuntu Linux (debian) 22.04.4 LTS (Jammy Jellyfish).
- | IoCs: [Indicator Removal: Clear Linux or Mac System Logs](https://attack.mitre.org/techniques/T1070/002/), [Application Log](https://attack.mitre.org/datasources/DS0015/)
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

- | Sensor: Email sensor [IMAP Sensor](https://www.paessler.com/manuals/prtg/imap_sensor)
- | Description: The IMAP sensor monitors an email server via the Internet Message Access Protocol (IMAP) unlike POP3 sensors.
i_round_blueThe sensor can check the content of emails for certain keywords. 
- |	System : Microsoft Windows 11, version 23H2, (Sun Valley 3). Marketing Workstation
- | IoCs : [Phishing for Information](https://attack.mitre.org/techniques/T1598/) ,[Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)
- | Associated	Rationale : Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns
- |	Priority (SIL) : High
- |	Thresholds / Assumptions: Email Count, Search String in email (potentailly integrating with AI for detection).


### Sales (F) & (P)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
>
> Sales SIL = High

- | Sensor: Email sensor [IMAP Sensor](https://www.paessler.com/manuals/prtg/imap_sensor)
- | Description: The IMAP sensor monitors an email server via the Internet Message Access Protocol (IMAP) unlike POP3 sensors.
i_round_blueThe sensor can check the content of emails for certain keywords. 
- |	System : icrosoft Windows 11, version 23H2, (Sun Valley 3). Sales Workstation.
- | IoCs : [Phishing for Information](https://attack.mitre.org/techniques/T1598/) ,[Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)
- | Associated	Rationale : Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns
- |	Priority (SIL) : High
- |	Thresholds / Assumptions: Email Count, Search String in email (potentailly integrating with AI for detection).

 
### Developer Machines (IP)
> Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
>
> IT Developer Machines SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)} 
> 
> IT Developer Machines SIL = High 
>
> Services with LISTENING PORTS:
> | Service      | Port            |
> |--------------|-----------------|
> | apache2      | *:80            |
> | mysqld       | 33060 \| 3306    |

> Developer Machines SC = {(confidentiality, High), (integrity, Moderate), (availability, Low)}
>
>  Developer Machines SIL = High

- | Sensor: [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)
- | Description:  sensor monitors a database on a MySQL server and executes a query.
- |	System : Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish). Developer Server.
- | IoCs: [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)
- | Associated	Rationale : Checks for the Integrity and Availability of the SQL database. As seen in listed ports, the Linux VM has mysqld ports LISTENING.
- |	Priority (SIL) : High
- |	Thresholds / Assumptions : Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts.

- | Sensor: [HTTP Apache ModStatus PerfStats Sensor](https://www.paessler.com/manuals/prtg/http_apache_modstatus_perfstats_sensor)
- | Description: The HTTP Apache ModStatus PerfStats sensor monitors performance statistics of an Apache web server over HTTP.
- |	System : Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish). Developer Server.
- | IoCs: 
- | Associated	Rationale : Attackers may try to attack the availability of the appache 2 server.
- |	Priority (SIL) : High
- |	Thresholds / Assumptions : CPULoad, Workers Idle/Busy, Requests Per Second, UP/DOWN time

- | Sensor: SSH Sensor [Port Sensor](https://www.paessler.com/manuals/prtg/port_sensor)
- | Description: Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).
- |	System: Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
- | IoCs: [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/), [Password spraying](https://attack.mitre.org/techniques/T1110/003/)
- | Associated	Rationale : Port 22 is used for remote ssh login. Having a baseline for accessibility will allow to spot spikes in unsual SSh attempts. It is likely that developers use this port for work and it should be monitored.
- |	Priority (SIL) : Moderate SIL (low Integrity, low Availability)
- |	Thresholds / Assumptions : Upper bound thresholds response time < 100ms. Developer SSH port allows acces to HVA as should be monitored.

- | Sensor: [SSH Remote Ping Sensor](https://www.paessler.com/manuals/prtg/ssh_remote_ping_sensor)
- | Description: The SSH Remote Ping sensor remotely monitors the connectivity between a system running Linux/macOS X and another device, using Internet Control Message Protocol (ICMP) echo requests ("ping") and Secure Shell (SSH). We're essentially making sure that two devices (Dev & Dev Server) can establish communication realiably.
- |	System : Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
- | IoCs: [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/), [Service Stop](https://attack.mitre.org/techniques/T1489/)
- | Associated	Rationale: Password spraying "Commonly targeted services [...] MySQL (3306/TCP)" 
- |	Priority (SIL) : High
- |	Thresholds / Assumptions: Packet Loss, Response time (average, max, min), Downtime. This is important to measure in order to ensure that developers have steady access to their environment (availability). A baseline can help establish unusal response times which could be IoC for Adversary-in-the-Middle attacks (confidentiality/integrity).


### Management functions (A)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Management SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>


### PRTG Network Monitor (SM)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> 
> PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315
> PRTG Network Monitor SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> PRTG Network Monitor SIL = Moderate


- | Sensor: [System Health Sensor](https://www.paessler.com/manuals/prtg/system_health_sensor)
- | Description: The System Health sensor monitors the status of the probe system. It checks various system parameters that can affect the quality of the monitoring results. It is automatically created however, but manual creations are possible.
- |	System : Microsoft Windows 11 Home, version 23H2, Sun Valley 3
- | IoCs : [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)
- | Associated	Rationale : This sensor is necessary to monitor the health of the Managing device's own probe system.
- |	Priority (SIL): Moderate
- |	Thresholds / Assumptions: Available Memory , System CPU Load, Downtine. An attack on the availability of the system would cause serrious harm to the very purpose of the probe device.


### SQL database (S)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)
-  SQL database SC = {(confidentiality, Low), (integrity, low), (availability, Moderate)}
-  SQL database SIL = Moderate

- | Sensor: [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)
- | Description:  sensor monitors a database on a MySQL server and executes a query.
- |	System : Microsoft Windows 11 Home, version 23H2, Sun Valley 3
- | IoCs: [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)
- | Associated	Rationale : Checks for the Integrity and Availability of the SQL database.
- |	Priority (SIL) : Moderate
- |	Thresholds / Assumptions : Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts.


### Internet Information Services (IIS) webserver (S)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> 
> IIS Version 10.0 | IIS webserver SIL = Moderate
> 
> IIS webserver SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, low)}
>
> IIS webserver SIL = Moderate
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


- | Sensor: HTTP Load Time
- | Description: Monitors the time it takes for the page to load.
- |	System: Microsoft Windows 11 Home, version 23H2 (Sun Valley 3)
- | IoCs: Malicious Redirects, DDoS Attacks, Content Injection	Unexpected changes in load time can indicate anomalies or performance-related issues that could indicate a security breach or compromise.
- | Associated	Rationale : Linux web server being internal and outward facing (Assumption)
- |	Priority (SIL): Medium (SIL of high, see assumptions)
- |	Thresholds / Assumptions: SIL based on the fact that *BIG DOG does NOT have a large Web Presence*, the Low impact on availability, higher chance of compromise.

  
- | Sensor: [FTP Sensor](https://www.paessler.com/manuals/prtg/ftp_sensor)
- | Description: he FTP sensor monitors file servers via the File Transfer Protocol (FTP) and FTP over SSL (FTPS). Monitors specified FTP port request response time and status (accepted).
- |	System:  Microsoft Windows 11 Home, version 23H2 (Sun Valley 3)
- | IoCs: [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)
- | Associated Rationale : The IIS server can host FTP services which can be used for exfiltration of data.
- |	Priority (SIL) : Moderate
- |	Thresholds / Assumptions : Response time in msec. The Upper bound should indicate a unusual activity.


- | Sensor: [Windows IIS Application Sensor](https://www.paessler.com/manuals/prtg/wmi_iis_application_sensor)
- | Description: Motonitors IIS server via Windows Management Instrumentation (WMI). Sensor gives insights into the performance, availability, and usage of the IIS server.
- |	System : Microsoft Windows 11 Home, version 23H2 (Sun Valley 3).  IS Version 10.0.
- | IoCs : [Server Software Component: IIS Components](https://attack.mitre.org/techniques/T1505/004/), [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
- | Associated	Rationale : The IIS is a webserver public facing, file share server. Such a server can be poisoned and distribute harm internally and externally of the organization.
- |	Priority (SIL) : Moderate
- |	Thresholds / Assumptions : IIS sensor can monitor for bytes and Files (data) sent/received, http requests Get/Post, Status Up/Down, Users Known/Anonymous. It is a Very powerfull sensor which should be used to monitor important IIS operations by the organization.


- | Sensor: [Windows Process Sensor](https://www.paessler.com/manuals/prtg/wmi_process_sensor#channels)
- | Description: The Windows Process sensor monitors a Windows process via Windows Management Instrumentation (WMI) or Windows performance counters, as configured in the Windows Compatibility Options of the parent device.
Microsoft Windows 11 Home, version 23H2 (Sun Valley 3)
- | IoC : [Service Stop](https://attack.mitre.org/techniques/T1489/),
- | Associated	Rationale : A baseline is important to monitor the activity of the organization and monitor for potentiall atacks on availability.
- |	Priority (SIL) : Moderate
- |	Thresholds / Assumptions : CPU, Handles, Instances, Threads, Working Set. Everything to monitor the performannce of the IIS server, since it has a webserver and FTP (inluding Windows Fileshare).


### Test System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> Test System SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>
> Test System SIL = Moderate

- | Sensor: SSH Sensor [Port Sensor](https://www.paessler.com/manuals/prtg/port_sensor)
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


- | Sensor: [Packet Sniffer Sensor](https://www.paessler.com/manuals/prtg/packet_sniffer_header_sensor)
- | Description: Monitors and analyzes network traffic to detect unusual patterns, unauthorized protocols, or suspicious activities within the network. The Packet Sniffer sensor monitors the headers of data packets that pass a local network card using a built-in packet sniffer.
- |	System: Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
- |	IoCs: [Reconnaissance](https://attack.mitre.org/tactics/TA0043/) and [Exfiltration](https://attack.mitre.org/tactics/TA0010/) attempts, unusual traffic patterns, and unauthorized protocols.
- |	Associated Rationale: Provides visibility into network traffic to identify potential security threats, such as reconnaissance activities or attempts to exfiltrate data. Identify baseline connections and protocols.
- |	Priority (SIL): Moderate SIL
- |	 Thresholds / Assumptions: Alert thresholds set for significant deviations in traffic volume, protocol usage, or packet sizes.
