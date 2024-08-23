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
Starting from Office 365, Microsoft now ties the location to the user's live ID. \
`NTUSER.DAT\Software\Microsoft\Office\VERSION\UserMRU\LiveID_####\FileMRU`














