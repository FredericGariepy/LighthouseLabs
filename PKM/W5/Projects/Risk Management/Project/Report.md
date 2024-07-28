# Risk Management Case Study

Fucked up stuff
- Vacant seat/ intern  
- Windows 10, EOF
- Windows 2019 server OEF [End of servicing](https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info)
- [EOS vs EOL](https://www.leanix.net/en/wiki/trm/what-is-end-of-life-vs-end-of-support#What-is-End-of-Support-End-of-Service-Life)
- L2TP VPN Client (Remote Workers), maybe not the best [nord vpn about l2tp](https://nordvpn.com/blog/l2tp-protocol/)
- L2TP VPN Client,  [avast](https://www.avast.com/c-vpn-protocols)
- Security    Speed    Popularity 
- L2TP    Strong    Slow    Low 

- L2P https://nordvpn.com/blog/l2tp-protocol/

Project Description
> The purpose of __Risk Management__ is to _systematically find out which incidents can happen_ to an organization.
> _Apply the process of_ __Risk Treatment__ to minimize the damage of such incidents in an organization.

Resources: 
-  NIST NVD and/or MITRE ATT&CK
- [IT Team](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Employees/IT%20Team.md)
- [Organization memebers](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Employees/users_table.md)
- [Inventory. Risk & Treatment Table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing)
- [ORM](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D4/Multi-tier%20RMF,%20ORM,%20NIST%20RMF.md#orm-table)
Deliverables: 
> Create a Risk Management Plan
>
> Executive Summary


# Executive Summary
Report is an Executive Summary that captures risk management process.
- Executive summary that gives _insight_ into the case
- Risk Assessment and Identification
- Recommendations for Risk Treatment.
- Executive Summary in the business language

This document was produced by assessing the [case information](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W5/Projects/Risk%20Management/case%20info.md), [organization struture](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W5/Projects/Risk%20Management/Employees) and [organization assets](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/Projects/Risk%20Management/Assets/tangibles.md) to fill the basics in the [risk __assesment__ and __treatment__ table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing).

The Report is not complete.
Follow this document to read about the reccomnnded treatmens of main threats, and the workflow used to further generate the risk assesment. \ 
To further bring this report into compliance with ISO 27001 see the recomendations at the end.





# 0. Purpose, scope, and users

purpose: couple of main risks and scope = [Coverage and Depth](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/D1/RMF/RMF%20Stage%204%20%E2%80%93%20Assessing%20Controls%20(Part%20One).md#testing-coverage-and-depth)

### the table
[Inventory. Risk & Treatment Table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing)




### Overview of Three threats

| Priority | threat | Primary Risk Owner | Priority | Mitigation |
|----------|--------|------------|------------|------------|
|     1<sub>rst</sub>    | EOL OS|      CIO, Amanda Wilson      |    4      |     official fix |
|     2<sub>nd</sub>     |        |            |            |            |
|     3<sub>rd</sub>     |        |            |            |            |
|          |        |            |            |            |


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
Summary:

Asset:\
Main Office 1,500 Desktop Computers running Windows 10, used by employees for daily tasks. \
Security Category = SC<sub>1,500 Desktops</sub> = {(Confidentiality: High),(Integrity: Moderate),(Availability: High)} \
Security Category reasoning: asset is a core part of operations. 
Risk owners table:
| **Role** | **Name** | **Responsibility Share** | **Key Responsibilities** |
|-|-|-|-|
| CIO  | Amanda Wilson     | Primary risk owner for overall management of IT & Security. | Leads the IT department, oversees information technology and security. |
| CISO | Paul Alexander    | Secondary risk owner for management of Security | Oversees information security, manages security strategies and policies. |
| Manager of Systems | William Freund | Secondary risk owner for management of systems.| Operation and maintenance of IT infrastructure. |

Existing vulnerability: \
1500 computers with the __Windows 10__ OS, used by employees for daily tasks, will no longer receive core security updates or fixes after 14 October 2025 (enter EOL). \

Threat: \
End-of-Life (EOL) for operating system (OS) Vulnerabilities, \
has serrious negative _tactical_ effect on the asset. Lack of core security updates entails a weak posture for OS attacks. EOL increases likelihood of all risks. \
Negative _strategic_ effects on compliance, reputation, operations. \

Risk strategy: Use mitigations before EOL.

Treatment: \
Following manifacturer's official recommendation, Windows 11 OS is freely avaible from current OS. \
First, the role of Manager of Systems and Security Techs, will ensure Windows 11 compatibility with organization systems. \
Second, find machines that can support Windows 11 at adequate performance, and upgrade those machines. \
Third, remaining Windows 10 machines must be either replaced or hardware upgraded to meet performance requirements.

Treatment schedule. \
Estimate treatment time: 1600 hours, or in single person 8 hour workday: 200 work days. \
Estimate assumptions: 1500 devices, 1000 upgradable devices, 3 labour hours spent per physical upgrade. \
Treatment time calculation: \
Between one IT and one security roles, estimated 80 hours of compatibility testing. \
Time spent finding upgradable machines, estimated between 8 to 24 hours, given automated tools, scripting, and access.
Time spend upgrading machine hardware, given by formula below. \
`f(x) = x * (1 - (n/x)) * t`
> x = number of devices
> n = number of upgradable devices 
> t = average labour hours spent per physical upgrade 
> f(x) = total time spent for physical upgrade

Estimated cost of treatment: 181,000$
Cost assumptions:  1500 devices, 1000 upgradable devices, 250$ cost per upgrade, 1600 labour hours, 35$ hourly wage. \
Treatment cost estimate, given by formula below. \
`g(x) = (x-n)*c + f(x)*h`
> x = number of devices
> n = number of upgradable devices 
> c = cost per upgrade
> f(x) = Time spend upgrading machine hardware, labour in hours.
> h = hourly labour wage


Estimated treatment 








<!-- 
treatment  (risk response, controls) + Priority w/ reasoning \
... (control assesment would not be done in this report) \
-->


Following the manifacturer's recommendations. The 1,500 Desktop Computers in the Main Office should be investiagated to see if upgrading the OS version is possible under 



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


# references
Don’t forget to _reference industry standard frameworks_ to aid you in deciding on your recommended mitigations or responses.

Microsoft. (n.d.). End of support for Windows 10, Windows 8.1, and Windows 7. Retrieved from https://www.microsoft.com/en-ca/windows/end-of-support?r=1#:~:text=Support%20for%20Windows%2010%20will,technical%20support%20for%20Windows%2010




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
