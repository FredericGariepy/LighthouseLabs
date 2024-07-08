Workflow:
1. ~~List assets, describe OS / software versions~~
2. ~~List labeled assets in descending priority, based on category.~~
3. ~~Assign CIA value to asset~~
4. ~~Assign SIL value to asset~~
5.  [Assets](#assets) ~~Add related vulnerabilties (search MITRE, CVE , NVD)~~
6. Calculate(vuln + asset SIL) to get CVSS Scores
___
5. Add related vulnerabilties.
Resources
- [NIST NVD](https://nvd.nist.gov/vuln/search)
- [CVSS](https://www.first.org/cvss/calculator/3.1)
- [MITRE CVE & ATT&CK](https://attack.mitre.org/)
- [Cyber Kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)
___
## assets
# Asset Vulnerabilities 

### Marketing (P)
> Microsoft Windows 11 Home 10.0.22631 22631
- Marketing SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
- Marketing SIL = High

### Sales (F) & (P)
> Microsoft Windows 11 Home 10.0.22631 22631
- Sales SC = {(confidentiality, High), (integrity, Moderate), (availability, low)}
- Sales SIL = High
 
### Developer Machines (IP)
> Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)
> Services with LISTENING PORTS:
> | Service      | Port            |
> |--------------|-----------------|
> | apache2      | *:80            |
> | mysqld       | 33060 \| 3306    |

- Developer Machines SC = {(confidentiality, High), (integrity, Moderate), (availability, Low)}
- Developer Machines SIL = High

### Management functions (A)
> Microsoft Windows 11 Home 10.0.22631 22631
- Management SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
- Management SIL = High

### PRTG Network Monitor (SM)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> 
> PRTG Probe 24.2.96.1315 | PRTG Server 24.2.96.1315
- PRTG Network Monitor SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
- PRTG Network Monitor SIL = Moderate


### SQL database (S)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> > The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)
-  SQL database SC = {(confidentiality, Low), (integrity, low), (availability, Moderate)}
-  SQL database SIL = Moderate


### Internet Information Services (IIS) webserver (S)
> On Windows Server : Microsoft Windows 11 Home 10.0.22631 22631
> 
> IIS Version 10.0
-  IIS webserver SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, low)}
-  IIS webserver SIL = Moderate

### Test System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
-  Test System SC = {(confidentiality, Moderate), (integrity, low), (availability, low)}
-  Test System SIL = Moderate


### IT System (S)
> Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
-  IT System SC = {(confidentiality, Moderate), (integrity, Moderate), (availability, Moderate)}
-  IT System SIL = Moderate
