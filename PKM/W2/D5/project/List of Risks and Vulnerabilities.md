Workflow:
1. List assets, describe OS / software versions
2. Add related vulnerabilties (search MITRE, CVE , NVD)
3. List labeled assets in descending priority, based on category.
4. Assign CIA value to asset
5. Assign SIL value to asset
6. Calculate(vuln + asset SIL) to get CVSS Scores

Goals:
- Created a list of assets owned by the Big Dog organization and their vulnerabilities.
- Decided on the risk each discovered vulnerability might pose to the Big Dog organization and prioritized them.
- Discussed your findings and decisions in a small group.
- Completed the research for case study Cat Scan II
- Understood the process of discovering asset vulnerabilities and how to rate & prioritize risks


1. Assets + OS/Software versions

# Assets
- ## Windows Server, runs: (S) (SM)
    - ### Windows OS
    - List listening ports, In Powershell: `netstat -ano | findstr "LISTENING"`
    - In Powershell: `Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber`
        ```ps1
        Caption                   Version    BuildNumber
        -------                   -------    -----------
        Microsoft Windows 11 Home 10.0.22631 22631
        ```

    - ### SQL database (S)
    
    In powershell: `Get-Service -Name *sql*` Returns nothing, hence the VM does not have an mySQL database installed.
    - ### Internet Information Services (IIS) webserver (S)

      In powershell `reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\InetStp" /v VersionString`
      > IIS Version 10.0
    - ### PRTG Network Monitor (SM)

      In powershell `Get-Process PRTG* | Select-Object Name, FileVersion`
      > PRTG Probe 24.2.96.1315
      > PRTG Server 24.2.96.1315

- Linux: (IP)
    - Used by developers to create important proprietary intellectual property (IP) for the company

- Windows workstations: (P) (A)
    - Sales (F) (P)
    - Marketing (P)
    - Management functions (A)

- Kali: 
    - Test systems (S)
    - IT systems (S)
