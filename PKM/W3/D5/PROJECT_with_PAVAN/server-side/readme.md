### CRON
```bash
@reboot /Your/path/to/server.py &
```
think `2>> cron_error.txt` instead
~~Optional
/dev/null 2>&1
 to run in silence, standard out and standard error to /dev/null~~
```
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

#### IoC monitoring Ideas:
> Use [resources](#resources) to build appropriate regex for parse 
- in server.py, make a **parse funciton**,  use regex with `?P <key>` ([example](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/regex_dict.py)), to create dictionary log objects
> Parse function will *triage* the logs and store them appropriately

> Parse function *could* contribute to updating a baseline
 
> pase function *could* trigger a threshold event based on a global variable.
 
> pase function *could* trigger a threshold event based on, the line count of a file - in  which it stores certain triaged logs.
> e.g.
> > parser: received data, triage, store the 'dangerous logs' in a *dangerous-logs-file.txt*
> >
> > logic :
> > 1. check *dangerous-logs-file.txt* for the number of new logs in the past ~1h
> > 2. threshold condition, if 'log rate' for *dangerous-logs-file.txt* is too high, then do security related event
> >


## resources
[Sample Access logs](https://www.ossec.net/docs/log_samples/apache/apache.html#log-samples-from-apache)

[Apache 2.4 (current) Docs](https://httpd.apache.org/docs/2.4/logs.html)
