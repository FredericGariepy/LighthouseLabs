- [ ] https://tryhackme.com/r/room/windowsforensics1

# Windows Registry and Forensics
'artifact' = activity left on the computer system

`⊞ + R` to _open_ `regedit.exe` Windows utility to view and edit the registry

The Windows Registry is a collection of databases that contains the system's configuration data. 

Windows registry consists of Keys and Values 

A [Registry Hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives#:~:text=Registry%20Hives.%20A%20hive%20is%20a%20logical%20group,with%20a%20separate%20file%20for%20the%20user%20profile.) is a group of Keys, subkeys, and values stored in a single file on the disk.

The registry on any Windows system contains the following five (5) root keys:
- HKEY_CURRENT_USER
- HKEY_USERS
- HKEY_LOCAL_MACHINE
- HKEY_CLASSES_ROOT
- HKEY_CURRENT_CONFIG

| Folder/predefined key | Desc. |
|-|-|
|HKEY_CURRENT_USER| root config current user. HKCU|
|HKEY_USERS| all actively loaded user profiles. subkey of HKCU. HKU.|
|HKEY_LOCAL_MACHINE| config  info of machine. HKLM. |
| HKEY_CURRENT_CONFIG | info on hardware profile for local machine @ startup |
| HKEY_CLASSES_ROOT | HKCR. subkey of `HKEY_LOCAL_MACHINE\Software`.  Correct program for file in Windows Explorer.  From Win2000 HKCR info stored in _both_ HKLM & HKCU. `HKEY_LOCAL_MACHINE\Software\Classes` key has default settings that can apply to all users on Local machine. `HKEY_CURRENT_USER\Software\Classes` key settings to override default, applies to _only_ interactive user. Writting kets to HKCR, system will store info to `HKLM\Software\Classes`. If write key to HKCR, and key exists in `HKCU\soft..\class`, it goes to `HKLM\Soft..\Class`.  |

- live system = access the registry using `regedit.exe`
- disk image  = hives are on `C:\Windows\System32\Config`

# __C:\Windows\System32\Config__:
1. DEFAULT (mounted on _HKEY_USERS_\DEFAULT)

2. SAM (mounted on HKEY_LOCAL_MACHINE\SAM) #Security Accounts Manager
3. SECURITY (mounted on HKEY_LOCAL_MACHINE\Security)
4. SOFTWARE (mounted on HKEY_LOCAL_MACHINE\Software)
5. SYSTEM (mounted on HKEY_LOCAL_MACHINE\System)

# `C:\Users\<username>\`
(2) two Hives containing user information in `C:\Users\<username>\`:
1. NTUSER.DAT (mounted on HKEY_CURRENT_USER when a user logs in)
2. USRCLASS.DAT (mounted on HKEY_CURRENT_USER\Software\CLASSES)

> NTUSER.DAT and USRCLASS.DAT are hidden files

__NTUSER.DAT hive__ is located in the directory `C:\Users\<username>\` \
__USRCLASS.DAT hive__ is located in the directory `C:\Users\<username>\AppData\Local\Microsoft\Windows`

# `C:\Windows\AppCompat\Programs\Amcache.hve`
Accessing registry hives offline
#### The Amcache Hive
Windows creates this hive to save information on programs that were recently run on the system. 
_AmCache_ is located in the directory `C \Windows\AppCompat\Programs\Amcache.hve` \

# Transaction Logs & Backups:
Accessing registry hives offline
## transaction logs
- The __transaction logs__ can be considered as the __journal of the changelog of the registry hive__
- __transaction logs__ can often have the latest changes in the registry that _haven't made their way to the registry hives themselves_ .
- The transaction log for each hive is __stored as a .LOG file__ in the same directory as the hive itself.
- It has the _same name as the registry hive_, but the extension is .LOG

e.g. the transaction log for the SAM hive will be located in `C:\Windows\System32\Config` in the filename SAM.LOG. Sometimes there can be multiple transaction logs as well. In that case, they will have .LOG1, .LOG2 etc.,

## Registry backups _are the opposite of_ Transaction logs
- backups of the registry hives are located in the `C:\Windows\System32\Config`
- These hives are copied to the C:\Windows\System32\Config\RegBack directory _every (10) ten days_.
> It might be an excellent place to look if you suspect that some registry keys might have been deleted/modified recently.

# Data Acquisition (extract Registry Hive)
## KAPE | Autopsy | FTK Imager
Good practice in forensics, use a copy of live system or image taken of the system.

- KAPE: Kroll Artifact Parser and Extractor by  Eric Zimmerman \
https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape

KAPE is a live data acquisition and analysis tool which can be used to acquire registry data.

- Autopsy: gives you the option to acquire data from both live systems or from a disk image. \
https://www.autopsy.com/

- FTK Imager: allows you to extract files from a disk image or a live system by mounting the said disk image or drive in FTK Imager \
https://www.exterro.com/ftk-imager

# Explore Windows Registry
## Registry Viewer | Registry Explorer | RegRipper 
0. Once we have extracted the registry hives
1. View these files as we would in the registry editor.
> Since the registry editor only works with live systems and can't load exported hives, we can use the following tools..

- Registry Viewer
> [!NOTE]
> Only loads one hive at a time, and it can't take the transaction logs into account.

- Zimmerman's Registry Explorer \
EZ tools https://ericzimmerman.github.io/#!index.md for Digital Forensics and Incident Response.
>  It can load multiple hives simultaneously and add data from transaction logs into the hive to make a more 'cleaner' hive with more up-to-date data
>
> It also has a handy 'Bookmarks' option containing forensically important registry keys often sought by forensics investigators.

- RegRipper https://github.com/keydet89/RegRipper3.0
Utility that takes a registry hive as input and outputs a report that extracts data from some of the forensically important keys and values in that hive.

> [!NOTE]
> RegRipper does not take the transaction logs into account
> 
> Use Registry Explorer to merge transaction logs with the respective registry hives before sending the output to RegRipper for a more accurate result.

# System Information and System Accounts
## Os Version
0. first step is to find out about the system information (machine's System and Account information)
1. determine the OS version from which this data was pulled through the registry

To find the OS version, we can use the following registry key:
`SOFTWARE\Microsoft\Windows NT\CurrentVersion`
> Has a lot of info about the Machine

## Current control set
__Control Sets__ = hives containing the machine’s configuration data for controlling system startup.

Commonly, we will see 92) two Control Sets, \
ControlSet001 and ControlSet002, in the SYSTEM hive on a machine.

- __ControlSet001__ will point to : the Control Set that the machine booted with \
in `SYSTEM\ControlSet001`

- __ControlSet002__ will be : the __last known good__ configuration \
in`SYSTEM\ControlSet002`

most accurate system information: \
Windows creates a volatile Control Set when the machine is live, \
called the CurrentControlSet : `HKLM\SYSTEM\CurrentControlSet`

Control Set used as the CurrentControlSet is in `SYSTEM\Select\Current`

__last known good__ configuration is in `SYSTEM\Select\LastKnownGood`

> many forensic artifacts we collect will be collected from the Control Sets.

## Computer Name
_Computer Name_ is in `SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName`

## Time Zone Information
Timezone info is in `SYSTEM\CurrentControlSet\Control\TimeZoneInformation`
> timestamp can be in UTC/GMT and others in the local time zone
>
> Knowledge of the local time zone helps in establishing a timeline when merging data from all the sources.

## Network Interfaces and Past Networks

list of network interfaces : `SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces` \
- Each Interface is represented with a unique identifier (GUID) subkey. (interface’s TCP/IP configuration)
- IP addresses, DHCP IP address and Subnet Mask, DNS Servers, and more.

__Past networks__ a given machine was connected to can be found in the following locations: \
- `SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged`
- `SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed`
> These registry keys contain past networks as well as the last time they were connected. The last write time of the registry key points to the last time these networks were connected.

## Autostart Programs (Autoruns)
These registry keys include information about __programs or commands that run when a user logs on__:
- `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Run`
- `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\RunOnce`
- `SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce`
- `SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer\Run`
- `SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

This registry key contains __information about services__:
- `SYSTEM\CurrentControlSet\Services`
If start key is set to 0x02 (2), this means that this service will start at boot.

## SAM hive and user information
The Security Accounts Manager (SAM) is a database file in the Microsoft Windows OS that contains usernames and passwords. \
The SAM hive contains __user account information, login information, and group information__.

`SAM\Domains\Account\Users`
> relative identifier (RID) of the user, number of times the user logged in, last login time, last failed login, last password change, password expiry, password policy and password hint, and any groups that the user is a part o

# Usage or knowledge of files/folders
## Recent Files
Windows maintains a list of recently opened files for each user. \
This information is stored in the NTUSER hive in: \
`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

> Recent documents tab arranges the Most Recently Used (MRU) file at the top of the list.

... continue here 




