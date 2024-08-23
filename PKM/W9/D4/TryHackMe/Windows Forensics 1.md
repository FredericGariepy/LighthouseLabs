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

# Data Acquisition | KAPE
Good practice in forensics, use a copy of live system or image taken of the system.

KAPE: Kroll Artifact Parser and Extractor by  Eric Zimmerman

 



















