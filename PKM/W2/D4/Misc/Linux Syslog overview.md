## Check Here for Overview of [Syslog message](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W1/D4/Syslog_msg.md)

## [Message components](https://en.wikipedia.org/wiki/Syslog)
The information provided by the originator of a syslog message includes the facility code and the severity level. The syslog software adds information to the information header before passing the entry to the syslog receiver. Such components include an originator process ID, a timestamp, and the hostname or IP address of the device.

[table source RDC5424](https://datatracker.ietf.org/doc/html/rfc5424)

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
| Value | Severity    | Keyword   | Deprecated keywords | Description                                          | Condition                                           |
|-------|-------------|-----------|---------------------|------------------------------------------------------|-----------------------------------------------------|
| 0     | Emergency   | emerg     | panic               | System is unusable                                   | A panic condition.                                  |
| 1     | Alert       | alert     |                     | Action must be taken immediately                     | A condition that should be corrected immediately, such as a corrupted system database. |
| 2     | Critical    | crit      |                     | Critical conditions                                  | Hard device errors.                                 |
| 3     | Error       | err       | error               | Error conditions                                     |                                                     |
| 4     | Warning     | warning   | warn                | Warning conditions                                   |                                                     |
| 5     | Notice      | notice    |                     | Normal but significant conditions                    | Conditions that are not error conditions, but that may require special handling. |
| 6     | Informational | info   |                     | Informational messages                               | Confirmation that the program is working as expected. |
| 7     | Debug       | debug     |                     | Debug-level messages                                 | Messages that contain information normally of use only when debugging a program. |
