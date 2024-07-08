# workflow
1. First, read and analyse the case study scenario given in this reading (i.e. Develop a Monitoring Solution reading),
2. Then, create a list of risks and vulnerabilities in the next activity (i.e. List of Risks and Vulnerabilties task), and discuss the same with your peers,
3. Document additional findings and insights as you research for the risks and vulnerabilties (during the Tools Research and Documentation task),
4. Finally create a report as per the provided template (in your final project Report on Risks & Vulnerabilities). Creating a report is the last step in the case study/ project.

# Tools
- [NIST NVD](https://nvd.nist.gov/vuln/search)
- [CVSS](https://www.first.org/cvss/calculator/3.1)
- [MITRE CVE & ATT&CK](https://attack.mitre.org/)
- [Cyber Kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)
- [Windows event ID -to- MITRE ATT&CK](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D5/project/COPY%20mitre_v_eventIDs.md)

# Resource
- [Refresher : Indicators of compromise (IOCs)](https://www.fortinet.com/resources/cyberglossary/indicators-of-compromise#:~:text=What%20are%20indicators%20of%20compromise,or%20another%20breach%20in%20security.)
- [PRTG Manual: Available Sensor Types](https://www.paessler.com/manuals/prtg/list_of_available_sensor_types)
# Do's
- put sensors and alerts on are the ones that will best identify known IoCs.
- Use Industry Standard resources like NIST, and MITRE
- recommend basic monitoring of logs, events, and SNMP for the scenario given in the case study.
- appropriate sensors have been added to the systems for monitoring key items and that proper thresholds have been set for alerts

- Asset background:
> systems is a server, she wants to focus most of her attention there, but also remembering that the Windows Workstation and Linux system are used for development, and the Windows Server system has an SQL database that needs to be watched.
- have approximately 20 sensors to monitor
    - sensors and alerts to best identify known IoCs.
    - understand why you are recommending each sensor and alert threshold as you will have to justify your decisions.
- recommend basic monitoring of logs, events, and SNMP for the scenario given in the case study.

# Assets
- Windows Server, runs: (S) (SM)
    - SQL database (S)
    - Internet Information Services (IIS) webserver (S)
      > used to exchange static and dynamic web content with internet user
    - PRTG Network Monitor (SM)

- Linux: (IP)
    - Used by developers to create important proprietary intellectual property (IP) for the company

- Windows workstations: (P) (A)
    - Sales (F) (P)
    - Marketing (P)
    - Management functions (A)

- Kali: 
    - Test systems (S)
    - IT systems (S)

The heads of the company have stated that all company information falls within the following classifications.
They have further ranked the importance of each class of information from most important to least important as follows:

1. Privacy (P)
2. Proprietary (IP)
3. Admin (A)
4. Financial/accounting (F)
5. Security Management (SM)
6. Systems (S)

Note
> When completing your vulnerability and risk research and prioritization, you can use the OS/software versions found in your VirtualBox lab environment as those that are found in the Big Dog architecture.
