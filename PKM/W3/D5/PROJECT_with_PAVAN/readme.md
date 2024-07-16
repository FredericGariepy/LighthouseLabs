> [!IMPORTANT]
> Dependency `sudo apt install inotify-tools`

Here is the project folder structure 
```bash
┌──(fred㉿machine)-[~/Project_Folder]
└─$ tree        
.
├── log_monitor_messages
│   └── log_monitor_messages.txt
├── log_storage
│   ├── access_logs
│   │   ├── standard_access.log
│   │   └── urgent_access.log
│   ├── error_logs
│   │   ├── standard_error.log
│   │   └── urgent_error.log
│   └── unknown_logs
│       └── standard_unknown.log
└── python_scripts
    ├── log_monitor_script
    │   └── access_log_monitor.py
    └── server_client
        ├── server.py
        └── triage.py
```
