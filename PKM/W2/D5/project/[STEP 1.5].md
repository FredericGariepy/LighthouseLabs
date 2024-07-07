Workflow:
1. [Assets](#assets)~~List assets, describe OS / software versions~~
2. List labeled assets in descending priority, based on category.
3. Assign CIA value to asset
4. Assign SIL value to asset
5. Add related vulnerabilties (search MITRE, CVE , NVD)
6. Calculate(vuln + asset SIL) to get CVSS Scores
___

2 List labeled assets in descending priority, based on category.

1. Privacy (P)
2. Proprietary (IP)
3. Admin (A)
4. Financial/accounting (F)
5. Security Management (SM)
6. Systems (S)

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
| systemd-r    | 127.0.0.53:53   |
| cupsd        | [::1]:631       |
| cupsd        | 127.0.0.1:631   |
| apache2      | *:80            |
| apache2      | *:80            |
| apache2      | *:80            |
| mysqld       | 127.0.0.1:33060 |
| mysqld       | 127.0.0.1:3306  |

## - Windows workstations: (P) (A) -
#### Windows OS:
Microsoft Windows 11 Home 10.0.22631 22631
- Sales (F) (P)
- Marketing (P)
- Management functions (A)

## - IT & Test System (S) -
#### Kali OS:
Kali GNU/Linux (debian) version 2024.2 (kali-rolling)
