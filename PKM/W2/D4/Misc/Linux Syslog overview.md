## Check Here for Overview of [Syslog message](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W1/D4/Syslog_msg.md)

## [Message components](https://en.wikipedia.org/wiki/Syslog)
The information provided by the originator of a syslog message includes the facility code and the severity level. The syslog software adds information to the information header before passing the entry to the syslog receiver. Such components include an originator process ID, a timestamp, and the hostname or IP address of the device.

[table source RDC5424](https://datatracker.ietf.org/doc/html/rfc5424)

[text info source](https://www.paessler.com/it-explained/syslog)

Facility and Severity values are not normative but often used.  They
   are described in the following tables for purely informational
   purposes.  Facility values MUST be in the range of 0 to 23 inclusive.

| Numerical Code | Facility                                   |
|----------------|--------------------------------------------|
| 0              | kernel messages                            |
| 1              | user-level messages                        |
| 2              | mail system                                |
| 3              | system daemons                             |
| 4              | security/authorization messages            |
| 5              | messages generated internally by syslogd   |
| 6              | line printer subsystem                     |
| 7              | network news subsystem                     |
| 8              | UUCP subsystem                             |
| 9              | clock daemon                               |
| 10             | security/authorization messages            |
| 11             | FTP daemon                                 |
| 12             | NTP subsystem                              |
| 13             | log audit                                  |
| 14             | log alert                                  |
| 15             | clock daemon (note 2)                      |
| 16             | local use 0 (local0)                       |
| 17             | local use 1 (local1)                       |
| 18             | local use 2 (local2)                       |
| 19             | local use 3 (local3)                       |
| 20             | local use 4 (local4)                       |
| 21             | local use 5 (local5)                       |
| 22             | local use 6 (local6)                       |
| 23             | local use 7 (local7)                       |

## Syslog Severity Levels
The meaning of severity levels other than Emergency and Debug are relative to the application.

Each message Priority also has a decimal Severity level indicator.
   These are described in the following table along with their numerical
   values.  Severity values MUST be in the range of 0 to 7 inclusive.

| Numerical Code | Severity                               | Description                              |
|----------------|----------------------------------------|------------------------------------------|
| 0              | Emergency                              | System is unusable                       |
| 1              | Alert                                  | Action must be taken immediately         |
| 2              | Critical                               | Critical conditions                      |
| 3              | Error                                  | Error conditions                         |
| 4              | Warning                                | Warning conditions                       |
| 5              | Notice                                 | Normal but significant condition         |
| 6              | Informational                          | Informational messages                   |
| 7              | Debug                                  | Debug-level messages                     |
