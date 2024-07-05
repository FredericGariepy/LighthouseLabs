## Check Here for Overview of [Syslog message](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W1/D4/Syslog_msg.md)

## [Message components](https://en.wikipedia.org/wiki/Syslog)
The information provided by the originator of a syslog message includes the facility code and the severity level. The syslog software adds information to the information header before passing the entry to the syslog receiver. Such components include an originator process ID, a timestamp, and the hostname or IP address of the device.

Syslog Facility Codes
| Facility code | Keyword    | Description                               |
|---------------|------------|-------------------------------------------|
| 0             | kern       | Kernel messages                           |
| 1             | user       | User-level messages                       |
| 2             | mail       | Mail system                               |
| 3             | daemon     | System daemons                            |
| 4             | auth       | Security/authentication messages         |
| 5             | syslog     | Messages generated internally by syslogd  |
| 6             | lpr        | Line printer subsystem                    |
| 7             | news       | Network news subsystem                    |
| 8             | uucp       | UUCP subsystem                            |
| 9             | cron       | Cron subsystem                            |
| 10            | authpriv   | Security/authentication messages         |
| 11            | ftp        | FTP daemon                                |
| 12            | ntp        | NTP subsystem                             |
| 13            | security   | Log audit                                 |
| 14            | console    | Log alert                                 |
| 15            | solaris-cron | Scheduling daemon                       |
| 16-23         | local0-7   | Locally used facilities (0-7)             |

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
