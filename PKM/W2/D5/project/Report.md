# Cat Scan II Big Dog
Date: 2024-07-08
## Contents:
1. [Executive Summar](#executive-summary)
2. [Table of sensors](#table-of-sensors)
3. [Discussion section](#discussion-section)
4. [Recommendation section](#recommendation-section)

# Executive Summary:
> A short, one or two paragraph summary explaining what you have done. Include information about the top five SILs and the sensors and thresholds you are monitoring or recommending.

A total 17 Sensors types were added. The purpose of these is to enhace security, by monitoring for potential IoCs.
Sensors 

# Table of Sensors:
1. Bandwidth Usage Sensor (SNMP Traffic Sensor)
2. Ping Sensor
3. WMI Security Center Sensor
4. WMI Event Log Sensor
5. Folder Sensor (Sensitive folder sensor)
6. File Content Sensor (Sensitive file sensor for Syslog)
7. IMAP Sensor (Email sensor)
8. MySQL v2 Sensor (Database Query Sensor)
9. HTTP Apache ModStatus PerfStats Sensor
10. SSH Sensor (Port Sensor)
11. SSH Remote Ping Sensor
12. System Health Sensor
13. HTTP Load Time Sensor
14. FTP Sensor
15. Windows IIS Application Sensor
16. Windows Process Sensor
17. Packet Sniffer Sensor

## Network Asset sensors (All devices)

| Sensor                         | Description                                                                                                 | System                 | IoCs                                                                                                     | Associated Rationale                                                                                          | Priority (SIL) | Thresholds / Assumptions                                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------|
| Bandwidth Usage Sensor [SNMP Traffic Sensor](https://www.paessler.com/manuals/prtg/snmp_traffic_sensor) | The SNMP Traffic sensor monitors traffic on a device via the Simple Network Management Protocol (SNMP). Monitors network bandwidth usage. | All, Router Interface | [Network Denial of Service](https://attack.mitre.org/techniques/T1498/), [Exfiltration](https://attack.mitre.org/tactics/TA0010/) | Network bandwidth baselines are vital for monitoring network health, detecting potential DDoS attacks, data exfiltration, and other unusual network events. | Moderate        | Thresholds: Traffic In, Traffic Out: 0.03 Mbits Upper Bound. Total Traffic: 0.43 Mbits Upper Bound.        |
| [Ping](https://www.paessler.com/manuals/prtg/ping_sensor) | The Ping sensor sends an Internet Control Message Protocol (ICMP) echo request ("ping") from the probe system to the parent device to monitor its availability. | ALL    | DDoS   | This is a simple, low-resource-use, and reliable PING sensor. It is a default sensor used to test network connectivity. | Low            | Device Downtime, Packet Loss, Ping time. Although ping is not a cornerstone of cybersecurity, it helps establish a reliable baseline of network connectivity and can detect interruptions and unusual downtime on the network. |

## OS specific sensors
### Windows

| Sensor                                                      | Description                                                                                                                                                          | System                                                                                                          | IoCs                                                                                               | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                                                   |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------|
| [WMI Security Center Sensor](https://www.paessler.com/manuals/prtg/wmi_security_center_sensor) | Status Sensor Monitors antivirus software status. The WMI Security Center sensor monitors the security status of a Windows client system via Windows Management Instrumentation (WMI). It can monitor all security products that are controlled by Windows Security Center / Windows Action Center. | Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/) | Ensuring that antivirus is up to date and running is essential for the security of a Windows machine. | High            | Statuses: Up (Running & Up To Date), Warning (Running & Out Of Date), Down (Not Running & Out Of Date). |
| [WMI Event Log Sensor](https://www.paessler.com/manuals/prtg/wmi_event_log_sensor) | Monitors Windows event logs. The WMI Event Log sensor monitors a Windows log file via Windows Management Instrumentation (WMI). | Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | [Indicator Removal: Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/), [Brute Force](https://attack.mitre.org/techniques/T1110/), [Application Log](https://attack.mitre.org/datasources/DS0015/) | Use the sensor to monitor event logs.                                                        | High            | Narrow down to event down to any attribute (type, Event ID, user, message, etc). Additionally Set-up (trap) Task related to important events. Use Event ID 104/1102 for Indicator Removal: Clear Windows Event Logs. Use Event ID 33205 for Brute Force attempts. |
| Sensitivie folder sensor [Folder Sensor](https://www.paessler.com/manuals/prtg/folder_sensor) | The Folder sensor monitors a folder via Server Message Block (SMB). You can monitor file changes and file ages. | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | [File and Directory Permissions Modification: Windows File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222/001/) | Detect unexpected changes in critical system folders.         | Moderate        | File Count, Folder Size, file modifications.                                |

  
### Linux
| Sensor                                               | Description                                                                                               | Systems                                                       | IoCs                                                                                                                      | Associated Rationale                                                                  | Priority (SIL) | Thresholds / Assumptions                                                                |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------|
| Sensitive file sensor (Syslog): [File Content Sensor](https://www.paessler.com/manuals/prtg/file_content_sensor) | Monitors changes to files and directories. The File Content sensor checks a text file (for example, a log file) for certain strings. | Kali GNU/Linux (debian) version 2024.2 (kali-rolling). Ubuntu Linux (debian) 22.04.4 LTS (Jammy Jellyfish). | [Indicator Removal: Clear Linux or Mac System Logs](https://attack.mitre.org/techniques/T1070/002/), [Application Log](https://attack.mitre.org/datasources/DS0015/) | Logs are the bedrock of reconnaissance and intrusion detection. Linux machines on the network contain IP and System information data. | High            | Monitoring of specific files will be in place, this can include syslog file, Access log files, application log files.                               |


## Specific Information Asset Sensors
In order of category importance

### Marketing (P)
Basic information (sensor context)
> Microsoft Windows 11, version 23H2, (Sun Valley 3)
>
> Marketing SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
>
> Marketing SIL = High

| Sensor                  | Description                                                                                               | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| Email sensor [IMAP Sensor](https://www.paessler.com/manuals/prtg/imap_sensor) | The IMAP sensor monitors an email server via the Internet Message Access Protocol (IMAP). It can check the content of emails for certain keywords. | Microsoft Windows 11, version 23H2, (Sun Valley 3). Marketing Workstation | [Phishing for Information](https://attack.mitre.org/techniques/T1598/), [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/) | Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns | High           | Email Count, Search String in email (potentially integrating with AI for detection). |

### Sales (F) & (P)
Basic information (sensor context)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
>
> Sales SIL = High

| Sensor                                      | Description                                                                                               | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| Email sensor [IMAP Sensor](https://www.paessler.com/manuals/prtg/imap_sensor) | The IMAP sensor monitors an email server via the Internet Message Access Protocol (IMAP). It can check the content of emails for certain keywords. | Microsoft Windows 11, version 23H2, (Sun Valley 3). Sales Workstation | [Phishing for Information](https://attack.mitre.org/techniques/T1598/), [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/) | Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns | High           | Email Count, Search String in email (potentially integrating with AI for detection). |

 
### Developer Machines (IP)
Basic information (sensor context)
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

| Sensor                                                  | Description                                                                                                           | System                                                | IoCs                                                                                                                      | Associated Rationale                                                                                                        | Priority (SIL)        | Thresholds / Assumptions                                                                                                       |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)                       | The sensor monitors a database on a MySQL server and executes a query.                                                | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish). Developer Server | [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)                                            | Checks for the Integrity and Availability of the SQL database. As seen in listed ports, the Linux VM has mysqld ports LISTENING. | High                  | Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts.                                                                                  |
| [HTTP Apache ModStatus PerfStats Sensor](https://www.paessler.com/manuals/prtg/http_apache_modstatus_perfstats_sensor) | The HTTP Apache ModStatus PerfStats sensor monitors performance statistics of an Apache web server over HTTP.          | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish). Developer Server |                                                                                                                           | Attackers may try to attack the availability of the Apache 2 server.                                                         | High                  | CPULoad, Workers Idle/Busy, Requests Per Second, UP/DOWN time                                                                                                                                  |
| [SSH Sensor Port Sensor](https://www.paessler.com/manuals/prtg/port_sensor)                                             | Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).             | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish) | [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/), [Password spraying](https://attack.mitre.org/techniques/T1110/003/) | Port 22 is used for remote SSH login. Having a baseline for accessibility will allow to spot spikes in unusual SSH attempts. It is likely that developers use this port for work and it should be monitored. | Moderate SIL (low Integrity, low Availability) | Upper bound thresholds response time < 100ms. Developer SSH port allows access to HVA and should be monitored.                                                                                  |
| [SSH Remote Ping Sensor](https://www.paessler.com/manuals/prtg/ssh_remote_ping_sensor)                                 | The SSH Remote Ping sensor remotely monitors the connectivity between a system running Linux/macOS X and another device. | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish) | [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/), [Service Stop](https://attack.mitre.org/techniques/T1489/) | Password spraying "Commonly targeted services [...] MySQL (3306/TCP)"                                                      | High                  | Packet Loss, Response time (average, max, min), Downtime. This is important to measure to ensure that developers have steady access to their environment (availability). A baseline can help establish unusual response times which could be IoC for Adversary-in-the-Middle attacks (confidentiality/integrity). |


### Management functions (A)
Basic information (sensor context)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Management SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>


### PRTG Network Monitor (SM)
Basic information (sensor context)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> 
> PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315
> PRTG Network Monitor SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> PRTG Network Monitor SIL = Moderate

| Sensor                                      | Description                                                                                                           | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| [System Health Sensor](https://www.paessler.com/manuals/prtg/system_health_sensor) | The System Health sensor monitors the status of the probe system. It checks various system parameters that can affect the quality of the monitoring results. It is automatically created, but manual creations are possible. | Microsoft Windows 11 Home, version 23H2, Sun Valley 3 | [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)                | This sensor is necessary to monitor the health of the managing device's own probe system.                | Moderate       | Available Memory, System CPU Load, Downtime. An attack on the availability of the system would cause serious harm to the very purpose of the probe device. |


### SQL database (S)
Basic information (sensor context)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
> > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)
>
> SQL database SC = {(confidentiality, Low), (integrity, low), (availability, Moderate)}
>
> SQL database SIL = Moderate

| Sensor                                                  | Description                                                                                                           | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)                       | The sensor monitors a database on a MySQL server and executes a query.                                                | Microsoft Windows 11 Home, version 23H2, Sun Valley 3 | [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)                               | Checks for the Integrity and Availability of the SQL database.                                            | Moderate       | Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts.                              |


### Internet Information Services (IIS) webserver (S)
Basic information (sensor context)
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

| Sensor                                                      | Description                                                                                                           | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| HTTP Load Time                                               | Monitors the time it takes for the page to load.                                                                       | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | Malicious Redirects, DDoS Attacks, Content Injection. Unexpected changes in load time can indicate anomalies or performance-related issues that could indicate a security breach or compromise. | Linux web server being internal and outward facing (Assumption).                                           | Medium (SIL of high, see assumptions) | SIL based on the fact that *BIG DOG does NOT have a large Web Presence*, the Low impact on availability, higher chance of compromise. |
| [FTP Sensor](https://www.paessler.com/manuals/prtg/ftp_sensor) | The FTP sensor monitors file servers via the File Transfer Protocol (FTP) and FTP over SSL (FTPS). Monitors specified FTP port request response time and status (accepted).              | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)                      | The IIS server can host FTP services which can be used for exfiltration of data.                         | Moderate       | Response time in msec. The Upper bound should indicate unusual activity.    |
| [Windows IIS Application Sensor](https://www.paessler.com/manuals/prtg/wmi_iis_application_sensor)                     | Monitors IIS server via Windows Management Instrumentation (WMI). Gives insights into the performance, availability, and usage of the IIS server.                                  | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3). IIS Version 10.0 | [Server Software Component: IIS Components](https://attack.mitre.org/techniques/T1505/004/), [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | The IIS is a webserver public-facing, file share server. Such a server can be compromised and distribute harm internally and externally. | Moderate       | IIS sensor can monitor for bytes and files (data) sent/received, HTTP requests Get/Post, Status Up/Down, Users Known/Anonymous. A very powerful sensor for monitoring critical IIS operations. |
| [Windows Process Sensor](https://www.paessler.com/manuals/prtg/wmi_process_sensor#channels)                               | The Windows Process sensor monitors a Windows process via Windows Management Instrumentation (WMI) or Windows performance counters.                                             | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | [Service Stop](https://attack.mitre.org/techniques/T1489/)                                               | A baseline is important to monitor the activity of the organization and potential attacks on availability. | Moderate       | CPU, Handles, Instances, Threads, Working Set. Everything to monitor the performance of the IIS server, which includes a web server, FTP, and Windows Fileshare. |


### Test System (S)
Basic information (sensor context)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> Test System SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>
> Test System SIL = Moderate

| Sensor                                                      | Description                                                                                                           | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| SSH Sensor [Port Sensor](https://www.paessler.com/manuals/prtg/port_sensor) | Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).              | Kali GNU/Linux (debian) version 2024.2 (kali-rolling) | [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/) higher response time as machine is sprayed by password attempts. | Port 22 is used for remote SSH login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unusual SSH attempts. Brute forcing attacks could occur since Test Systems might not be as thoroughly configured (passwords, IDs, default settings) hence opening them up for attacks. | Moderate SIL (low Integrity, low Availability) | Upper bound thresholds response time < 80ms. This sensor is likely used less often, so the baseline should be tighter to notice disturbances. Test Services may contain key strategic information for future planning of attackers. |


### IT System (S)
Basic information (sensor context)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> IT System SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> IT System SIL = Moderate

| Sensor | Description | System | IoCs | Associated Rationale | Priority (SIL) | Thresholds / Assumptions |
|--------|-------------|--------|------|----------------------|----------------|--------------------------|
| [SSH Sensor](https://www.paessler.com/manuals/prtg/port_sensor) | Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted). | Kali GNU/Linux (debian) version 2024.2 (kali-rolling) | [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/) higher response time as machine is sprayed by password attempts. | Port 22 is used for remote ssh login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unusual SSH attempts. | Moderate SIL | Upper bound thresholds response time < 100ms. This sensor is used less often, so the baseline should be tighter to detect disturbances. |
| [Packet Sniffer Sensor](https://www.paessler.com/manuals/prtg/packet_sniffer_header_sensor) | Monitors and analyzes network traffic to detect unusual patterns, unauthorized protocols, or suspicious activities within the network. The Packet Sniffer sensor monitors the headers of data packets that pass a local network card using a built-in packet sniffer. | Kali GNU/Linux (debian) version 2024.2 (kali-rolling) | [Reconnaissance](https://attack.mitre.org/tactics/TA0043/) and [Exfiltration](https://attack.mitre.org/tactics/TA0010/) attempts, unusual traffic patterns, and unauthorized protocols. | Provides visibility into network traffic to identify potential security threats, such as reconnaissance activities or attempts to exfiltrate data. Identify baseline connections and protocols. | Moderate SIL | Alert thresholds set for significant deviations in traffic volume, protocol usage, or packet sizes. |


# Discussion Section:
> A discussion of each of the connections between the sensors, IoCs and thresholds.
1. Bandwidth Usage Sensor (SNMP Traffic Sensor)
> 
2. Ping Sensor
3. WMI Security Center Sensor
4. WMI Event Log Sensor
5. Folder Sensor (Sensitive folder sensor)
6. File Content Sensor (Sensitive file sensor for Syslog)
7. IMAP Sensor (Email sensor)
8. MySQL v2 Sensor (Database Query Sensor)
9. HTTP Apache ModStatus PerfStats Sensor
10. SSH Sensor (Port Sensor)
11. SSH Remote Ping Sensor
12. System Health Sensor
13. HTTP Load Time Sensor
14. FTP Sensor
15. Windows IIS Application Sensor
16. Windows Process Sensor
17. Packet Sniffer Sensor
# Recommendation Section:
> A recommendation section where you should recommend how the client might enhance the security of their systems (for example added sensors); you must cite industry best practices as you make your recommendations.
