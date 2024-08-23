# Usage or knowledge of files/folders
## Recent Files
Windows maintains a list of recently opened files for each user. \
This information is stored in the NTUSER hive in: \
`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`
> Recent documents tab arranges the Most Recently Used (MRU) file at the top of the list.

IF you are looking for a __file type__ most recently used, \
e.g.  `.pdf`, `.jpg`, `.docx` \
Go to `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.pdf`

## Office Recent Files

Microsoft Office also maintains a list of recently opened documents \

##### OLD 
`NTUSER.DAT\Software\Microsoft\Office\VERSION` \
e.g. For Windows 15.0 Office 2013 \
`NTUSER.DAT\Software\Microsoft\Office\15.0\Word`
##### NEW
Starting from Office 365, Microsoft now ties the location to the user's [live ID](https://www.microsoft.com/en-us/security/blog/2008/05/07/what-is-a-windows-live-id/). \
`NTUSER.DAT\Software\Microsoft\Office\VERSION\UserMRU\LiveID_####\FileMRU`

## ShellBags | EZ tools ShellBag Explorer
User opens layout \
`USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\Bags` \
`USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\BagMRU` \
`NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU` \
`NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags`

## Open/Save and LastVisited Dialog MRUs
find out recently used files
recently used files
`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths` \
`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`

## Windows Explorer Address/Search Bars
User Recent activityof path typed in the Windows Explorer address bar or searches performed using the following registry keys. \
`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths` \
`NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`

# Evidence of Execution
## UserAssist
Track of applications launched by the user using Windows Explorer. \
However, programs that were run using the command line can't be found in the User Assist keys.

`NTUSER.DAT\Software\Microsoft\Windows\Currentversion\Explorer\UserAssist\{GUID}\Count`

## ShimCache | AppCompatCache Parser
ShimCache is a mechanism used to keep track of application compatibility with the OS and tracks all applications launched on the machine. \
-  ensure backward compatibility of applications.

`SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache`

ShimCache stores file name, file size, and last modified time of the executables.

> [!NOTE]
> Registry Explorer, doesn't parse ShimCache data in a human-readable format.

#### AppCompatCache Parser
`AppCompatCacheParser.exe --csv <path to save output> -f <path to SYSTEM hive for data parsing> -c <control set to parse>`

EZ Tools' Application Compatibility Cache (AppCompatCache)
-  input = SYSTEM give, outputs a CSV file.
## AmCache













