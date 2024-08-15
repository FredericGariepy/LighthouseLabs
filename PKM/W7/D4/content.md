# dict
| term| def|
|-|-|
|TTPs | tactics, techniques, and procedures|
|CTI |cyber threat intelligence|
|IoC|Indicator of Compromise |
|AoC|Artifact of Compromise |
| TIP | Threat Intelligence Platform|
|SOC|security operations center|

## cyber threat intelligence (CTI)

## CTI lifecycle
<img src="https://www.splunk.com/content/dam/splunk2/images/data-insider/cyber-threat-intelligence/threat-intelligence-life-cycle.jpg" width="400" />

#### 1. Planning and Requirements
intelligence program:
- objectives and procedures
#### 2. Information Collection
traffic logs, publicly available data sources, relevant forums, social media, and industry or subject matter experts
#### 3. Processing
transform the data into a format that is appropriate for analysis. \
The majority of the time, this requires arranging data points into spreadsheets, decrypting files, translating information from foreign sources, and reviewing the data to determine its relevance and dependability.
#### 4. Analysis
identify responses to the questions that were given during the requirements phase \
-  translate the data set into relevant suggestions and action items
#### 5. Dissemination
transform their analysis into a format that can be easily consumed


## CTI Types
- Strategic
- Tactical
- Operational
#### Strategic CTI (Long-term)
- long-term trends and patterns in the threat landscape.
- broader threat environment
- informs high-level decision-making and planning.
#### Operational CTI (Surface Contact)
- tactics, techniques, and procedures (TTPs)
- implementation of security controls and threat mitigation strategies on a more immediate basis.
#### Tactical CTI (Real-time, Active)
- detailed, actionable information on specific threats and incidents. 
- immediate response and incident handling
- detecting and responding to active threats.

## TIP
Threat Intelligence Platform (TIP) tech that processes external threat feeds and internal log files to generate a prioritized, customized, and contextualized feed of alerts for the consumption of Blue Team members in an SOC. 
TIP: \
- Automated alerting and reporting capabilities of the CTI platform.
- Insights on types of threats most pertinent to an organization's industry or business
- Consolidated repository of threat intelligence data.
#### TIP business values
- Automate Alert Response
- Reduce mean time to Respond
- Increase Incident coverage
### TIP SOC values
- Data Aggregation and Integration
- Data Analysis (IoC)
- Real-time Monitoring and Alerts
- Contextualization of Threat Data
- Sharing and Dissemination
- Integration with SOC
- Automation and Response

## Cyber Kill Chain
https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
<img src="https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/photo/cyber/THE-CYBER-KILL-CHAIN-body.png.pc-adaptive.480.medium.png" width="400" />

- Reconnaissance
> The observation stage: attackers typically assess the situation from the outside-in, in order to identify both targets and tactics for the attack.
- Intrusion
> Based on what the attackers discovered in the reconnaissance phase, they’re able to get into your systems: often leveraging malware or security vulnerabilities.
- Exploitation
> The act of exploiting vulnerabilities, and delivering malicious code onto the system, in order to get a better foothold.
- Privilege Escalation
> Attackers often need more privileges on a system to get access to more data and permissions: for this, they need to escalate their privileges often to an Admin.
- Lateral Movement
> Once they’re in the system, attackers can move laterally to other systems and accounts in order to gain more leverage: whether that’s higher permissions, more data, or greater access to systems.
- Obfuscation / Anti-forensics
> In order to successfully pull off a cyberattack, attackers need to cover their tracks, and in this stage they often lay false trails, compromise data, and clear logs to confuse and/or slow down any forensics team.
- Denial of Service
> Disruption of normal access for users and systems, in order to stop the attack from being monitored, tracked, or blocked
- Exfiltration
> The extraction stage: getting data out of the compromised system.
