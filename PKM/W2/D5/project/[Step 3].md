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

# Assets CIA
Security Category = {(confidentiality, ), (integrity, ), (availability, )}

- Marketing (P)
- Marketing SC = {(confidentiality, High), (integrity, impact), (availability, impact)}
> Microsoft Windows 11 Home 10.0.22631 22631

- Sales (F) & (P)
  - Microsoft Windows 11 Home 10.0.22631 22631

- Developer Machines (IP)
  - Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish) 
  - Services with LISTENING PORTS:
    
    | Service      | Port            |
    |--------------|-----------------|
    | apache2      | *:80            |
    | mysqld       | 33060 \| 3306    |

- Management functions (A)
  - Microsoft Windows 11 Home 10.0.22631 22631

- PRTG Network Monitor (SM)
  - On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
  - PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315

- SQL database (S)
  - On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
  - > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)

- Internet Information Services (IIS) webserver (S)
  - On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
  - IIS Version 10.0

- IT & Test System (S)
  - Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
