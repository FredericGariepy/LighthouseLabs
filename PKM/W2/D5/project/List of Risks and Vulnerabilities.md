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
      List listening ports, In Powershell: `netstat -ano | findstr "LISTENING"`
    - In Powershell: `Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber`
        ```ps1
        Caption                   Version    BuildNumber
        -------                   -------    -----------
        Microsoft Windows 11 Home 10.0.22631 22631
        ```

    - ### SQL database (S)
    
    In powershell: `Get-Service -Name *sql*`
  
    Returns nothing, hence the VM does not have an mySQL database installed.
  
    - ### Internet Information Services (IIS) webserver (S)

      In powershell `reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\InetStp" /v VersionString`
      > IIS Version 10.0
    - ### PRTG Network Monitor (SM)

      In powershell `Get-Process PRTG* | Select-Object Name, FileVersion`
      > PRTG Probe 24.2.96.1315
      > PRTG Server 24.2.96.1315

- ## Linux: (IP)
    - ### Linux OS:
      Terminal command: `cat /etc/os-release`
        ```bash
        PRETTY_NAME="Ubuntu 22.04.4 LTS"
        NAME="Ubuntu"
        VERSION_ID="22.04"
        VERSION="22.04.4 LTS (Jammy Jellyfish)"
        VERSION_CODENAME=jammy
        ID=ubuntu
        ID_LIKE=debian
        HOME_URL="https://www.ubuntu.com/"
        SUPPORT_URL="https://help.ubuntu.com/"
        BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
        PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
        UBUNTU_CODENAME=jammy
        ```
        
    - ### Services with LISTENING PORTS,
      In terminal: `sudo lsof -i -P -n | grep LISTEN`

        ```bash
        systemd-r  434 systemd-resolve   14u  IPv4  18091      0t0  TCP 127.0.0.53:53 (LISTEN)
        cupsd      721            root    6u  IPv6  19991      0t0  TCP [::1]:631 (LISTEN)
        cupsd      721            root    7u  IPv4  19992      0t0  TCP 127.0.0.1:631 (LISTEN)
        apache2    726            root    4u  IPv6  21073      0t0  TCP *:80 (LISTEN)
        apache2    728        www-data    4u  IPv6  21073      0t0  TCP *:80 (LISTEN)
        apache2    729        www-data    4u  IPv6  21073      0t0  TCP *:80 (LISTEN)
        mysqld     839           mysql   21u  IPv4  22788      0t0  TCP 127.0.0.1:33060 (LISTEN)
        mysqld     839           mysql   24u  IPv4  22790      0t0  TCP 127.0.0.1:3306 (LISTEN)
        ```

- Windows workstations: (P) (A)
    ### Windows OS
    - List listening ports, In Powershell: `netstat -ano | findstr "LISTENING"`
    - In Powershell: `Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber`
        ```ps1
        Caption                   Version    BuildNumber
        -------                   -------    -----------
        Microsoft Windows 11 Home 10.0.22631 22631
        ```
    In Powershell:
  ```ps1
  netstat -ano | Select-String "LISTENING" | ForEach-Object { $parts = $_ -split '\s+'; if ($parts.Count -gt 1) { $proc = Get-Process -Id $parts[-1]; if ($proc) { "Service Name: $($proc.ProcessName), File Version: $($proc.FileVersionInfo.FileVersion)" } } }
  ```
  
    However, No services besides generic services & afromentioned PRGT is running...
    - Sales (F) (P)
    - Marketing (P)
    - Management functions (A)

- Kali: 
    - Test systems (S)
    - IT systems (S)
