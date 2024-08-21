## Reads/resources
- [ ] [WINDOWS SYSMON LOGGING CHEAT SHEET ](https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/5eb3687f39d69d48c403a42a/1588816000014/Windows+Sysmon+Logging+Cheat+Sheet_Jan_2020.pdf)
- [ ] [How to optimize Windows event logging to better investigate attacks](https://www.csoonline.com/article/569759/how-to-optimize-windows-event-logging-to-better-investigate-attacks.html)
- [x] Video [How to tweak Windows logs to better investigate attacks ](https://www.youtube.com/watch?v=i3HShJqLpE8)
## Do
- [ ] [Sysmon v15.15](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [ ] WINDOWS LOGGING CHEAT SHEET
> System Monitor (Sysmon) is a Windows system service and device driver that, once installed on a system, remains resident across system reboots to monitor and log system activity to the Windows event log.

# How to optimize Windows event logging to better investigate attacks

Prepare for better data availability, integrity, improved visibility and saving critical time in the event of conducting a forensic investigation.

__What kind of information does Sysmon provide that is crucial for investigating attacks?__ \
With Sysmon, you can detect malicious activity by tracking code behavior and network traffic, as well as create detections based on the malicious activity


### Install Sysmon on outward-facing machine
### Increase the log size with 200 gigs of hard drive space.
### Log DNS and DHCP events:
    - Log packets for debugging
    - Outgoing and incoming
    - UDP and TCP
    - Packet type request and response
    - Queries/transfers and updates

## Set audit policies
