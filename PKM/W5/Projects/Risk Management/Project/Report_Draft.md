TO DO 7/30

- [x] ~~In intro mention that typically, companies use NIST RMF, if they dont have securit in place, and then work their way up to ISO (check PKM for ref)~~ put it in the end
- [x] ~~Finish report of main threats~~
- [x] ~~Add controls~~
- [x] ~~Document relevant ISO/IEC Mapings [example](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=MA-06)~~
- [x] ~~Write a replicable workflow~~
- [x] ~~finish cosiderations, suggest ISMS (basically get a SIEM), mention security department infancy, ISO 270001 Apendix A checklist.~~
- [x] ~~Write exec, Finish and submit.~~


# some RMF controsl
RMF - check equivalent in ISO 27001 Apendix A
[MA-03(06)	maintenance tools are inspected to ensure that the latest software updates and patches are installed.](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=MA-03)

FSI file seerver/ data breach [Contingency planning](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=CP-02)

[CP-04 CONTINGENCY PLAN TESTING ](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=CP-04)

[CP-09 SYSTEM BACKUP ](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=CP-09)

[CP-10 SYSTEM RECOVERY AND RECONSTITUTION ](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=CP-10)

## ISO controls
- [Best available free resource](https://www.isms.online/iso-27001/annex-a-controls/)



# Risk Management Case Study

Fucked up stuff
- Vacant seat/ intern  
- Windows 10, EOF
- Windows 2019 server OEF [End of servicing](https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info)
- [EOS vs EOL](https://www.leanix.net/en/wiki/trm/what-is-end-of-life-vs-end-of-support#What-is-End-of-Support-End-of-Service-Life)

<!-- 
- L2TP VPN Client (Remote Workers), maybe not the best [nord vpn about l2tp](https://nordvpn.com/blog/l2tp-protocol/)
- L2TP VPN Client,  [avast](https://www.avast.com/c-vpn-protocols)
- Security    Speed    Popularity 
- L2TP    Strong    Slow    Low 
- L2P https://nordvpn.com/blog/l2tp-protocol/ 
-->

Needs: \
systems meet a minimum level of security and that its information is protected from attacks \
collect and act on security events from across its digital estate \
establish a network infrastructure to provide authentication, authorization, and accounting of its network assets \
contingency system in place in a form of load-balancing and cluster management to provide redundancy and risk mitigation.

<!--
> The purpose of __Risk Management__ is to _systematically find out which incidents can happen_ to an organization.
> _Apply the process of_ __Risk Treatment__ to minimize the damage of such incidents in an organization.
-->

Resources: 
-  NIST NVD and/or MITRE ATT&CK
- [IT Team](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Employees/IT%20Team.md)
- [Organization memebers](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Employees/users_table.md)
- [Inventory. Risk & Treatment Table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing)
- [ORM](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D4/Multi-tier%20RMF,%20ORM,%20NIST%20RMF.md#orm-table)
- [What is FSI?](https://www3.rocketsoftware.com/rocketd3/support/documentation/d3nt/102/userguide/File_System_Interface.htm)
- [Cybersecurity and Privacy Reference Tool](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home)
<!--
Deliverables: 
> Risk Management Plan
>
> Executive Summary
-->

# Executive Summary
<!--
Report is an Executive Summary that captures risk management process.
- Executive summary that gives _insight_ into the case
- Risk Assessment and Identification
- Recommendations for Risk Treatment.
- Executive Summary in the business language
-->
This risk management document focuses on existing and important pressing security matters. \
It was produced by assessing the [case information](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W5/Projects/Risk%20Management/case%20info.md), [organization struture](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W5/Projects/Risk%20Management/Employees) and [organization assets](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Assets/tangibles.md) to make a [risk __assesment__ and __treatment__ table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing).

Follow this document to learn about recommended treatments for three(3) main threats, and the workflow used to further generate the risk assesment. \ 
To further bring this report into compliance with ISO 27001 see the recomendations at the end.


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
The purpose of this document is to identify and present the three main threats to existing vulnerabilities, utilizing risk assessment and treatment methodologies described in the section following this presentation.

purpose: couple of main risks and scope = [Coverage and Depth](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/D1/RMF/RMF%20Stage%204%20%E2%80%93%20Assessing%20Controls%20(Part%20One).md#testing-coverage-and-depth)




### Overview of three (3) main threats
| Priority | threat | Primary Risk Owner | Risk response |
|-|-|-|-|
|1<sub>rst</sub>    | EOL OS                   |  CIO, Amanda Wilson      |  Mitigate: Official mitigation     |
|2<sub>nd</sub>     | Single Point of Failure   |  CIO, Amanda Wilson    |  Mitigate: Implement Redundant FSI.         |
|3<sub>nd</sub>     | Understaffed Security    |  CISO, Paul Alexander    |  Accept: Interim coverage.         |
|3<sub>rd</sub>     | Security insider threat  |  CISO, Paul Alexander    |  Accept: Training and Education    |


<!--
> - The process: Explain what process you might follow. List 3 or more individuals or groups you might involve & why.

> - Assets, vulnerabilities, and threats: Based on the information provided by DE, list the 3 main threats you expect DE to face and the

> - challenges you expect them to face while managing these threats; reflect back on vulnerabilities and threats.
-->


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






-----------


<!-- format-
Format \
name, \
Asset: description, risk owners.  “chain” of ownership  botom -> top \
-  Explain what and how each owner may contribute to the chain.

context (vulnerability) \
threat (likelihood, impact) (use ORM language format)\
Risk accept, ignore, mitigate, transfer. 
treatment  (risk response, controls) + Priority w/ reasoning \
... (control assesment would not be done in this report) \
-->

# process (workflow)

# considerations
Implement an ISMS... u got none

# references
Don’t forget to _reference industry standard frameworks_ to aid you in deciding on your recommended mitigations or responses.

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

#---------------------------

> - The process: Explain what process you might follow. List 3 or more individuals or groups you might involve & why.

> - Assets, vulnerabilities, and threats: Based on the information provided by DE, list the 3 main threats you expect DE to face and the
> - challenges you expect them to face while managing these threats; reflect back on vulnerabilities and threats.

- Determining the risk owners:
- In examination of three different risks,
- create a “chain” of ownership of the risk from ground level to senior executive level.
-  Explain what and how each owner may contribute to the chain.


- Impact and likelihood:
- Create a table that lists three threats or risks.
-  Reflect and document the effect of these risks on C, I, or A or more than one of these,
-  to what extent (from 0 to 10) and how likely (0 to 5)?
  
- Risk acceptance criteria:
- Explain how the most likely / highest risk item may impact DE and explain why some items in the table may be “ignored” or “minimized”
- based on the information provided by DE – reflect back on your risk assignments.
  
2. Risk Treatment:
- Summarize the 3 main threats you have identified
- Recommended mitigations or responses you recommend for each
- Priority you would give each threat.
- Be sure to explain your prioritizations and your recommended responses.
  


    Purpose, scope, and users
    Risk Assessment and Risk Treatment Methodology:
        2.1 Risk Assessment:
            The process: Explain what process you might follow. List 3 or more individuals or groups you might involve & why.
            Assets, vulnerabilities, and threats: Based on the information provided by DE, list the 3 main threats you expect DE to face and the challenges you expect them to face while managing these threats; reflect back on vulnerabilities and threats.
            Determining the risk owners: In examination of three different risks, create a “chain” of ownership of the risk from ground level to senior executive level. Explain what and how each owner may contribute to the chain.
            Impact and likelihood: Create a table that lists three threats or risks. Reflect and document the effect of these risks on C, I, or A or more than one of these, to what extent (from 0 to 10) and how likely (0 to 5)?
            Risk acceptance criteria: Explain how the most likely / highest risk item may impact DE and explain why some items in the table may be “ignored” or “minimized” based on the information provided by DE – reflect back on your risk assignments.
        2.2 Risk Treatment: Summarize the 3 main threats you have identified above, what recommended mitigations or responses you recommend for each and what priority you would give each one. Be sure to explain your prioritizations and your recommended responses. Don’t forget to reference industry standard frameworks to aid you in deciding on your recommended mitigations or responses.

Executive Su
