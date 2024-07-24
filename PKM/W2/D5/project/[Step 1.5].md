Workflow:
1. [Assets](#assets)~~List assets, describe OS / software versions~~
    - 1.5 Make data collected about Asset's OS/Software streamlined for step 2   <--You are here
2. List labeled assets in descending priority, based on category.
3. Assign CIA value to asset
4. Assign SIL value to asset
5. Add related vulnerabilties (search MITRE, CVE , NVD)
6. Calculate(vuln + asset SIL) to get CVSS Scores
___

1.5 Make data collected about Asset's OS/Software streamlined for step 2

---
# Assets
## - Windows Server (S) (SM) - 
#### Windows OS:
Microsoft Windows 11 Home 10.0.22631 22631
#### SQL database (S):
> The Win 11 VM does not have an mySQL database installed. [fact source](https://github.com/FredericGariepy/LighthouseLabs/edit/main/PKM/W2/D5/project/%5BSTEP%201%5D.md)
#### Internet Information Services (IIS) webserver (S):
IIS Version 10.0
#### PRTG Network Monitor (SM):
- PRTG Probe 24.2.96.1315
- PRTG Server 24.2.96.1315

## - Developer Machines (IP) -
#### Linux OS:
- Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish) 
#### Services with LISTENING PORTS:
| Service      | Port            |
|--------------|-----------------|
| systemd-r    | 53   |
| cupsd        | 631       |
| apache2      | *:80            |
| mysqld       | 33060 & 3306    |

## - Windows workstations: (P) (A) -
#### Windows OS:
Microsoft Windows 11 Home 10.0.22631 22631
- Sales (F) (P)
- Marketing (P)
- Management functions (A)

## - IT & Test System (S) -
#### Kali OS:
Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
