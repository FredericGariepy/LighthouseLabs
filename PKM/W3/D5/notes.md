Self-questions:

Log rotation, older files get their name incremented. 
- How can access logs increment their files names, whithout changing their associated modfidication dates?

### How to log monitor (linux)?
> Setup a syslog-ng server and setup rsyslogd on your other machines to forward their logs to the syslog-ng server.
>
> You can configure the syslog-ng to create a subfolder for each of the machines that are sending logs based on the remote ip or reverse-dns to organize everything.
>
> Thank you [nikade87](https://www.reddit.com/user/nikade87/) on reddit [covo](https://www.reddit.com/r/selfhosted/comments/1031chv/simple_way_to_centralize_my_server_logs/)

Syslog-ng
- [Configuring syslog-ng on Linux OS](https://www.ibm.com/docs/en/dsm?topic=os-configuring-syslog-ng-linux)
- [Configuring Linux OS to send audit logs](https://www.ibm.com/docs/en/dsm?topic=os-configuring-linux-send-audit-logs)




[Detecting Attacks on Web Applications from Log Files- Roger Meyer](https://sansorg.egnyte.com/dl/jmtbTzYCuX)
> I love you Roger, so clear

| acro | def |
|-|-|
|NIDS|Network-Based Intrusion Detection System|
|IDS|Intrusion detection systems|


Why analyzing log files instead of using a network intrusion detection system?
- HTTPS -> SSL
- No NIDS deployed
- High traffic load makes
- NIDS are designed to work on the TCP/IP level, and thus they may not be as effective on the HTTP layer
- IDS evasion techniques (HTTP, encoding, fragmenting, ...)

