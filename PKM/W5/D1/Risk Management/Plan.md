# Risk Management Plan
###### Document
Date: 07/25/2024


- [Executive Summary](#executive-summary)
- [Referenced Documents](#referenced-documents)
- [Purpose, Scope, and Users, Reference Documents](#1-purpose-scope-and-users-reference-documents)
- [Categorize Inventory (1/2)](#2-categorize-inventory-12)
- [Asset Management Table](#asset-management-table)
- [Categorize Inventory (2/2)](#2-categorize-inventory-22)
- [CIA Values Table](#cia-values-table)
- [Risk Assessment (1/4)](#4-risk-assessment-14-start-filling-table-with-basic-information-from-step-3)
- [Risk Assessment and Treatment Table](#risk-assessment-and-treatment-table)
- [Risk Assessment (2/4)](#4-risk-assessment-24-find-existing-vulnerabilities-in-assets)
- [Risk Assessment (3/4)](#4-risk-assessment-34-add-threats-risk-owners-likelihood-impact-risk-scores)
- [Impact and Likelihood Scoring Table](#impact-and-likelihood-scoring-table)
- [Risk Assessment (4/4)](#4-risk-assessment-44-select-controls-risk-response-treatment-details-monitoring-review)
- [References](#references)


## Executive Summary
This plan is for DE to: identify, assess, and manage the risks it faces, while taking into account the company's limited resources and competitive market environment.
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
__Scope__: Establish risk assesment for all assets part of the organization. \

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



3.1.1. The Process
Risk Assessment is implemented through the Risk Assessment Table. The Risk Assessment
process is coordinated by the information security analyst, identification of threats and
vulnerabilities is performed by asset owners, and assessment of consequences and likelihood is
performed by risk owners. ACME INC. in selective situations will have the same asset owner
and risk owner for a given asset.
3.1.2. Assets, Vulnerabilities, and Threats
The first step in Risk Assessment is the identification of all assets in the ISMS scope (i.e., of all
assets which may affect the confidentiality, integrity, and availability of information at MHS).
Assets may include documents in paper or electronic form, applications and databases, people,
IT equipment, infrastructure, and external services/outsourced processes. When identifying
assets, it is also necessary to identify their owners (the person or organizational unit responsible
for each asset).
The next step is to identify all threats and vulnerabilities associated with each asset. Threats
and vulnerabilities are identified using the catalogues included in the Risk Assessment Table.
Every asset may be associated with several threats, and every threat may be associated with
several vulnerabilities.
3.1.3. Determining the Risk Owners
For each risk, a risk owner has to be identified—the person or organizational unit responsible for
each risk. This person may or may not be the same as the asset owner.
3.1.4. Impact and Likelihood
Once risk owners have been identified, it is necessary to assess impacts for each combination
of threats and vulnerabilities for an individual asset if such a risk materializes:
High Impact 2 Loss of confidentiality, availability, or integrity has considerable and/or
immediate impact on the organization's cash flow,
operations, legal or contractual obligations, or its reputation.
Moderate
Impact
1 Loss of confidentiality, availability, or integrity incurs costs and has a
low or moderate impact on legal or contractual obligations, or the
organization's reputation.
Low Impact 0 Loss of confidentiality, availability, or integrity does not affect the
organization's cash flow, legal or contractual obligations, or its
reputation.
After the assessment of consequences, it is necessary to assess the likelihood of occurrence of
such a risk (i.e., the probability that a threat will exploit the vulnerability of the respective asset):
High Likelihood 2 Existing security controls are low or ineffective. Such incidents have a
high likelihood of occurring in the future.
Moderate
Likelihood 1
Existing security controls are moderate and have mostly provided an
adequate level of protection. New incidents are possible, but not
highly likely.
Low Likelihood 0 Existing security controls are strong and have so far provided an
adequate level of protection. No new incidents are expected in the
future.
By entering the values of consequence and likelihood into the Risk Assessment Table, the level
of risk is calculated automatically by adding up the two values. Existing security controls are to
be entered in the last column of the Risk Assessment Table.
3.2. Risk Acceptance Criteria
Values 0, 1, and 2 are acceptable risks, while values 3 and 4 are unacceptable risks.
Unacceptable risks must be treated.
3.3. Risk Treatment
Risk Treatment is implemented through the Risk Treatment Table, by copying all risks identified
as unacceptable from the Risk Assessment Table. Risk Treatment is conducted by the risk
owner.
One or more treatment options must be selected for risks valued 3 and 4:
● Selection of security control or controls from Annex A of the ISO/IEC 27001 standard or
some other security controls.
● Transferring the risks to a third party (e.g., by purchasing an insurance policy or signing
a contract with suppliers or partners).
● Avoiding the risk by discontinuing a business activity that causes such risk.
● Accepting the risk. This option is allowed only if the selection of other Risk Treatment
options would cost more than the potential impact should such risk materialize.
The selection of options is implemented through the Risk Treatment Table. Usually, option one
is selected: selection of one or more security controls. When several security controls are
selected for a risk, then additional rows are inserted into the table immediately below the row
specifying the risk.
The treatment of risks related to outsourced processes must be addressed through the
contracts with responsible third parties, as specified in the corresponding MSA.
In the case of option one (selection of security controls), it is necessary to assess the new value
of consequence and likelihood (residual risk) in the Risk Treatment Table, in order to evaluate
the effectiveness of planned controls.
3.4. Regular Reviews of Risk Assessment and Risk Treatment
Risk owners must review existing risks and update the Risk Assessment Table and Risk
Treatment Table in line with newly identified risks. The review is conducted at least once a year,
or more frequently in the case of significant organizational changes, significant change in
technology, change of business objectives, changes in the business environment, etc.
3.5. SoA and Risk Treatment Pplan
The information security analyst must document the following in the SoA: which security controls
from Annex A of the ISO/IEC 27001 standard are applicable and which are not, the justification
for such decisions, and whether they are implemented or not.
On behalf of the risk owners, ACME INC, the Senior Leadership Team (SLT) will accept all
residual risks through the SoA.
The information security analysts will prepare the Risk Treatment plan in which the
implementation of controls will be planned. On behalf of the risk owners, the SLT will approve
the Risk Treatment plan.
3.5. Reporting
The information security analyst will document the results of Risk Assessment and Tisk
Treatment, and all of the subsequent reviews, in the Risk Assessment and Treatment Report.
The information security analyst will monitor the progress of implementation of the Risk
Treatment plan and report the results to organizational unit heads each month.
3. Managing Records Kept on the Basis of this Document
Record Name Storage Location Person
Responsible for
Storage
Control for Record
Protection
Retention
Time
Risk Assessment
Table (electronic
form Excel
document)
Information
Security
Manager’s
computer
Information
Security Analyst
Only the Information
Security Manager has
the right to make
entries into and
changes to the Risk
Assessment Table
Data is stored
permanently
Risk Treatment
Table (electronic
form Excel
document)
Information
Security
Manager’s
computer
Information
Security Analyst
Only the Information
Security Manager has
the right to make
entries into and
changes to the Risk
Treatment Table
Data is stored
permanently
SoA Information
Security
Manager’s
computer
Information
Security Analyst
Only the Information
Security Manager has
the right to make
entries into and
changes to the SoA
Older
versions of
SoA are
stored for a
period of
three years
Risk Treatment
Plan (electronic
form Word
document)
Information
Security
Manager’s
computer
Information
Security Analyst
Only the Information
Security Manager has
the right to make
entries into and
changes to the Risk
Treatment Plan
Older
versions of
Risk
Treatment
Plan are
stored for a
period of
three years
Only the Information Security Manager can grant other employees’ access to any of the above
mentioned documents.
4. Validity and Document Management
This document is valid as of April 2021.
The owner of this document is the Information Security Analyst, who must check and, if
necessary, update the document at least once a year before the regular review of existing Risk
Assessment.
5. Appendices
● Appendix 1: Risk Assessment Table
● Appendix 2: Risk Treatment Table
Appendix A – Risk Assessment Table
ID
# Asset Name Asset Owner Threat Vulnerabil
ity
Impact
(0-2)
Likelihoo
d
(0-2)
Risk
(=I+L)
Notes
Appendix B – Risk Treatment Table
This spreadsheet is a continuation from the Risk Assessment Table spreadsheet.
ID
#
Comput
ed
Value of
Risk
Proposed
Risk
Response
Descriptio
n of the
Proposed
Response
Estimated
Cost
Implement
ation
Priority
(1-3)
Planned
Start Review Date Planned
Closure

## Refferences

National Institute of Standards and Technology. (2013). Security and privacy controls for federal information systems and organizations (Special Publication 800-53 Rev. 4). https://csrc.nist.gov/files/pubs/sp/800/53/r4/final/docs/sp800-53-rev4-ipd.pdf



| Acronym     | Full Form                                            |
|-------------|------------------------------------------------------|
| RMF         | Risk Management Framework                            |
| ISMS        | Information Security Management System               |
| MSA         | Master Service Agreement                             |
| SoA         | Statement of Applicability                           |
| DE | Danny’s Enterprise|
