## dependency
`sudo apt install inotify-tools`
## workflow
0. fetch.sh should be changed to read from `tail -f`, if the system is to be synchronous. `cat file.log` is asynchronous in security.
1.  in client.py, use split('\n') on fetch_log.sh, send single log lines as message to server
> although we agree, in the real world, a max byte size with arbitrary message size would be safer
>
> This is only to make current project deliverable in < 48h.
2. in server.py, make a **parse funciton**,  use regex with `?P <key>` ([example](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/regex_dict.py)), to create dictionary log objects
> This will turn received strings into dict-obj={IP:xxx, error_code:xxx, info:xxx, key:value}
>
> Use [resources](#resources) to build appropriate regex for parse 
3.  on serverside, using the log obj. , create a logic/algorithm to monitor for IoC.
> see bellow for logic/algorithm ideas

#### IoC monitoring Ideas:
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

> [!TIP]
> In Client.py **change** `server_addr` to server IP

## resources
[Sample Access logs](https://www.ossec.net/docs/log_samples/apache/apache.html#log-samples-from-apache)

[Apache 2.4 (current) Docs](https://httpd.apache.org/docs/2.4/logs.html)
