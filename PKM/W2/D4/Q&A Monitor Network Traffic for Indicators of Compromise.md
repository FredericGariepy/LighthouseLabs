# Question
Imagine you are monitoring network traffic and notice a sudden spike in bandwidth utilization. What steps would you take to determine if this is an Indicator of Compromise (IoC)?

# Correct Answer
To determine if the sudden spike in bandwidth utilization is an IoC, follow these steps:

1. Check the Network Baseline: Compare the current bandwidth usage against the established network baseline to confirm the anomaly.
> Put into context: Events, special events
2. Identify the Source: Use network monitoring tools to identify which device or application is causing the spike.
> SRC / DST 
3. Analyze Traffic: Inspect the type of traffic (e.g., HTTP, FTP) and look for any unusual patterns or destinations.
> Protocols
4. Check for Known Threats: Cross-reference the traffic patterns with known IoCs or threat intelligence databases.
> Known bad IPs

Real-world example:

If a sudden spike in bandwidth is traced back to a specific server,
and analysis reveals it is communicating with a known malicious IP address,
this could indicate a data exfiltration attempt.
Immediate isolation of the server and a thorough forensic investigation would be necessary.
