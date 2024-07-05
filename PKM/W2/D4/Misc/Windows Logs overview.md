# Windows
The [Elements of a Windows Event Log](https://www.solarwinds.com/resources/it-glossary/windows-event-log)
- **Log name**: Name of the event log to which events from different logging components will be written. Events are commonly logged for system, security, and applications.
- **Event date/time**: Includes the date and time when the event occurred.
- **Task category**: Identifies the type of recorded event log. Application developers can also define task categories to serve as extra information about the event.
- **Event ID**: This Windows identification number helps network administrators uniquely identify a specific logged event.
- **Source**: Name of the program or software causing the event log.
- **Level**: Event level represents the severity of the recorded event log. These include information, error, verbose, warning, and critical.
- **User**: Name of the user who logged onto the Windows computer when the event occurred.
- **Computer**: Name of the computer logging the event.


What Types of Information Are Stored in Windows Event Log?
Windows event logs store information about different events that occur within the system. The type of information stored varies based on the category of an event log. Data is recorded commonly for four Windows event log types:

system
application
setup
security
Windows system event log includes information about incidents related to the Windows operating system. Similarly, the application event log provides some information about errors occurring within the installed software on the machine. The security event log contains data about security events on the system, while the setup log focuses more on installation-related events. The information stored in event logs allows system administrators to investigate different problems and diagnose them accordingly.

Common Event Log Categories and Types
Event logs are classified into four categories such as application, security, setup, and system. There's also a special category of event logs called forwarded events.

System Log: Windows system event log contains events related to the system and its components. Failure to load the boot-start driver is an example of a system-level event.
Application Log: Events related to a software or an application hosted on a Windows computer get logged under the application event log. For example, the problem in starting Microsoft PowerPoint comes under the Application log.
Security: Security logs contain events related to the safety of the system. The event gets recorded via the Windows auditing process. Examples include failed and valid logins, file deletions, etc.
Setup: The setup log contains events that occur during the installation of the Windows operating system. On domain controllers, this log will also record events related to Active Directory.

Forwarded Events: Contains event logs forwarded from other computers in the same network.

Windows events are further divided into five different types:

Information: Indicates an application or service is operating well. For example, when Windows loads the network driver, the incident will be logged as an information event.
Warning: Unimportant events hinting toward potential issues in the future. A warning event will get logged for a problem like low disk space.
Error: Describes a significant issue when a system cannot function normally—for example, the operating system stops responding.
Success Audit: Records valid attempt of audited security access for security log. For example, a login attempt that goes well will come under a success audit event.
Failure Audit: Indicates the failure of audited security access under the security log, such as the inability to access the network drive.
Windows Event Severity Levels
Windows event levels indicate the severity or importance of the recorded event. These are categorized as follows:

Information: Indicates the event occurred without issues. Most logs contain information events.
Verbose: Indicates progress or success messages for a particular event.
Warning: Highlights a potential problem system administrators should monitor.
Error: Describes issues in the system or service that don't require immediate troubleshooting.
Critical: Indicates a significant issue in an application or a system needing urgent attention.
How to Check and View Windows Event Logs
Windows event log location is C:\WINDOWS\system32\config\ folder. Event logs can be checked with the help of 'Event Viewer' to keep track of issues in the system. Here's how:

Press the Windows key + R on your keyboard to open the run window
In the run dialog box, type in eventvwr and click OK
In the Event Viewer window, expand the Windows Logs menu
Under the Windows Logs menu, you'll notice different categories of event logs—application, security, setup, system, and forwarded events
Click on one of the event logs to check and view the events recorded under it
