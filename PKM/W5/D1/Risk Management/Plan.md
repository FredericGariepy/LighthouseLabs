# Risk Management Plan
###### Document
Date: 07/25/2024

This plan is for DE to: identify, assess, and manage the risks it faces, while taking into account the company's limited resources and competitive market environment.

This plan will can ensure DE is prepared to respond to the risks it faces and maintain its reputation for reliable and high-quality service.



1. Purpose, Scope, and Users, Reference Documents

Users: IT professionals, supply chain experts, and Risk Management specialists.

Purpose: This document uses the NIST RMF framework.

Scope: Establish risk assesment for all assets part of the organization.

Reference Documents:
- [Categorize Step](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D4/RMF/1.%20Categorizing%20Systems.md)
- [Select & Implementation Steps](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W4/D5/RMF)
- [Risk Assesment Table Example](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D5/Risk%20Assessment%20Table.md)


Large amounts of work will be made on the Risk Assesment and Treatment Table (below). Take a moment to observe it, then continue. \
This table will be refferenced throughout this document.
## Risk Assesment and Treatment Table
| Function | Asset Name | Asset Owner(s) | Classification | Threat | Vulnerability | Impact (0-2) | Likelihood (0-2) | Risk (=I+L) | Risk Owner | Computed Value of Risk | Proposed Risk Response | Description of the Proposed Response | Estimated Cost | Implementation Priority (1st, 2nd, 3rd) | Planned Start | Actual Start | Next Review Date | Implementing Control |
|----------|------------|----------------|----------------|--------|---------------|--------------|------------------|------------|------------|------------------------|------------------------|----------------------------------------|----------------|------------------------------------------|---------------|--------------|-----------------|-----------------------|
---

2. Risk Assessment

2.1. Inventory
Using automated or and manual technniques list all assets beloning to the organization. 

Autommated tools to detect devices on your network:
-  [nmap](https://nmap.org/)
> Use it to scan your network and detect all active devices
- [OCS Inventory NG ](https://github.com/OCSInventory-NG)
> Open Computers and Software Inventory Next Generation is an assets management and deployment solution.

Enter the asset into the Risk assesment table.



Autommated tools:
-  [OpenVas](https://www.openvas.org/)
> Set up scans to identify vulnerabilities on your network,

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

| Acronym     | Full Form                                            |
|-------------|------------------------------------------------------|
| RMF         | Risk Management Framework                            |
| ISMS        | Information Security Management System               |
| MSA         | Master Service Agreement                             |
| SoA         | Statement of Applicability                           |
| DE | Danny’s Enterprise|
