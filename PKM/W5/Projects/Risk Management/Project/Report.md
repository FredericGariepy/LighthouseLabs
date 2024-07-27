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




__Include the following components:__

# 0. Purpose, scope, and users

purpose: couple of main risks and scope = [Coverage and Depth](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/D1/RMF/RMF%20Stage%204%20%E2%80%93%20Assessing%20Controls%20(Part%20One).md#testing-coverage-and-depth)

### the table
[Inventory. Risk & Treatment Table](https://docs.google.com/spreadsheets/d/1tdwJMT4QcLoH7Z3jlgjyE5qsRtAtCaPpqXVqKaXtYuU/edit?usp=sharing)



> Risk __Assessment__ and Risk __Treatment__ Methodology:
# 1. Risk Assessment:


# Three threats
<!--Executuve format-->
Format \
name, \
context (vulnerability) \
threat (likelihood, impact)\
treatment  (risk response, \


## 1. Major threat: End-of-Life (EOL) for OS Vulnerabilities 
Context:
As of 14 October 2025, PCs running __Windows 10__ will still function, but Microsoft will no longer provide Security updates or fixes (Microsoft, n.d.).
1500 __Windows 10__ used by employees for daily tasks will no longer receive Security updates or fixes.

Threat:
The event will happen in less 15 months (14 October 2025). 
Without security updates or fixes, all devices are now EOL OS vulnerable. 
EOL is a serrious threat that will change from potential to immediate effective on 14 October 2025.

Treatment:
The manifacturer's official recommendation: transition to the OS version (Windows 11) if existing device can run it. Else replace or upgrade system to meet performance requirements.
To effectively take advantage of time (15 months), the 


The must be be mitigated. 
The risk response for tstrategy mitigate the 

Following the manifacturer's recommendations. The 1,500 Desktop Computers in the Main Office should be investiagated to see if upgrading the OS version is possible under 


> - The process: Explain what process you might follow. List 3 or more individuals or groups you might involve & why.

> - Assets, vulnerabilities, and threats: Based on the information provided by DE, list the 3 main threats you expect DE to face and the challenges you expect them to face while managing these threats; reflect back on vulnerabilities and threats.

- Determining the risk owners: In examination of three different risks, create a “chain” of ownership of the risk from ground level to senior executive level. Explain what and how each owner may contribute to the chain.
- Impact and likelihood: Create a table that lists three threats or risks. Reflect and document the effect of these risks on C, I, or A or more than one of these, to what extent (from 0 to 10) and how likely (0 to 5)?
- Risk acceptance criteria: Explain how the most likely / highest risk item may impact DE and explain why some items in the table may be “ignored” or “minimized” based on the information provided by DE – reflect back on your risk assignments.
2. Risk Treatment:
- Summarize the 3 main threats you have identified
- Recommended mitigations or responses you recommend for each
- Priority you would give each threat.
    - Be sure to explain your prioritizations and your recommended responses.
  

# references
Don’t forget to _reference industry standard frameworks_ to aid you in deciding on your recommended mitigations or responses.

Microsoft. (n.d.). End of support for Windows 10, Windows 8.1, and Windows 7. Retrieved from https://www.microsoft.com/en-ca/windows/end-of-support?r=1#:~:text=Support%20for%20Windows%2010%20will,technical%20support%20for%20Windows%2010
