# Cat Scan II Big Dog
Date: 2024-07-08
## Contents:
1. [Executive Summar](#executive-summary)
2. [Table of sensors](#table-of-sensors)
3. [Discussion section](#discussion-section)
4. [Recommendation section](#recommendation-section)
5. References

# Executive Summary:
> A short, one or two paragraph summary explaining what you have done. Include information about the top five SILs and the sensors and thresholds you are monitoring or recommending.

A total 17 Sensors *types* were added.
Sensors together create a 'baseline' from which anomalies can be detected.
Such events possing as IoCs are at the attention of our sensors.
The purpose of these is to enhace security, by monitoring for potential IoCs.
Most sensors monitor for at least one of 3 things:
- **status** of a device and it's service (Down, Up, Running, Stopped, Warrning, ...)
- **performance** of a device (responce time, hardware metrics, ...)
- and **end point data** such as Strings (Words in an email, logs, ...) or Integers (Email volume, File counts, ...).

(Syslog) File Content and Event Log Sensors for Linux and Windows machines are the most important sensors regarding security. Logs are the bedrock of detecting attacker reconnaissance which is the first step in the [cyber kill chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) (Lockheed Martin, n.d.).
Besides these, Bandwidth Usage Sensor and Ping Sensors are very important in establishing a network baseline, monitoring data volumes and the connectivty in which all devices operate. WMI Security Center Sensor monitoring the security software updates of Windows machines, Port Sensors monitoring for potential attacks at port of entries, Packet Sniffer Sensor in IT Systems giving valuable insight into network traffic communications, these are all complimentary parts of developing a strong monitoring system tailored to detect potential attackers.

Though PRTG sensors are themselves powerfull netowork monitoring tools, alone they are not a sufficient security practice to ensure the C.I.A. of devices on this network.

To further secure your organizaiton consult the recommendation section.

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
| Bandwidth Usage Sensor [SNMP Traffic Sensor](https://www.paessler.com/manuals/prtg/snmp_traffic_sensor) (Paessler AG,. n.d.) | The SNMP Traffic sensor monitors traffic on a device via the Simple Network Management Protocol (SNMP). Monitors network bandwidth usage. | All, Router Interface | [Network Denial of Service](https://attack.mitre.org/techniques/T1498/)(MITRE ATT&CK, n.d.), [Exfiltration](https://attack.mitre.org/tactics/TA0010/)(MITRE ATT&CK, n.d.) | Network bandwidth baselines are vital for monitoring network health, detecting potential DDoS attacks, data exfiltration, and other unusual network events. | Moderate        | Thresholds: Traffic In, Traffic Out: 0.03 Mbits Upper Bound. Total Traffic: 0.43 Mbits Upper Bound.        |
| [Ping](https://www.paessler.com/manuals/prtg/ping_sensor) (Paessler AG,. n.d.) | The Ping sensor sends an Internet Control Message Protocol (ICMP) echo request ("ping") from the probe system to the parent device to monitor its availability. | ALL    | DDoS   | This is a simple, low-resource-use, and reliable PING sensor. It is a default sensor used to test network connectivity. | Low            | Device Downtime, Packet Loss, Ping time. Although ping is not a cornerstone of cybersecurity, it helps establish a reliable baseline of network connectivity and can detect interruptions and unusual downtime on the network. |

## OS specific sensors
### Windows

| Sensor                                                      | Description                                                                                                                                                          | System                                                                                                          | IoCs                                                                                               | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                                                   |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------|
| [WMI Security Center Sensor](https://www.paessler.com/manuals/prtg/wmi_security_center_sensor)(Paessler AG,. n.d.)  | Status Sensor Monitors antivirus software status. The WMI Security Center sensor monitors the security status of a Windows client system via Windows Management Instrumentation (WMI). It can monitor all security products that are controlled by Windows Security Center / Windows Action Center. | Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)(MITRE ATT&CK, n.d.) | Ensuring that antivirus is up to date and running is essential for the security of a Windows machine. | High            | Statuses: Up (Running & Up To Date), Warning (Running & Out Of Date), Down (Not Running & Out Of Date). |
| [WMI Event Log Sensor](https://www.paessler.com/manuals/prtg/wmi_event_log_sensor)(Paessler AG,. n.d.)  | Monitors Windows event logs. The WMI Event Log sensor monitors a Windows log file via Windows Management Instrumentation (WMI). | Microsoft Windows 11 Home, Version 10.0.22631 Build 22631 | [Indicator Removal: Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/)(MITRE ATT&CK, n.d.), [Brute Force](https://attack.mitre.org/techniques/T1110/)(MITRE ATT&CK, n.d.), [Application Log](https://attack.mitre.org/datasources/DS0015/)(MITRE ATT&CK, n.d.) | Use the sensor to monitor event logs.                                                        | High            | Narrow down to event down to any attribute (type, Event ID, user, message, etc). Additionally Set-up (trap) Task related to important events. Use Event ID 104/1102 for Indicator Removal: Clear Windows Event Logs. Use Event ID 33205 for Brute Force attempts. |
| Sensitivie folder sensor [Folder Sensor](https://www.paessler.com/manuals/prtg/folder_sensor)(Paessler AG,. n.d.)  | The Folder sensor monitors a folder via Server Message Block (SMB). You can monitor file changes and file ages. | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | [File and Directory Permissions Modification: Windows File and Directory Permissions Modification](https://attack.mitre.org/techniques/T1222/001/)(MITRE ATT&CK, n.d.) | Detect unexpected changes in critical system folders.         | Moderate        | File Count, Folder Size, file modifications.                                |

  
### Linux
| Sensor                                               | Description                                                                                               | Systems                                                       | IoCs                                                                                                                      | Associated Rationale                                                                  | Priority (SIL) | Thresholds / Assumptions                                                                |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------|
| Sensitive file sensor (Syslog): [File Content Sensor](https://www.paessler.com/manuals/prtg/file_content_sensor)(Paessler AG,. n.d.) | Monitors changes to files and directories. The File Content sensor checks a text file (for example, a log file) for certain strings. | Kali GNU/Linux (debian) version 2024.2 (kali-rolling). Ubuntu Linux (debian) 22.04.4 LTS (Jammy Jellyfish). | [Indicator Removal: Clear Linux or Mac System Logs](https://attack.mitre.org/techniques/T1070/002/)(MITRE ATT&CK, n.d.), [Application Log](https://attack.mitre.org/datasources/DS0015/)(MITRE ATT&CK, n.d.) | Logs are the bedrock of reconnaissance and intrusion detection. Linux machines on the network contain IP and System information data. | High            | Monitoring of specific files will be in place, this can include syslog file, Access log files, application log files.                               |


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
| Email sensor [IMAP Sensor](https://www.paessler.com/manuals/prtg/imap_sensor)(Paessler AG,. n.d.) | The IMAP sensor monitors an email server via the Internet Message Access Protocol (IMAP). It can check the content of emails for certain keywords. | Microsoft Windows 11, version 23H2, (Sun Valley 3). Marketing Workstation | [Phishing for Information](https://attack.mitre.org/techniques/T1598/)(MITRE ATT&CK, n.d.), [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)(MITRE ATT&CK, n.d.) | Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns | High           | Email Count, Search String in email (potentially integrating with AI for detection). |

### Sales (F) & (P)
Basic information (sensor context)
> Microsoft Windows 11 Home, version 23H2, Sun Valley 3
>
> Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
>
> Sales SIL = High

| Sensor                                      | Description                                                                                               | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| Email sensor [IMAP Sensor](https://www.paessler.com/manuals/prtg/imap_sensor)(Paessler AG,. n.d.) | The IMAP sensor monitors an email server via the Internet Message Access Protocol (IMAP). It can check the content of emails for certain keywords. | Microsoft Windows 11, version 23H2, (Sun Valley 3). Sales Workstation | [Phishing for Information](https://attack.mitre.org/techniques/T1598/)(MITRE ATT&CK, n.d.), [Phishing for Information: Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002/)(MITRE ATT&CK, n.d.) | Unusual volume of emails or connection attempts, potentially indicating spam or phishing campaigns | High           | Email Count, Search String in email (potentially integrating with AI for detection). |

 
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
| [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)(Paessler AG,. n.d.)                       | The sensor monitors a database on a MySQL server and executes a query.                                                | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish). Developer Server | [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)(MITRE ATT&CK, n.d.)                                            | Checks for the Integrity and Availability of the SQL database. As seen in listed ports, the Linux VM has mysqld ports LISTENING. | High                  | Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts.                                                                                  |
| [HTTP Apache ModStatus PerfStats Sensor](https://www.paessler.com/manuals/prtg/http_apache_modstatus_perfstats_sensor)(Paessler AG,. n.d.) | The HTTP Apache ModStatus PerfStats sensor monitors performance statistics of an Apache web server over HTTP.          | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish). Developer Server |                                                                                                                           | Attackers may try to attack the availability of the Apache 2 server.                                                         | Moderate                  | CPULoad, Workers Idle/Busy, Requests Per Second, UP/DOWN time                                                                                                                                  |
| [SSH Sensor Port Sensor](https://www.paessler.com/manuals/prtg/port_sensor)(Paessler AG,. n.d.)                                             | Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).             | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish) | [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/)(MITRE ATT&CK, n.d.), [Password spraying](https://attack.mitre.org/techniques/T1110/003/)(MITRE ATT&CK, n.d.) | Port 22 is used for remote SSH login. Having a baseline for accessibility will allow to spot spikes in unusual SSH attempts. It is likely that developers use this port for work and it should be monitored. | Moderate | Upper bound thresholds response time < 100ms. Developer SSH port allows access to HVA and should be monitored.                                                                                  |
| [SSH Remote Ping Sensor](https://www.paessler.com/manuals/prtg/ssh_remote_ping_sensor)(Paessler AG,. n.d.)                                 | The SSH Remote Ping sensor remotely monitors the connectivity between a system running Linux/macOS X and another device. | Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish) | [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/)(MITRE ATT&CK, n.d.), [Service Stop](https://attack.mitre.org/techniques/T1489/)(MITRE ATT&CK, n.d.) | Password spraying "Commonly targeted services [...] MySQL (3306/TCP)"                                                      | High                  | Packet Loss, Response time (average, max, min), Downtime. This is important to measure to ensure that developers have steady access to their environment (availability). A baseline can help establish unusual response times which could be IoC for Adversary-in-the-Middle attacks (confidentiality/integrity). |


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
| [System Health Sensor](https://www.paessler.com/manuals/prtg/system_health_sensor)(Paessler AG,. n.d.) | The System Health sensor monitors the status of the probe system. It checks various system parameters that can affect the quality of the monitoring results. It is automatically created, but manual creations are possible. | Microsoft Windows 11 Home, version 23H2, Sun Valley 3 | [Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)(MITRE ATT&CK, n.d.)                | This sensor is necessary to monitor the health of the managing device's own probe system.                | High       | Available Memory, System CPU Load, Downtime. An attack on the availability of the system would cause serious harm to the very purpose of the probe device. |


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
| [MySQL v2 Sensor Database Query Sensor](https://www.paessler.com/manuals/prtg/mysql_v2_sensor)(Paessler AG,. n.d.)                        | The sensor monitors a database on a MySQL server and executes a query.                                                | Microsoft Windows 11 Home, version 23H2, Sun Valley 3 | [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)(MITRE ATT&CK, n.d.)                               | Checks for the Integrity and Availability of the SQL database.                                            | Moderate       | Sudden changes in query execution times or connection counts, which could indicate SQL injection attempts.                              |


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
| [FTP Sensor](https://www.paessler.com/manuals/prtg/ftp_sensor)(Paessler AG,. n.d.) | The FTP sensor monitors file servers via the File Transfer Protocol (FTP) and FTP over SSL (FTPS). Monitors specified FTP port request response time and status (accepted).              | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)(MITRE ATT&CK, n.d.)                      | The IIS server can host FTP services which can be used for exfiltration of data.                         | Moderate       | Response time in msec. The Upper bound should indicate unusual activity.    |
| [Windows IIS Application Sensor](https://www.paessler.com/manuals/prtg/wmi_iis_application_sensor)(Paessler AG,. n.d.)                     | Monitors IIS server via Windows Management Instrumentation (WMI). Gives insights into the performance, availability, and usage of the IIS server.                                  | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3). IIS Version 10.0 | [Server Software Component: IIS Components](https://attack.mitre.org/techniques/T1505/004/)(MITRE ATT&CK, n.d.), [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)(MITRE ATT&CK, n.d.) | The IIS is a webserver public-facing, file share server. Such a server can be compromised and distribute harm internally and externally. | Moderate       | IIS sensor can monitor for bytes and files (data) sent/received, HTTP requests Get/Post, Status Up/Down, Users Known/Anonymous. A very powerful sensor for monitoring critical IIS operations. |
| [Windows Process Sensor](https://www.paessler.com/manuals/prtg/wmi_process_sensor#channels)(Paessler AG,. n.d.)                               | The Windows Process sensor monitors a Windows process via Windows Management Instrumentation (WMI) or Windows performance counters.                                             | Microsoft Windows 11 Home, version 23H2 (Sun Valley 3) | [Service Stop](https://attack.mitre.org/techniques/T1489/)(MITRE ATT&CK, n.d.)                                               | A baseline is important to monitor the activity of the organization and potential attacks on availability. | Moderate       | CPU, Handles, Instances, Threads, Working Set. Everything to monitor the performance of the IIS server, which includes a web server, FTP, and Windows Fileshare. |


### Test System (S)
Basic information (sensor context)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> Test System SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
>
> Test System SIL = Moderate

| Sensor                                                      | Description                                                                                                           | System                                                | IoCs                                                                                                     | Associated Rationale                                                                                      | Priority (SIL) | Thresholds / Assumptions                                                   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------|
| SSH Sensor [Port Sensor](https://www.paessler.com/manuals/prtg/port_sensor)(Paessler AG,. n.d.) | Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted).              | Kali GNU/Linux (debian) version 2024.2 (kali-rolling) | [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/)(MITRE ATT&CK, n.d.) higher response time as machine is sprayed by password attempts. | Port 22 is used for remote SSH login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unusual SSH attempts. Brute forcing attacks could occur since Test Systems might not be as thoroughly configured (passwords, IDs, default settings) hence opening them up for attacks. | Moderate SIL (low Integrity, low Availability) | Upper bound thresholds response time < 80ms. This sensor is likely used less often, so the baseline should be tighter to notice disturbances. Test Services may contain key strategic information for future planning of attackers. |


### IT System (S)
Basic information (sensor context)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
>
> IT System SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
>
> IT System SIL = Moderate

| Sensor | Description | System | IoCs | Associated Rationale | Priority (SIL) | Thresholds / Assumptions |
|--------|-------------|--------|------|----------------------|----------------|--------------------------|
| [SSH Sensor](https://www.paessler.com/manuals/prtg/port_sensor)(Paessler AG,. n.d.)  | Monitors SSH access and usage. Monitors specified TCP/IP port request response time and status (accepted). | Kali GNU/Linux (debian) version 2024.2 (kali-rolling) | [Bruteforcing](https://attack.mitre.org/techniques/T1110/003/)(MITRE ATT&CK, n.d.) higher response time as machine is sprayed by password attempts. | Port 22 is used for remote ssh login to IT Systems machines. Having a baseline for accessibility will allow to spot spikes in unusual SSH attempts. | Moderate SIL | Upper bound thresholds response time < 100ms. This sensor is used less often, so the baseline should be tighter to detect disturbances. |
| [Packet Sniffer Sensor](https://www.paessler.com/manuals/prtg/packet_sniffer_header_sensor)(Paessler AG,. n.d.)  | Monitors and analyzes network traffic to detect unusual patterns, unauthorized protocols, or suspicious activities within the network. The Packet Sniffer sensor monitors the headers of data packets that pass a local network card using a built-in packet sniffer. | Kali GNU/Linux (debian) version 2024.2 (kali-rolling) | [Reconnaissance](https://attack.mitre.org/tactics/TA0043/)(MITRE ATT&CK, n.d.) and [Exfiltration](https://attack.mitre.org/tactics/TA0010/)(MITRE ATT&CK, n.d.) attempts, unusual traffic patterns, and unauthorized protocols. | Provides visibility into network traffic to identify potential security threats, such as reconnaissance activities or attempts to exfiltrate data. Identify baseline connections and protocols. | Moderate SIL | Alert thresholds set for significant deviations in traffic volume, protocol usage, or packet sizes. |


# Discussion Section:

**All devices** on the network have a Ping Sensor to ensure probe connectivity and device downtime. Together with Bandwidth Usage Sensor, this creates a baseline for traffic on the network, used for IoC detection at a network level.

**All Windows devices** are probed by WMI Security Center Sensors to check for antivirus software status. WMI Event Log sensors are the bedrock of log-based IoC detection. These sensors are foundational to recording important Event IDs and mainting device security updates.
Additionally, some Folder Sensor keep track activity related to HVA which occupy windows worksations in Marketing & Sales (PII and Financial data).  

For **Linux machines**, file Content Sensor are required to centrally monitor Syslog. Just like in Windows, Logs are the bedrock of reconnaissance and intrusion detection. 

**Marketing and Sales** have IMAP Sensor (Email sensor) to detect IoCs related to the deparment's activities. The sensor performs Email Volume and can Search String in messages to detect Phishing.
 
**Developer** (VMs) were found to run mySQL and apache 2, hence were equiped with MySQL v2 Sensor (Database Query Sensor) and HTTP Apache ModStatus PerfStats Sensor. Those two sensors monitor IoCs related to availability of services, and integrity of the database.
Developers benefit from SSH Sensor (Port Sensor) SSH Remote (Ping Sensor), to detect brute force attacks and man-in-the-middle attacks.

The **PRTG Managing device**'s probe has a default System Health Sensor. This is an important monitor due to the system itself relying on the availability of the probe. Such probes can also be manually added, in case load-balancing probes were added.

The **ISS server** contains FTP and Webserver. Hence it has a HTTP Load Time Sensor for public facing IoCs (DDoS, Malicious Redirects, Content Injections) and and a FTP Sensor for a baseline checking on filetransfer for IoCs of Exfiltration.
PRTG expressly has an Windows IIS Application Sensor, which might replace both HTTP Load Time and FTP sensors because of its very powerfull monitoring capabilties in Integrity (bytes and files (data) sent/received, HTTP requests Get/Post, Status Up/Down, Users Known/Anonymous).
The Windows Process Sensor checks on IIS Server performance for potential IoCs related to Availability.

**Test Systems** have SSH Port Sensors to monitor potential break-ins, as test enviroments are likely to cary default settings and vulnerable to brute force attempts.

Lastly, **IT System** devices also have SSH Port Sensors due to the likelyhood of operators to use remote acces. Packet Sniffer Sensor provides baseline information [filter network traffic](https://attack.mitre.org/mitigations/M1037/)(MITRE ATT&CK, n.d.) in order to recognize IoCs such as reconaisance or Exfiltration.

# Recommendation Section:

PRTG sensors are powerfull tools for netowrk monitoring and can be used to look for potential IoCs in an organiation. Alone however, sensors can not protect an organization. [Network Segmentation](https://attack.mitre.org/mitigations/M1030/)(MITRE ATT&CK, n.d.) is a industry standard practice which can include IP subneting, VLANs, DMZ for public faceing services (*such as the IIS Server*) and virtual private cloud.

For windows, set up event-triggered task for specific [Windows Event IDs](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D5/project/COPY%20mitre_v_eventIDs.md)(Johnson E., 7.24) . In Linux set up CRON jobs based on things like: log entries or file changes.

[Data Backup](https://attack.mitre.org/mitigations/M1053/)(MITRE ATT&CK, n.d.) are necessary to restore systems and should be kept seperated from the network to prevent compromise. Sensitive data should be kept [encrypted](https://attack.mitre.org/mitigations/M1041/)(MITRE ATT&CK, n.d.) and segregated.

# References

  1. Lockheed Martin. (n.d.). The cyber kill chain. Retrieved July 8, 2024, from https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
  2. MITRE ATT&CK. (n.d.). Network denial of service. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1498
  3. MITRE ATT&CK. (n.d.). Exfiltration. Retrieved July 8, 2024, from https://attack.mitre.org/tactics/TA0010/
  4. MITRE ATT&CK. (n.d.). Impair defenses: Disable or modify tools. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1562/001/
  5. MITRE ATT&CK. (n.d.). Indicator removal: Clear Windows event logs. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1070/001/
  6. MITRE ATT&CK. (n.d.). Brute force. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1110/
  7. MITRE ATT&CK. (n.d.). Application log. Retrieved July 8, 2024, from https://attack.mitre.org/datasources/DS0015/
  8. MITRE ATT&CK. (n.d.). File and directory permissions modification: Windows file and directory permissions modification. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1222/001/
  9. MITRE ATT&CK. (n.d.). Indicator removal: Clear Linux or Mac system logs. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1070/002/
  10. MITRE ATT&CK. (n.d.). Phishing for information. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1598/
  11. MITRE ATT&CK. (n.d.). Phishing for information: Spearphishing attachment. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1598/002/
  12. MITRE ATT&CK. (n.d.). Exploitation of remote services. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1210/
  13. MITRE ATT&CK. (n.d.). Password spraying. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1110/003/
  14. MITRE ATT&CK. (n.d.). Adversary-in-the-middle. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1557/
  15. MITRE ATT&CK. (n.d.). Service stop. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1489/
  16. MITRE ATT&CK. (n.d.). Exfiltration over alternative protocol. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1048/
  17. MITRE ATT&CK. (n.d.). Server software component: IIS components. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1505/004/
  18. MITRE ATT&CK. (n.d.). Exploit public-facing application. Retrieved July 8, 2024, from https://attack.mitre.org/techniques/T1190/
  19. MITRE ATT&CK. (n.d.). Reconnaissance. Retrieved July 8, 2024, from https://attack.mitre.org/tactics/TA0043/
  20. MITRE ATT&CK. (n.d.). Network segmentation. Retrieved July 8, 2024, from https://attack.mitre.org/mitigations/M1030/
  21. MITRE ATT&CK. (n.d.). Filter network traffic. Retrieved July 8, 2024, from https://attack.mitre.org/mitigations/M1037
  22. MITRE ATT&CK. (n.d.). Data backup. Retrieved July 8, 2024, from https://attack.mitre.org/mitigations/M1053/
  23. MITRE ATT&CK. (n.d.). Encrypt sensitive information. Retrieved July 8, 2024, from https://attack.mitre.org/mitigations/M1041/ 
  24. Paessler AG. (n.d.). SNMP traffic sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/snmp_traffic_sensor
  25. Paessler AG. (n.d.). Ping sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/ping_sensor
  26. Paessler AG. (n.d.). WMI security center sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/wmi_security_center_sensor
  27. Paessler AG. (n.d.). WMI event log sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/wmi_event_log_sensor
  28. Paessler AG. (n.d.). Folder sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/folder_sensor
  29. Paessler AG. (n.d.). File content sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/file_content_sensor
  30. Paessler AG. (n.d.). IMAP sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/imap_sensor
  31. Paessler AG. (n.d.). MySQL v2 sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/mysql_v2_sensor
  32. Paessler AG. (n.d.). HTTP Apache ModStatus PerfStats sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/http_apache_modstatus_perfstats_sensor
  33. Paessler AG. (n.d.). Port sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/port_sensor
  34. Paessler AG. (n.d.). SSH remote ping sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/ssh_remote_ping_sensor
  35. Paessler AG. (n.d.). System health sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/system_health_sensor
  36. Paessler AG. (n.d.). FTP sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/ftp_sensor
  37. Paessler AG. (n.d.). Windows IIS application sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/wmi_iis_application_sensor
  38. Paessler AG. (n.d.). Windows process sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/wmi_process_sensor#channels
  39. Paessler AG. (n.d.). Packet sniffer header sensor. Retrieved July 8, 2024, from https://www.paessler.com/manuals/prtg/packet_sniffer_header_sensor
