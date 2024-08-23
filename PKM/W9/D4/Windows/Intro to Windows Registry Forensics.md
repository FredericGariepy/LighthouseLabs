- [x] [Registry Editor: Practical Windows Registry Explanation](https://www.youtube.com/watch?v=tBwAHqqPoQY)
Windows registry forensic investigations requires specialized knowledge, tools, and caution to avoid unintended modifications or damage to the system.

Windows Registry is crucial in tracing the source of a security breach because it contains detailed information about system configurations, installed software, and user activities. 

Use the Registry to identify suspicious modifications, track software installations that might have vulnerabilities, and review recently run programs that could have been executed during the breach


- [x] https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users

# Windows Registry :blue_heart: :window:
The Windows Registry is a database to organize and run Windows. \
It is essential part of the Windows operating system.

- central repository for storing and retrieving a wide range of system and application settings. 

It is maintained in eight (8) main files as follows:
- Five (5) containing __general system and user information__
- Two (2) dedicated to __user profile information__
- One (1) to __record programs that were recently run__.


The Registry contains information that Windows continually references during operation,
such as profiles for each user, the applications installed on the computer and
the types of documents that each can create,
property sheet settings for folders and application icons,
what hardware exists on the system, and the ports that are being used.

# Registry hive :honey_pot: :key:
A __registry hive__ is a group of :
- keys
- subkeys
- values in the registry 
that has a set of supporting files that contain backups of its data (registry data).

The supporting files for all hives are in the `%SystemRoot%\System32\Config` folder.

The supporting files for __`HKEY_CURRENT_USER`__ are in the `%SystemRoot%\Profiles\Username` folder.

|Registry hive|	Supporting files|
|-|-|
|HKEY_LOCAL_MACHINE\SAM| 	Sam, Sam.log, Sam.sav|
|HKEY_LOCAL_MACHINE\Security |	Security, Security.log, Security.sav|
|HKEY_LOCAL_MACHINE\Software |	Software, Software.log, Software.sav|
|HKEY_LOCAL_MACHINE\System 	|System, System.alt, System.log, System.sav|
|HKEY_CURRENT_CONFIG 	|System, System.alt, System.log, System.sav, Ntuser.dat, Ntuser.dat.log|
|HKEY_USERS\DEFAULT 	|Default, Default.log, Default.sav|

### Back up the registry
Before you edit the registry, \
export the keys in the registry that you plan to edit, \
or back up the whole registry.

If a problem occurs, \
you can then follow the steps in the [Restore the registry](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users#restore-the-registry) section to restore the registry to its previous state. \

To back up the whole registry, \
use the Backup utility to back up the system state. 

The system state includes the registry, \
the __COM+ Class Registration Database__, and your __boot files__.

### Edit the registry
To modify registry data, \
a program must use the [__registry functions__](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-functions) that are defined in Registry Functions.

Administrators can modify the registry by using:
- Registry Editor (Regedit.exe or Regedt32.exe)
- Group Policy, System Policy, Registry (.reg) files
- running scripts such as VisualBasic script files.

### Restore the registry
To restore the registry, use the appropriate method.
#### Method 1: Restore the registry keys
To restore registry subkeys that you exported, \
double-click the Registration Entries (.reg) file that you saved in the Export registry subkeys section. 

Or, you can restore the whole registry from a backup.

#### Method 2: Restore the whole registry
To restore the whole registry, \
restore the system state from a backup.
