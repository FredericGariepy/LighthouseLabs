>[!IMPORTANT]
> In server.py change `path_triage_script`
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
