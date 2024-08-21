## Q.1
- After optimizing your Windows event logging based on the article's recommendations, imagine you are tasked with examining logs after a suspected breach. \
 \
What specific types of log entries would you prioritize reviewing and why?


In the scenario of a suspected breach, priority should be given to reviewing log entries that record account logon events, security group changes, and unusual access patterns to sensitive files. \
These types of entries are crucial as they can indicate unauthorized access attempts, changes in permissions, and potential data exfiltration activities. \
Additionally, reviewing Sysmon logs for process creation and network connections can provide insights into malicious processes and external communication attempts by malware.

## Q.2
- Considering the importance of DNS and DHCP logging as discussed, \
  how would you use this logged information to trace the source of a network intrusion?

DNS and DHCP logs are invaluable for tracing network intrusions as they provide details about the devices on the network and their communication patterns. \
By analyzing DHCP logs, you can identify unauthorized devices obtaining IP addresses. \
DNS logs, on the other hand, can reveal queries to malicious domains or unusual amounts of DNS traffic, which are indicators of command and control communications or data exfiltration attempts. \
Correlating this information helps in pinpointing the source and method of intrusion.
