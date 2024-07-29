# Risk Management Case Study
Date 07.29.20224
# Executive Summary
This Risk Management Plan aims to address three critical security threats
identified within the organization by evaluating current vulnerabilities (classifying), assessing potential impacts (treat assesment),
and recommending mitigation strategies (risk treament). 

Classification of assets was produced by assessing the [case information](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W5/Projects/Risk%20Management/case%20info.md) and [organization struture](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W5/Projects/Risk%20Management/Employees).

Threat assesment and treatment, are documented in the [risk __assesment__ and __treatment__ table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing).

Follow this document to learn about assesment and recommended treatments for three (3) main threats.
<!-- and the workflow used to further generate the risk assesment. \ -->

Consult the recommendations towards the end of this document to learn about implementing an information security management system (ISMS)
and aligning with ISO/IEC 27001 standards.

# Purpose, scope, and users
<!-- 
The purpose of this document is to define the methodology for assessment and treatment of
information risks in MHS, and to define the acceptable level of risk according to the ISO/IEC
27001 standard.

Risk Assessment and Risk Treatment are applied to the entire scope of the ISMS (i.e., to all
assets which are used within the organization or which could have an impact on information
security within the ISMS).
Users of this document are all employees of ACME INC. who take part in Risk Assessment and
Risk Treatment.
Note: all data is classified as confidential.
-->
The purpose of this document is to identify and present the three main threats to the organization.
Each threat is identified and presented by the same risk assessment and treatment methodologies described in the section following the presentations.

This document is intended to 

## Executive Summary Analysis
Overview of three (3) main threats. \
The top three risks identified are:
1. __End-of-Life (EOL) for OS__: High priority due to the risk associated with outdated operating systems that will no longer receive security updates.
2. __Single Point of Failure (FSI)__: High impact of data loss and operations shutdown by possiblity of single file server failure.
3. __Understaffed Security Team__: Moderate risk from inadequate incidents response and monitoring resources.

| Priority | threat | Primary Risk Owner | Risk response  |
|-|-|-|-|
|1| EOL OS                   |  CIO, Amanda Wilson    |  Mitigate: Official mitigation     |
|2| Single Point of Failure  |  CIO, Amanda Wilson    |  Mitigate: Implement Redundant FSI.|
|3| Understaffed Security    |  CISO, Paul Alexander  |  Accept: Interim coverage.         |
|-| Security insider threat  |  CISO, Paul Alexander  |  Accept: Training and Education    |

Detailed profiles have been created for each risk. 
The risk strategies identified are mostly focused on mitigation and acceptance.

<!--
Template:

## Vulnerability
#### Summary:

#### Threat profile:
__Asset__:
__Security Category__:
__Security Category reasoning__: 
__Risk owners table__:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|

__Existing vulnerability__: 

__Threat__: 
_tactical_ effect 
_strategic_ effects

__Risk strategy__: 

__Treatment__: 

__Estimated treatment schedule__: 
Treatment time calculation: \
0. Assumptions: 
...
n. Estimated total: 

__Estimated treatment cost__:
Treatment cost calculations: \
0. assumptions: 
...
n.  Estimated total: 181,000$

Recomemnded controls: missing

RMF control translation to ISO control: 

Control assesment:
-->


## 1. End-of-Life (EOL) for OS Vulnerabilities 
#### Summary:
High priority risk, EOL for 1500 operation computers. Treatment deadline 14 October 2025. Treatment time required 9 months, cost 181,000$.

#### Threat profile:
__Asset__: Main Office 1,500 Desktop Computers running Windows 10, used by employees for daily tasks. \
__Security Category__: = SC<sub>1,500 Desktops</sub> = {(Confidentiality: Moderate),(Integrity: Moderate),(Availability: High)} \
__Security Category reasoning__: asset is a core part of operations, requires high availability. While critical data is stored on file servers, desktops may still contain sensitive information, necessitating moderate confidentiality and integrity controls., \
__Risk owners table__:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|
| CIO  | Amanda Wilson     | Primary risk owner for overall management of IT & Security. | Leads the IT department, oversees information technology and security. |
| CISO | Paul Alexander    | Secondary risk owner for management of Security | Oversees information security, manages security strategies and policies. |
| Manager of Systems | William Freund | Secondary risk owner for management of systems.| Operation and maintenance of IT infrastructure. |

__Existing vulnerability__: 500 computers with the __Windows 10__ OS, used by employees for daily tasks, will no longer receive core security updates or fixes after 14 October 2025 (enter EOL).

__Threat__: End-of-Life (EOL) for operating system (OS) Vulnerabilities, \
has serrious negative _tactical_ effect on the asset. Lack of core security updates entails a weak posture for OS attacks. EOL increases likelihood of all risks. \
Negative _strategic_ effects on compliance, reputation, operations.

__Risk strategy__: Use mitigations before EOL.

__Treatment__: \
Following manifacturer's official recommendation, Windows 11 OS is freely avaible from current OS. \
First, the role of Manager of Systems and Security Techs, will ensure Windows 11 compatibility with organization systems. \
Second, find machines that can support Windows 11 at adequate performance, and upgrade those machines. \
Third, remaining Windows 10 machines must be either replaced or hardware upgraded to meet performance requirements.

__Estimated treatment schedule__: 9 months. \
Treatment time calculation: \
0. Assumptions: 1500 devices, 1000 upgradable-ready devices, 3 labour hours spent per physical upgrade.
1. Between one IT and one security roles, estimated 80 hours of compatibility testing. 
2. Time spent finding upgradable machines, estimated between 8 to 24 hours, given automated tools, scripting, and access. 
3. Time spend upgrading machine hardware: `f(x) = x * (1 - (n/x)) * t` 
> x = number of devices
> 
> n = number of upgradable devices 
>
> t = average labour hours spent per physical upgrade 
>
> f(x) = total time spent for physical upgrade
4. Estimated total: 80h + 20h + 1500h = 1600h = single employee 9 months standard work schedule. 

__Estimated treatment cost__: 181,000$ \
Treatment cost calculations: \
    0. assumptions:  1500 devices, 1000 upgradable devices, 250$ cost per upgrade, 1600 labour hours, 35$ hourly wage.
1. Treatment cost estimate: `g(x) = (x-n)*c + f(x)*h`
> x = number of devices
>
> n = number of upgrade-ready devices 
>
> c = cost per upgrade
>
> f(x) = Time spend upgrading machine hardware, labour in hours.
>
> h = hourly labour wage
2.  Estimated total: 181,000$

Recomemnded controls: -missing
RMF control <-> ISO control

Controll assesment: - missing




## 2. Single Point of Failure (SPOF)
#### Summary:
High impact to operations in likelihood of file server failure or data breach. Operational shutdown, non-compliance, reputational harm. \
The risk of relying on a single system component that could cause operational disruptions. This requires implementing redundant systems to ensure continuity. \
Treatment time required to be determined, cost 5,000$ ~ 20,000$.

#### Threat profile:
__Asset__: File System Interface (FSI). _Not only an Interface, but also a file system_ (Rocket Software, n.d.). \
__Security Category__: SC<sub>FSI</sub> = {(Confidentiality: High), (Integrity: High), (Availability: High)} \
__Security Category reasoning__: The FSI server holds data and is used organization-wide as part of operations. Case details do not indicate exact location of high value information asset, the FSI server is assumed as the central location for sensive data. \
__Risk owners table__:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|
| CIO  | Amanda Wilson     | Primary risk owner for overall management of IT. | Leads and oversees the IT department |
| Manager of Systems | William Freund | Secondary risk owner for management of systems.| Operation and maintenance of IT infrastructure. |

__Existing Vulnerability__: Dependence on a single FSI component, narrows the organization-wide file system to a single point of failure. \
__Threat__: Potential operational halt if the single point fails through human error, configurations, or attack. \
This SPOF Makes the component a high value asset for attackers. SPOF has a negative _tactical_ effect_ as it halts operations that use the FSI server. \
The threat has strong negative _strategic_ effects if the FSI server, if contains sensitive information. \
This would to a likely loss of compliance, reputation, and operations. \
__Risk Strategy__: Mitigate by adding redundant FSI server. \
__Treatment__: Implement redundancy for FSI to prevent single point failures. In case of failure, the secondary server can take over immediately, ensuring continuous access. \
Additionally, if the secondary server is in a geographically separate location, the system can serve as a disaster recovery solution. \
__Treatment Schedule and Cost__: Based on purchasing research, the inital estimated cost here is between 5000$ to 20,000$ dollars. \
The Manager of Systems must determine approprite purchases and the CIO should decide weather to support these purchases. \
Likewise, both roles must determine and support a schedule for treatment.

Recomemnded controls: missing

RMF control translation to ISO control: 

Control assesment:

# 3. Understaffed Security Team

Summary:
Current staffing levels are inadequate to handle the organization's security needs effectively. The risk is managed by accepting interim coverage while exploring long-term staffing solutions.

Threat Profile:
Asset: Security Team
Security Category: SC<sub>Security Team</sub> = {(Confidentiality: High), (Integrity: High), (Availability: Moderate)}
Existing Vulnerability: Limited personnel to address all security needs.
Threat: Potential delays in addressing security incidents and vulnerabilities.
Risk Strategy: Accept with interim coverage.
Treatment: Continue with current staffing while developing a plan for future hiring or resource allocation.
Treatment Schedule and Cost: Ongoing; cost associated with interim coverage and future recruitment.






# process (workflow)

# recommendations
DHAEI has the key elements for an ISMS required by ISO 27001 compliance (Chin, n.d.).
The organizaton has a security personnel, budget, resources, security requirements.

However, the parts are not connected as a whole through an ISMS system and it can not be said that DHAEI is currently ISO 27001 compliant.
Following this risk management plan here will be _a start_ towards standard level compliance.

As a general observation: \
Typically, companies that begin their information security programs will [start with NIST and work their way up to ISO 27001](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W4/D4/Compare%20Frameworks/CSF%20v%20ISO.md) as they scale. This industry observation seems it should apply in this case as well.



# references

Microsoft. (n.d.). End of support for Windows 10, Windows 8.1, and Windows 7. Retrieved from https://www.microsoft.com/en-ca/windows/end-of-support?r=1#:~:text=Support%20for%20Windows%2010%20will,technical%20support%20for%20Windows%2010



- What is FSI? FSI is a somewhat ambiguous term as it refers to both a file system and the interface to that file system.

Rocket Software. (n.d.). File system interface. Rocket Software. Retrieved July 29, 2024, from https://www3.rocketsoftware.com/rocketd3/support/documentation/d3nt/102/userguide/File_System_Interface.htm

(MITRE, n.d.)

- EOL OS (mitigation)
MITRE. (n.d.). Update software. MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/mitigations/M1051/

- Understaffed
MITRE. (n.d.). Defense evasion (TA0005). MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/tactics/TA0005/

-  FSI server SPOF
MITRE. (n.d.). Service stop (T1489). MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/techniques/T1489/

- Data breach impact, The adversary is trying to manipulate, interrupt, or destroy your systems and data.
MITRE. (n.d.). Impact (TA0040). MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/tactics/TA0040/

(Cybersecurity and Infrastructure Security Agency, n.d.)
- (unintentioanl) Insider threat
Cybersecurity and Infrastructure Security Agency. (n.d.). Defining insider threats. Cybersecurity and Infrastructure Security Agency. Retrieved July 29, 2024, from https://www.cisa.gov/topics/physical-security/insider-threat-mitigation/defining-insider-threats


Chin, K. (n.d.). What is an ISMS (Information Security Management System)? UpGuard. Retrieved July 29, 2024, from https://www.upguard.com/blog/isms


-------------

Resources: 
-  NIST NVD and/or MITRE ATT&CK
- [IT Team](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Employees/IT%20Team.md)
- [Organization memebers](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Employees/users_table.md)
- [Inventory. Risk & Treatment Table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing)
- [ORM](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D4/Multi-tier%20RMF,%20ORM,%20NIST%20RMF.md#orm-table)
- [What is FSI?](https://www3.rocketsoftware.com/rocketd3/support/documentation/d3nt/102/userguide/File_System_Interface.htm)
- [Cybersecurity and Privacy Reference Tool](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home)
