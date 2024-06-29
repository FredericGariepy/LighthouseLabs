# Q1.
Imagine you are a network administrator using an NMS.

You receive an alert that the CPU utilization on a core router has exceeded 80%.

What steps would you take to investigate and resolve this issue before it impacts the network?

Correct Answer
1. Verify the Alert:
   > Check the NMS dashboard to confirm the alert and review the historical CPU utilization data to understand if this is a recurring issue or a sudden spike.
3. Identify the Cause:
   > Determine if there are any recent changes or updates to the network that might have caused the spike, such as new devices, services, or applications added.
5. Analyze Traffic:
   > Use tools like Wireshark or TCPDUMP to analyze network traffic through the router to identify any unusual patterns or excessive traffic that could be contributing to high CPU usage.
7. Check Running Processes:
   > Access the router's management interface to review running processes and their CPU consumption. Identify any processes that are consuming an unusually high amount of resources.
9. Apply Temporary Mitigations:
   > If necessary, apply temporary mitigations such as traffic shaping or rate limiting to reduce the load on the router.
11. Long-Term Solutions:
    > Develop and implement long-term solutions, such as upgrading hardware, optimizing configurations, or redistributing traffic loads to prevent future occurrences.
13. Document the Incident:
    > Document the incident, findings, and steps taken to resolve the issue for future reference and to improve network monitoring processes.

# Q2.
You are using Wireshark to monitor network traffic and notice a sudden spike in CPU usage on a normally idle server.

What steps would you take to investigate whether this spike indicates a potential security threat?

Correct Answer:
- Examine Traffic Patterns:
  > Use Wireshark to analyze incoming and outgoing traffic during the spike period.
  > Look for unusual patterns, high volume of requests, or unexpected ports being used.
- Identify Source and Destination:
  > Filter traffic by the server's IP address to identify the source and destination of the traffic.
  > Determine if the traffic is coming from or going to known and trusted IP addresses.
- Check for Malicious Activity:
  > Look for signs of malicious activity such as repeated login attempts,
  > large data transfers, or unusual protocols being used.
- Review Server Logs:
  > Check the server's logs (e.g., web server logs, system logs)
  > for any suspicious activity or errors that could be related to the spike.
- Isolate the Server:
  > If a security threat is suspected, consider isolating the server from the network
  > to prevent potential spread or data exfiltration.
- Run Security Scans:
  > Perform a security scan on the server to detect any malware, unauthorized access, or vulnerabilities.
- Notify the Security Team:
  > Inform the security team of the findings and collaborate on further investigation and remediation steps.
- Document Findings: Document the incident, including the steps taken and the conclusions drawn, to help prevent future occurrences and improve security protocols.
