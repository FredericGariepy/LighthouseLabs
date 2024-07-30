# Risk Management Case Study
Date 07.30.2024

# Table of contents
- [Executive summary](#executive-summary)
- [Purpose, scope and users of this document](#purpose-scope-and-users)
- [Executive summary analysis](#executive-summary-analysis)
  - [EOL OS Vulenrability](#1-end-of-life-eol-for-os-vulnerabilities)
  - [Single Point of Failure](#2-single-point-of-failure-spof)
  - [Understaffed security team](#3-understaffed-security-team)
- [recommended controls](#recommended-controls)
- [Conclusion](#conclusion)
- [References](#references)

# Executive Summary
This narrow risk management plan aims to address three critical security threats.

Each threat is identified within the organization (DHAEI) by evaluating its current vulnerabilities (classifying), \
then assessing potential impacts (treat assesment), and finally recommending mitigation strategies (risk treament, associated controls). 

Classification of [assets](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Assets/tangibles.md) was produced by assessing the [case information](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W5/Projects/Risk%20Management/case%20info.md) and [organization struture](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W5/Projects/Risk%20Management/Employees).

Threat assesment and treatment, are documented in the [risk __assesment__ and __treatment__ table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing) (Lighthouse Labs, n.d.).

Following this document, the reader will learn about assesment and recommended treatments for three (3) main organization threats.
<!-- and the workflow used to further generate the risk assesment. \ -->
Further, one control per threat will examined.

Consult the recommendations towards the end of this document to learn about implementing an information security management system (ISMS)
and aligning with ISO/IEC 27001 standards.

## Purpose, scope, and users
<!-- 
The purpose of this document is to define the methodology for assessment and treatment of
information risks in DHAEI, and to define the acceptable level of risk according to the ISO/IEC
27001 standard.

Risk Assessment and Risk Treatment are applied to the entire scope of the ISMS (i.e., to all
assets which are used within the organization or which could have an impact on information
security within the ISMS).
Users of this document are all employees of ACME INC. who take part in Risk Assessment and
Risk Treatment.
Note: all data is classified as confidential.
-->
This document is intended for Executives, CIOs, CISOs, IT staff, security personnel, and all DHAEI employees involved in Risk Assessment and Risk Treatment.

The purpose of this document is to identify, assess, and address the three primary threats facing the organization.
It provides a risk assessment and treatment methodology for each threat, including the application of relevant treatments and controls.

## Executive Summary Analysis
Here is short list of the top three risks identified:
1. __End-of-Life (EOL) for OS__: High priority due to the risk associated with outdated operating systems that will no longer receive security updates.
2. __Single Point of Failure (FSI)__: High impact of data loss and operations shutdown by possiblity of single file server failure.
3. __Understaffed Security Team__: Moderate risk from inadequate incidents response and monitoring resources.

Executive overview of risk ownership and response
| Priority | threat | Primary Risk Owner | Risk response  |
|-|-|-|-|
|1| EOL OS                   |  CIO, Amanda Wilson    |  Mitigate: Official mitigation     |
|2| Single Point of Failure  |  CIO, Amanda Wilson    |  Mitigate: Implement Redundant FSI.|
|3| Understaffed Security    |  CISO, Paul Alexander  |  Accept: Interim coverage.         |
<!--|-| Security insider threat  |  CISO, Paul Alexander  |  Accept: Training and Education    |-->

Detailed profiles have been created for each risk. 
The risk strategies identified are mostly focused on mitigation and acceptance.

<!--
Template:

## Vulnerability
#### Summary:

#### profile:
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

#### Profile:
__Asset__: Main Office 1,500 Desktop Computers running Windows 10, used by employees for daily tasks.

__Security Category__: = SC<sub>1,500 Desktops</sub> = {(Confidentiality: Moderate),(Integrity: Moderate),(Availability: High)}

__Security Category reasoning__: asset is a core part of operations, requires high availability. While critical data is stored on file servers, desktops may still contain sensitive information, necessitating moderate confidentiality and integrity controls.

__Risk owners table__:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|
| CIO  | Amanda Wilson     | Primary risk owner for overall management of IT & Security. | Leads the IT department, oversees information technology and security. |
| CISO | Paul Alexander    | Secondary risk owner for management of Security | Oversees information security, manages security strategies and policies. |
| Manager of Systems | William Freund | Secondary risk owner for management of systems.| Operation and maintenance of IT infrastructure. |

__Existing vulnerability__: 500 computers with the __Windows 10__ OS, used by employees for daily tasks, will no longer receive core security updates or fixes after 14 October 2025 (enter EOL).

__Threat__: End-of-Life (EOL) for operating system (OS) Vulnerabilities, has serrious negative 
_tactical_ effect on the asset. Lack of core security updates entails a weak posture for OS attacks. EOL increases likelihood of all risks. Negative _strategic_ effects on compliance, reputation, operations.

__Risk strategy__: Use mitigations before EOL.

__Treatment__: \
Following manifacturer's official recommendation, Windows 11 OS is freely avaible from current OS. \
First, the role of Manager of Systems and Security Techs, will ensure Windows 11 compatibility with organization systems. \
Second, find machines that can support Windows 11 at adequate performance, and upgrade those machines. \
Third, remaining Windows 10 machines must be either replaced or hardware upgraded to meet performance requirements (MITRE, n.d.).

__Estimated treatment schedule__: 9 months. \
Treatment time calculation: \
Assumptions: 1500 devices, 1000 upgradable-ready devices, 3 labour hours spent per physical upgrade.
1. Between one IT and one security roles, estimated 80 hours of compatibility testing.
2. Time spent finding upgradable machines, estimated between 8 to 24 hours, given automated tools, scripting, and access. 
3. Time spend upgrading machine hardware: `f(x) = (x-n) * t` 
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
Assumptions:  1500 devices, 1000 upgradable devices, 250$ cost per upgrade, 1600 labour hours, 35$ hourly wage.
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

## 2. Single Point of Failure (SPOF)
#### Summary:
High impact to operations in likelihood of file server failure or data breach. Operational shutdown, non-compliance, reputational harm.
The risk of relying on a single system component that could cause operational disruptions. This requires implementing redundant systems to ensure continuity.
Treatment time required to be determined, cost 5,000$ ~ 20,000$.

#### Profile:
__Asset__: File System Interface (FSI). _Not only an Interface, but also a file system_ (Rocket Software, n.d.).

__Security Category__: SC<sub>FSI</sub> = {(Confidentiality: High), (Integrity: High), (Availability: High)}

__Security Category reasoning__: The FSI server holds data and is used organization-wide as part of operations. Case details do not indicate exact location of high value information asset, the FSI server is assumed as the central location for sensive data.

__Risk owners table__:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|
| CIO  | Amanda Wilson     | Primary risk owner for overall management of IT. | Leads and oversees the IT department |
| Manager of Systems | William Freund | Secondary risk owner for management of systems.| Operation and maintenance of IT infrastructure. |

__Existing Vulnerability__: Dependence on a single FSI component, narrows the organization-wide file system to a single point of failure.

__Threat__: \
Potential operational halt if the single point fails through human error, configurations, or attack. (MITRE. n.d.)
This SPOF Makes the component a high value asset for attackers. SPOF has a negative _tactical_ effect as it halts operations that use the FSI server.
The threat has strong negative _strategic_ effects if the FSI server, if contains sensitive information. 
This would to a likely loss of compliance, reputation, and operations. 

__Risk Strategy__: Mitigate by adding redundant FSI server. 

__Treatment__: \
Implement redundancy for FSI to prevent single point failures. In case of failure, the secondary server can take over immediately, ensuring continuous access.
Additionally, if the secondary server is in a geographically separate location, the system can serve as a disaster recovery solution.

__Treatment Schedule and Cost__: \
Based on purchasing research, the inital estimated cost here is between 5000$ to 20,000$ dollars.
The Manager of Systems must determine approprite purchases and the CIO should decide weather to support these purchases.
Likewise, both roles must determine and support a schedule for treatment.

## 3. Understaffed Security Team
#### Summary:
Current staffing levels are inadequate to handle the organization's security needs effectively. The risk is managed by accepting interim coverage while exploring long-term staffing solutions.

#### profile:
__Asset__: Vacancy in security Team.

__Security Category__: SC<sub>Vacancy in Security Team</sub> = {(Confidentiality: Moderate), (Integrity: Moderate), (Availability: Moderate)}

__Security Category reasoning__: As one of three security tech roles, vacancy negatively impacts incident response and monitoring efforts, and introduces a temporary gaps in security operations.

__Risk owners table__:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|
| CIO  | Amanda Wilson     | Primary risk owner for overall management of IT & Security. | Leads the IT department, oversees information technology and security. |
| CISO | Paul Alexander    | Secondary risk owner for management of Security | Oversees information security, manages security strategies and policies. |
| COO | Richard Xavir      | Risk  owner for daily operations   | Approves budgets and final decisions for new hires in the security team |

__Existing vulnerability__: Vacancy in security Team role.

__Threat__: \
Inefficient human resources for Incident Response. Inadequate force for monitoring and incident response.
Threat has negative _tactical_ effect on human resources for incident reponse and monitoring performance. 
Prolonged vacancy will have negative _strategic_ effects on compliance with desired standard.

__Risk strategy__: Accept with interim coverage.

__Treatment__: Assign a temporary or cross-functional team to handle the security tasks until the position is filled.

__Treatment Schedule and Cost__: \
Role of CISO should be in charge of candidate selection, CIO in charge of CISO selection support, and COO in charge of budget aproval decision for new hire. The initial estimated average time is 3 ~ 6 months (Statista, 2024) and cost of 76,000$ (ZipRecruiter, 2024).

## Recommended controls
#### What to not expect from the following recommendations: 
This document does not focus on technical applications of controls. \
ISO 27001 compliance requires rigorous documentation of control's effectiveness through performance measures, and compliance assesment through scheduled audits. \
This level of riggor will not be found here. \
In selecting controls from the [NIST CPRT](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home) we are theoreticaly supposed to apply all of the __control numbers__ that match our __component's impact level__. \
This level of application will not be found here.

#### What can be expected: 
One recomendations will be made per presented major threat. \
However, it is important to underline that controls can also be _applied to_ and _guided by_ the organization's security requirements. \
As can be found in the [case information](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/case%20info.md#technical-requirements), the organization has __Technical, Security and User Requirements.__ \
Some of these requirements will be met through the controls presented here. This is because security needs can overlap across diffrent selected controls.

> [!NOTE]
>  NIST RMF _freely available_ documented controls have cross-refference mappings to NIST Documents. \
> (NIST Computer Security Resource Center, n.d.)
> 
> These control mappings are used in the `ISO/IEC 27001:2022` collumn below. 
>
> ISO control documents are _pay-to-access_, information about ISO controls come ISMS.online (n.d.).
>
> For `Asset IDs`, see asset ID in the [Risk Assesment Table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?gid=1152325635#gid=1152325635). 

Recomended controls table of top 3 presented threats
|Asset| Asset IDs | NIST CPRT control | ISO/IEC 27001:2022 |
|-|-|-|-|
|Windows 10 machines|1| SI-02 | A.6.8, A.8.32, A.8.8  |
|FSI server SPOF|3| CP-09 | A.5.29, A.5.33, A.8.13  |
|Vaccant Security role|4| PS-03 |  A.6.1  |

#### Window 10 OS 
[SI-02 Flaw Remediation](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=SI-02) This control is for correcting system flaws, which includes applying security-relevant software updates. It can include OS updates. It is selected to be applied to the component because of the likely High threat impact.

SI-02 can further be made to fullfils organization's technical Requirement; \
"[Ensure that all company-issued computers receive all updates that have been approved for release by the technology department.](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/case%20info.md#technical-requirements)". \
To do this, futher control configurations can enable update release aprovals. 

This NIST control SI-02 cross-refferences to ISO 27001: A.6.8, A.8.32, A.8.8.

The related ISO A.6 is family is important in ISO compliance, \ 
to establish a management framework to initiate and control the implementation and operation of information security within the organisation. \
__Example__: _schedule updates that have been released._ \
The related ISO A.8 familly regards responsibility for assets, and identifies information assets in scope for the management system and define appropriate protection responsibilities. \
 __Example__: _Apply security updates to computers we manage_.

#### FSI Server SPOF
[CP-09 System Backup](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=CP-09). This control is relevant for ensuring data recovery and maintaining the availability of information in case of failures. It is selected to be applied to the component because of the likely High threat impact.

CP-09 contributes to fufilling the organization's security requirement; \
"[Files stored on the company file servers must be protected in the event that a file server or the drives from any file server are stolen.](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/case%20info.md#security-requirements)".

This NIST CP-09 cross-reffereces to ISO 27001: A.5.29, A.5.33, A.8.13.

The related ISO A.5 regards management direction for information security, \
it has for purpose to manage direction and support for information security in line with the organisation’s requirements, as well as in accordance with relevant laws and regulations. \
 __Example__: _store data safely and support authorized access_.

The related ISO A.8 familly regards responsibility for assets, \
it serves to identify information assets in scope for the management system and define appropriate protection responsibilities. \
__Example__: _protect stored data_.

#### Vaccant Security role
[PS-03 Personnel screening](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=PS-03). This control involves ensuring that personnel are vetted before they are given access to sensitive systems and data. Used here as an initial screening for the staffing gap. Ensuring interim staff are adequately screened and suited for their temporary roles. It is selected to be applied to the component because of the likely Morderate threat impact.

PS-03 does not contribute directly to fullifing a [specifically outlined organization requirement](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/case%20info.md#user-requirements).

This NIST PS-03 cross-reffereces to ISO 27001: A.6.1.

The related ISO A.6 is family serves to establish a management framework to initiate and control the implementation and operation of information security within the organisation. \
__Example__: _screen interim staff._ 

# Conclusion
Creating a security management plan which posses risk assesment and treatment in line with ISO 27001 Apendix A, requires a lot effort. \
The document presented here lacks many features of a full plan, noticeably, SOA, gap assessment, residual risk analysys. 

The DHAEI organization has the key elements for an ISMS required by ISO 27001 compliance (Chin, n.d.). \
The organizaton has a security personnel, budget, resources, security requirements.

However, the parts are not yet connected as a whole through an ISMS system and it can not be said that DHAEI is currently ISO 27001 compliant. \
Starting by implementing this narrow risk management plan, and addressing further identified gaps using the example methodologies from this document, will be a first step toward achieving standard-level compliance.

As a general observation: \
Typically, companies that begin their information security programs will [start with NIST (CSF) and work their way up to ISO 27001](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D4/Compare%20Frameworks/CSF%20v%20ISO.md#csf-free-moneybag-iso) as they scale. This industry observation seems it should apply in this case as well.

# References
Chin, K. (n.d.). What is an ISMS (Information Security Management System)? UpGuard. Retrieved July 29, 2024, from https://www.upguard.com/blog/isms

ISMS.online. (n.d.). ISO 27001 – Annex A controls. ISMS.online. https://www.isms.online/iso-27001/annex-a-controls/

Microsoft. (n.d.). End of support for Windows 10, Windows 8.1, and Windows 7. Retrieved from https://www.microsoft.com/en-ca/windows/end-of-support?r=1#:~:text=Support%20for%20Windows%2010%20will,technical%20support%20for%20Windows%2010

Lighthouse Labs. (n.d.). Sample risk management methodology document. Retrieved July 29, 2024, from https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C5/Cyber+BC+C5.2/Sample+Risk+Management+Plan.pdf

MITRE. (n.d.). Update software. MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/mitigations/M1051/

MITRE. (n.d.). Defense evasion (TA0005). MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/tactics/TA0005/

MITRE. (n.d.). Service stop (T1489). MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/techniques/T1489/

MITRE. (n.d.). Impact (TA0040). MITRE. Retrieved July 29, 2024, from https://attack.mitre.org/tactics/TA0040/

National Institute of Standards and Technology Computer Security Resource Center. (n.d.). Mappings to NIST documents. Retrieved July 29, 2024, from https://csrc.nist.gov/projects/olir

National Institute of Standards and Technology. (2023). Cybersecurity and privacy controls for information systems and organizations (NIST SP 800-53 Rev. 5.1.1). Retrieved from https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home

Rocket Software. (n.d.). File system interface. Rocket Software. Retrieved July 29, 2024, from https://www3.rocketsoftware.com/rocketd3/support/documentation/d3nt/102/userguide/File_System_Interface.htm

<!-- (unintentioanl) Insider threat 
Cybersecurity and Infrastructure Security Agency. (n.d.). Defining insider threats. Cybersecurity and Infrastructure Security Agency. Retrieved July 29, 2024, from https://www.cisa.gov/topics/physical-security/insider-threat-mitigation/defining-insider-threats
-->

Statista. (2024). How long does it take your organization to fill a cybersecurity position with a qualified candidate? Retrieved from https://www.statista.com/statistics/1322366/cybersecurity-staffing-time-to-fill-vacancy-worldwide/

ZipRecruiter. (2024). Security technician salary. Retrieved from https://www.ziprecruiter.com/Salaries/Security-Technician-Salary
