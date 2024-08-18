####  readings
- [x] YO that was cool asf: https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf
- [x] SIEM = ? https://www.crowdstrike.com/cybersecurity-101/security-information-and-event-management-siem/
#### Do
- [x] https://mitre-attack.github.io/attack-navigator/
#### Side
- [ ] https://www.pathfactory.com/ web beacons

# Limitations of a SIEM
- The __SIEM itself does NOT monitor__ events as they happen throughout the enterprise in real time,
  but rather uses log data recorded by other software to determine that an event occurred.
- __SIEMs DON'T replace enterprise security controls__ such as intrusion prevention systems, firewalls or antivirus technologies.
- SIEMs cannot always provide complete __context on _unstructured data___.
> This can lead to false alerts,
>
> and security teams can find it difficult to diagnose and research security events
>
> because of the high volume of alerts and data provided by the SIEM.

- Responses to alerts can be delayed or overlooked because analysts lack an understanding of which alerts need attention.

# SIEM v SIM v SEM
|term|def|
|-|-|
|SIEM |Security information and event management|
|SEM|security events management |
|SIM| security information management |

- __SIM__ focuses on collecting & managing: logs and other security data. + Log retention, analysis, reporting, and correlation with threat intelligence sources.
- __SEM__ is for real-time analysis and reporting. Advanced operations: event aggregation, correlation, and notification triggering for endpoint and network devices like Firewalls, Linux, and Windows servers, etc.

__SIEM__ = set of tools/services that combine __SEM + SIM__.



<img src="https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C9/Cyber+BC+C9.4/CyberBC+09.04.01.01.png" width="400" alt="SIEM v SIM v SEM">




