Workflow:
1.  [Assets](#assets) ~~List assets, describe OS / software versions~~
2. List labeled assets in descending priority, based on category.
3. Assign CIA value to asset
4. Assign SIL value to asset
5. Add related vulnerabilties (search MITRE, CVE , NVD)
6. Calculate(vuln + asset SIL) to get CVSS Scores

---

1. Assets + OS/Software versions
> Find the OS and Software versions on each VM, make steps replicable.
---
# Assets
- ## Windows Server, runs: (S) (SM)
    - ### Windows OS
      In Powershell:
    
      `Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber`
        ```ps1
        Caption                   Version    BuildNumber
        -------                   -------    -----------
        Microsoft Windows 11 Home 10.0.22631 22631
        ```
    - ### Windows public-facing services  
      List listening ports, In Powershell: `netstat -ano | findstr "LISTENING"`
      
      This will list services with listening ports and their PIDs:
      > 4, 996, 772, 608, 2120, 748
      
      Use those PIDs in the following script:
      
      Powershell script to find version and name of services on open listening ports:
      ```ps1
      # Retrieve process details including service name, file version, and port for specified PIDs
        Get-NetTCPConnection | Where-Object { $_.OwningProcess -in @(4, 996, 772, 608, 2120, 748) } | 
            Group-Object OwningProcess | ForEach-Object {
                $proc = Get-Process -Id $_.Name
                $_.Group | Select-Object -First 1 | Select-Object @{Name="ProcessName";Expression={$proc.ProcessName}},
                                                                 @{Name="FileVersion";Expression={$proc.FileVersionInfo.FileVersion}},
                                                                 LocalPort, State }
      ```
      This will output the following table. Notice NO FileVersion, these are default services.
      ```cmd
        ProcessName FileVersion LocalPort  State
        ----------- ----------- ---------  -----
        services                    49669 Listen
        spoolsv                     49668 Listen
        wininit                     49665 Listen
        lsass                       49664 Listen
        System                        445 Listen
        svchost                       135 Listen
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

- ## Kali:
    - ### Kali OS
      Terminal command: `cat /etc/os-release`
        ```bash
        PRETTY_NAME="Kali GNU/Linux Rolling"
        NAME="Kali GNU/Linux"
        VERSION_ID="2024.2"
        VERSION="2024.2"
        VERSION_CODENAME=kali-rolling
        ID=kali
        ID_LIKE=debian
        HOME_URL="https://www.kali.org/"
        SUPPORT_URL="https://forums.kali.org/"
        BUG_REPORT_URL="https://bugs.kali.org/"
        ANSI_COLOR="1;31"
        ```

  - Find other services UP and LISTENING on open Port(s) [*Workflow*]
    ```bash
    1. 
    └─$ sudo netstat -tuln | grep LISTEN
    tcp        0      0 127.0.0.1:35619         0.0.0.0:*               LISTEN 
    
    2.
    └─$ sudo lsof -i :35619 
    COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
    container 714 root   10u  IPv4   8218      0t0  TCP localhost:35619 (LISTEN)
    
    3.
    └─$ ps -p 714 -o command     
    COMMAND
    /usr/bin/containerd
    
    4.
    └─$ containerd --version
    containerd github.com/containerd/containerd 1.6.24~ds1 1.6.24~ds1-1
    ```
    github : https://github.com/containerd/containerd
    
    -> This seems to be the container on which the Kali Linux OS image is running on.
    > containerd is an industry-standard container runtime with an emphasis on simplicity, robustness, and portability. It is available as a daemon for Linux and Windows, which can manage the complete container lifecycle of its host system: image transfer and storage, container execution and supervision, low-level storage and network attachments, etc.

    - Test systems (S)
    - IT systems (S)
