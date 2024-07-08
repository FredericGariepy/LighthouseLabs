Workflow:
1. ~~List assets, describe OS / software versions~~
2. ~~List labeled assets in descending priority, based on category.~~
3. [Assets](#assets) ~~Assign CIA value to asset~~
4. Assign SIL value to asset
5. Add related vulnerabilties (search MITRE, CVE , NVD)
6. Calculate(vuln + asset SIL) to get CVSS Scores
___
3. Assign CIA value to asset
> [Nist Risk Management Framework RMF Categorization](https://csrc.nist.gov/Projects/risk-management/about-rmf/categorize-step)
#### Security Category (SC) information type = {(confidentiality, impact), (integrity, impact), (availability, impact)}
> Impact values: Low, Moderate, High

- Low, loss of C.I.A. has **limited** adverse effect on organizational operations, assets, individuals, other organizations, or the Nation.
- Moderate, loss of C.I.A. has **serious** adverse effects ...
- High, loss of C.I.A. has **catastrophic** adverse effects ...

Questions/Answers to justify CIA impact levels:
- How can a malicious adversary use the information to do [limited, serious, severe] harm to organizational operations, organizational assets, or individuals?
• Would authorized disclosure or the dissemination of elements of the information type violate laws, Executive Orders, or organizational regulations?
• What is the impact associated with unauthorized modification or destruction of the information or each unauthorized use of the information by the system?
• What is the impact associated with the loss of availability of the information in the system?
___

# Informatio Asset: CIA
Security Category = {(confidentiality, High), (integrity, Moderate), (availability, low)}

### Marketing (P)
> Microsoft Windows 11 Home 10.0.22631 22631
- Marketing SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
  - Confidentiality: Leakage of PII could be used to cause severe harm to individuals and the organization.
  - Integrity : Modification or destruction would cause serious harm to operations, but possibly redeemable/recoverable though database backups, data encryptions, data segregations.
  - Availability: harm to operations, likely redeemable/recoverable, therefore limited impact.


### Sales (F) & (P)
> Microsoft Windows 11 Home 10.0.22631 22631
- Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
  - Confidentiality: Leakage of PII & Financial data could be used to cause severe harm to individuals, the organization and other orgs.
  - Integrity : Modification or destruction would cause serious harm to operations, but possibly redeemable/recoverable though database backups, data encryptions, data segregations.
  - Availability: harm to operations, likely redeemable/recoverable, therefore limited impact.


### Developer Machines (IP)
> Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
> Services with LISTENING PORTS:
> | Service      | Port            |
> |--------------|-----------------|
> | apache2      | *:80            |
> | mysqld       | 33060 \| 3306    |

- Developer Machines SC = {(confidentiality, High), (integrity, Moderate), (availability, Low)}
  - Confidentiality: Leakage of PI could be used to cause severe harm the organization and other orgs. Attackers could use information to further their attack on the organization or related third parties.
  - Integrity : Modification or destruction would cause serious harm to operations, but possibly redeemable/recoverable through GIT, backups, secrets encryptions.
  - Availability: harm to operations, likely redeemable/recoverable by use other work machines or OS images, therefore limited impact.


### Management functions (A)
> Microsoft Windows 11 Home 10.0.22631 22631
- Management SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
  - Confidentiality: Leakage of administrative info could be used to cause severe harm to individuals and the organization. By allowing attackers to plan attacks by gain of organizational information such as: schedules, plans, projects, roles.
  - Integrity : Modification or destruction would cause limited harm to operations, likely redeemable/recoverable through third party applications such as JIRA, Organizational leadership and management staff.
  - Availability: harm to operations, likely redeemable/recoverable, therefore limited impact.


### PRTG Network Monitor (SM)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> 
> PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315
- PRTG Network Monitor SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
  - Confidentiality: Leakage of Security Management info could be used to cause severe harm to individuals and the organization. By allowing attackers to plan attacks by gain of organizational information such as: sensors, thresholds, IoC detections, endpoints, traps, ports.
  - Integrity : Modification or destruction would cause serrious harm to operations ESPECIALLY if left un-noticed. Causing network monitor to be out-of-order/useless. Integrity harm is likely redeemable/recoverable through backup and restores.
  - Availability: Serrious harm to operations, primary function of Network Monitoring is availability. Likely redeemable/recoverable through load balancing, backups and restores

- SQL database (S)
  - On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
  - > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)

- Internet Information Services (IIS) webserver (S)
  - On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
  - IIS Version 10.0

- IT & Test System (S)
  - Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
