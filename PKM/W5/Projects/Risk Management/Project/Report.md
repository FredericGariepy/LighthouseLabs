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
1. End-of-Life (EOL) for OS: High priority due to the risk associated with outdated operating systems that will no longer receive security updates.
2. Single Point of Failure (FSI): High impact of data loss and operations shutdown by possiblity of single file server failure.
3. Understaffed Security Team: Moderate risk from inadequate incidents response and monitoring resources.

| Priority | threat | Primary Risk Owner | Risk response 
|-|-|-|-|
|1| EOL OS                   |  CIO, Amanda Wilson    |  Mitigate: Official mitigation     |
|2| Single Point of Failure  |  CIO, Amanda Wilson    |  Mitigate: Implement Redundant FSI.|
|3| Understaffed Security    |  CISO, Paul Alexander  |  Accept: Interim coverage.         |
|4| Security insider threat  |  CISO, Paul Alexander  |  Accept: Training and Education    |

Detailed profiles have been created for each risk. 
The risk strategies identified are mostly focused on mitigation and acceptance.

<!-- 
# each threat format \
Format \
Sumarry:
name, \
Asset: description
Security Category = SC<sub>asset</sub> = {(C:val),(I:val),(A:val)} 
risk owners: risk owners.  “chain” of ownership  botom -> top -  Explain what and how each owner may contribute to the chain. \
context (vulnerability) \
threat (likelihood, impact) (use ORM language format)\
Risk accept, ignore, mitigate, transfer. 
treatment  (risk response, controls) + Priority w/ reasoning \
... (control assesment would not be done in this report) \

-->

## 1. Major threat: End-of-Life (EOL) for OS Vulnerabilities 
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

__Treatment schedule__: \
__Estimate treatment time__: 1600 hours, as a single person 8 hour workday is 200 work days. 200 total work days, in a typical 5 work week, equals 40 weeks. 40 weeks divided by the average number of weeks per month(4.345), equals aproximately 9 months rounded down.
__Estimate assumptions__: 1500 devices, 1000 upgradable devices, 3 labour hours spent per physical upgrade. \
__Treatment time calculation__: \
Between one IT and one security roles, estimated 80 hours of compatibility testing. \
Time spent finding upgradable machines, estimated between 8 to 24 hours, given automated tools, scripting, and access. \
Time spend upgrading machine hardware, given by formula below: \
`f(x) = x * (1 - (n/x)) * t`
> x = number of devices
> 
> n = number of upgradable devices 
>
> t = average labour hours spent per physical upgrade 
>
> f(x) = total time spent for physical upgrade


__Treatment cost__: \
__Estimated cost of treatment__: 181,000$ \
__Estiamte assumptions__:  1500 devices, 1000 upgradable devices, 250$ cost per upgrade, 1600 labour hours, 35$ hourly wage. \
__Treatment cost calculaiton__: \
Treatment cost estimate, given by formula below: \
`g(x) = (x-n)*c + f(x)*h`
> x = number of devices
>
> n = number of upgradable devices 
>
> c = cost per upgrade
>
> f(x) = Time spend upgrading machine hardware, labour in hours.
>
> h = hourly labour wage







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


(Rocket Software, n.d.)
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
