## Reads/resources
- [ ] [WINDOWS SYSMON LOGGING CHEAT SHEET ](https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/5eb3687f39d69d48c403a42a/1588816000014/Windows+Sysmon+Logging+Cheat+Sheet_Jan_2020.pdf)
- [ ] [WINDOWS LOGGING CHEAT SHEET](https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/5c586681f4e1fced3ce1308b/1549297281905/Windows+Logging+Cheat+Sheet_ver_Feb_2019.pdf)
- [x] [How to optimize Windows event logging to better investigate attacks](https://www.csoonline.com/article/569759/how-to-optimize-windows-event-logging-to-better-investigate-attacks.html)
- [x] Video [How to tweak Windows logs to better investigate attacks ](https://www.youtube.com/watch?v=i3HShJqLpE8)
## Do
- [ ] [Sysmon v15.15](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
> System Monitor (Sysmon) is a Windows system service and device driver that, once installed on a system, remains resident across system reboots to monitor and log system activity to the Windows event log.

# How to optimize Windows event logging to better investigate attacks

Prepare for better data availability, integrity, improved visibility and saving critical time in the event of conducting a forensic investigation.

__What kind of information does Sysmon provide that is crucial for investigating attacks?__ \
With Sysmon, you can detect malicious activity by tracking code behavior and network traffic, as well as create detections based on the malicious activity

__Why is it recommended that you enable Other Object Access Events to review malicious activity?__ \
Audit Other Object Access Events allows you to monitor operations with scheduled tasks, COM+ objects and indirect object access requests. Event volume: Low. Computer Type - [Microsoft](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-other-object-access-events)

__Why is it recommended to to log both DNS and DHCP events?__ \
Logging DNS and DHCP events with a focus on detailed packet information provides a comprehensive view of network activities, which is essential for effective network security monitoring. It helps in detecting anomalies, troubleshooting issues, investigating incidents, and maintaining overall network health. By capturing outgoing and incoming traffic, UDP and TCP packets, request and response types, and both queries/transfers and updates, you ensure a thorough approach to monitoring and analysis

### Install Sysmon on outward-facing machine
### Increase the log size with 200 gigs of hard drive space.
### Log DNS and DHCP events:
    - Log packets for debugging
    - Outgoing and incoming
    - UDP and TCP
    - Packet type request and response
    - Queries/transfers and updates

## Set audit policies
