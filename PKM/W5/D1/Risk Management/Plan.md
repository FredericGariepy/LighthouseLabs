# Risk Management Plan
###### Document
Date: 07/25/2024

# Table of Contents

- [Executive Summary](#executive-summary)
- [Referenced Documents](#referenced-documents)
- [1. Purpose, Scope, and Users, Reference Documents](#1-purpose-scope-and-users-reference-documents)
- [2. Categorize Inventory (1/2)](#2-categorize-inventory-12)
  - [Asset Management Table](#asset-management-table)
- [2. Categorize Inventory (2/2)](#2-categorize-inventory-22)
  - [CIA Values table](#cia-values-table)
- [4. Risk Assessment (1/4)](#4-risk-assessment-14-start-filling-table-with-basic-information-from-step-3)
  - [Risk Assessment and Treatment Table](#risk-assessment-and-treatment-table)
- [4. Risk Assessment (2/4)](#4-risk-assessment-24-find-existing-vulnerabilities-in-assets)
- [4. Risk Assessment (3/4) ](#4-risk-assessment-34-add-threats-risk-owners-likelihood-impact-risk-scores)
  - [Impact and Likelihood scoring table](#impact-and-likelihood-scoring-table)
- [4. Risk Assessment (4/4)](#4-risk-assessment-44-select-controls-risk-response-treatment-details-monitoringreview)
- [5. Missing parts](#5-missing-parts)
- [6. Validity and Document Management](#6-validity-and-document-management)
- [References](#references)
- [Glossary](#glossary)


## Executive Summary
This plan is for [DE](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/D1/Risk%20Management/Assingment.md) to: identify, assess, and manage the risks it faces, while taking into account the company's limited resources and competitive market environment.
This plan will can ensure DE is prepared to respond to the risks it faces and maintain its reputation for reliable and high-quality service. \
The plan takes inspiration from the NIST RMF.

## Referenced Documents
- [Categorize Step](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D4/RMF/1.%20Categorizing%20Systems.md)
- [Select & Implementation Steps](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W4/D5/RMF)
- [Risk Assesment Table Example](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D5/Risk%20Assessment%20Table.md)
- NIST  SP 800-53 [Access Controll Familly](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=AC)

## 1. Purpose, Scope, and Users, Reference Documents:
__Users__: IT professionals, supply chain experts, and Risk Management specialists. \
__Purpose__: This document uses the NIST RMF framework. \
__Scope__: Establish risk assesment for all assets part of the organization.

## 2. Categorize Inventory (1/2)
#### All systems must be registered and documented.
System registration facilitates management of assets and is used as a tracking tool.

Roles in charge: IT professionals

Using automated or and manual technniques list all assets beloning to the organization. \
Autommations and tools to detect and make an inventory devices on your network:
-  [nmap](https://nmap.org/) Use it to scan your network and detect all active devices.
- [OCS Inventory NG ](https://github.com/OCSInventory-NG) Open Computers and Software Inventory is an assets management and deployment solution.
- Content Management System (CMS)
- Enterprise Mission Assurance Support System (eMASS)
- Telos XACTA

Fill out the Asset Management Table, and enter it into your Enterprise IT Registry.
- Do not yet fill Integrity, Availability, Security, Category Score
- Asset Type = Software, Hardware, Information (in physical or electronic form)
- Purpose = Use it to add context 
### Asset Management Table
| Asset ID | Asset Name | Asset Type | Asset Owner(s) | Location | Version Number | IP Address | MAC Address | Purpose | Confidentiality | Integrity | Availability | Security Category Score |
|----------|------------|------------|----------------|----------|----------------|------------|-------------|---------|----------------|-----------|--------------|-------------------------|

## 2. Categorize Inventory (2/2)
#### Add CIA values and SCS to the Asset Management Table
Each asset will now receive a CIA values, the score of each value is based on the respective __loss__ brought to the organization by an attack.

Roles in charge: Risk Management specialists

Equation: \
SC<sub>Information</sub> = {(C:val),(I:val),(A:val)} \
SC<sub>Information System</sub> =  {(C:val),(I:val),(A:val)} 

CIA values are assigned scores according this table:
### CIA Values table
| Attribute       | Low (1)                      | Moderate (2)                  | High (3)                       |
|-----------------|------------------------------|--------------------------------|--------------------------------|
| Confidentiality | Public, minimal sensitivity  | Requires protection            | Highly sensitive, severe impact if leaked |
| Integrity       | Minor impact if altered      | Significant impact if corrupted| Critical, severe impact if altered |
| Availability    | Minimal impact if unavailable| Moderate impact, some disruption| Major impact, operation failure |

Security Category Score (SCS), are calculated by taking the higest value from the SC<sub>Asset</sub>. \
This follows NIST SP 800-53 ussing a high-water mark (NIST, 2013). 

Add the SCS value to the Asset Management Table.

Sort the Asset Management Table by SC score, this will _help* to better reflect_ asset priorities.

## 4. Risk Assesment (1/4) Start filling table with basic information from Step 3
#### Fill Risk Assesment with information found in Asset Management Table
With the completed Asset Management Table, \
Fill in the Risk Assesment and Treatment Table (below) \
__Add__: Asset ID, SC Score, Function, Asset Name, Asset Owner(s)

Roles in charge: Risk Management specialists

> [!NOTE]
> Function is based on Asset type. \
> Function = Hardware, Software, Information (in physical or electronic form) 
### Risk Assesment and Treatment Table
| Asset ID | SC Score | Function (based on Asset type) | Asset Name | Asset Owner(s) | Vulnerability | Threat | Impact (0-2) | Likelihood (0-2) | Risk (=I+L) | Risk Owner | Computed Value of Risk ($) | Proposed Risk Response | Description of the Proposed Response | Estimated Cost ($) | Implementation Priority (1st, 2nd, 3rd) | Planned Start | Actual Start | Next Review Date | Implementing Control |
|----------|----------|---------------------|------------|----------------|--------|---------------|--------------|------------------|------------|------------|--------------------------|------------------------|----------------------------------------|--------------------|------------------------------------------|---------------|--------------|-----------------|-----------------------|

## 4. Risk Assesment (2/4) Find existing vulnerabilities in assets
#### For each asset, find existing vulnerabilities (manualy or with automated tools)

Roles in charge: Risk Management specialists

##### Manual
To __manually__ look for vulnerabilities Using the Asset Management Table:
1. Reseach the asset name, version number, to find officially documented manifacturer/developer vulnerabilities.
2. Reseach the asset name, version number in NVD 
    1. Find __asset related CVE__, and CVE details. \
       Use: [cvedetails](https://www.cvedetails.com/vulnerability-list/) \
       Use: [VND search](https://nvd.nist.gov/vuln/search) \
       Use: Your research skills.
    2. Read the CVE and look for:
       CVE for description, listed mitigations, listed CV score, links to CWE. \
       Use [CWE](https://cwe.mitre.org/) for vulnerability category and mitigations. \
       If you found a documented vector, plug it into NVD CVSS v3.x Calculator. \
       Else, Use CVSS NVD CVSS v3.x Calculator to calculate CVS. \
   3. In the End, you should have: Vulnerabilities, related CVE threat, and CVSs. \

##### Automated
To use __Autommated tools__:
Use the Asset Management Table and feed the relevant informaiton (IP, MAC, Version number) to automated vulnerability detection systems:
-  For systems: [OpenVas](https://www.openvas.org/)
-  For Web Apps: [Owasp ZAP](https://www.zaproxy.org/)

Write down the vulnerabilities found for each assets.

## 4. Risk Assesment (3/4) Add threats, risk owners, likelyhood, impact, risk scores.

Roles in charge: Risk Management specialists, Risk Owners

The roles in charge must now assign Risk Owners to each asset.
- __Write the Risk Owner__ for each asset in Risk Assesment and Treatment Table.

The roles in charge, must now assign threats to each vulnerability
- __Write the threat for each vulnerability.__

The roles in charge, must now assign each risk : Impact, Likelihood rating. \
Use the Impact and Likelihood scoring table (below): 
### Impact and Likelihood scoring table.
|           | 0 - Low | 1 - Moderate | 2 - High |
|-----------|-----------------|---------------------|-----------------|
| Impact    | No significant effect | Moderate impact on obligations | Severe impact on operations |
| Likelyhood| unlikely | possible | likely |

Now __add risk scores__ which are the sum of the Impact and Likelyhood values:
- Risk = Impact + Likelyhood

## 4. Risk Assesment (4/4) Select Controls (Risk response), treatment details, monitoring(review).
#### For each risk, assign an access controll. Write the treatment details.

Roles in charge: Risk Management specialists, IT professionals

The roles in charge will select controls for each risk. \
Chose the controls from the comprehensive NIST control families:
- NIST SP 800-53 [Control Families](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home)
This security plan reccomends using the Access Controll Familly:
- NIST  SP 800-53 [Access Controll Familly](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=AC)

Once a control has been selected and writen in the Risk Assesment and Treatment Table, \
The roles in charge must fill in the remaining table collumns: \
Description of the Proposed Response, Estimated Cost ($), Implementation Priority (1st, 2nd, 3rd), Planned Start, Actual Start, Next Review Date, Implementing Control.
 
It is important at this time that a robust monitoring solution is thought out by the Risk Management specialists. \
The review should be conducted at least once a year, or more frequently in the case of significant organizational changes, significant change in
technology, change of business objectives, changes in the business environment, etc.

## 5. Missing parts
because I ain't got no time. \
Plan acceptance by Seniors, Statement of Applicability (SoA), terms of service, a bunch of other stuff...

## 6. Validity and Document Management
This document is valid as of July 25 2024. \
The owner of this document is the Information Security Analyst, who must check and, if necessary, update the document at least once a year before the regular review of existing Risk

## References
National Institute of Standards and Technology. (2013). Security and privacy controls for federal information systems and organizations (Special Publication 800-53 Rev. 4). https://csrc.nist.gov/files/pubs/sp/800/53/r4/final/docs/sp800-53-rev4-ipd.pdf

## Glossary
| Acronym     | Full Form                                            |
|-------------|------------------------------------------------------|
| RMF         | Risk Management Framework                            |
| ISMS        | Information Security Management System               |
| MSA         | Master Service Agreement                             |
| SoA         | Statement of Applicability                           |
| DE | Danny’s Enterprise|
