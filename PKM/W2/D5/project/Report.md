# Cat Scan II Big Dog
# Executive Summary:
> A short, one or two paragraph summary explaining what you have done. Include information about the top five SILs and the sensors and thresholds you are monitoring or recommending.
# Table of Sensors:
> Complete the table as required; give appropriate explanation wherever required.

| Sensor | Description | System | IoCs Associated | Rationale | Priority | Thresholds / Assumptions|
| - | - | - | - | - | - | - |
| HTTP Load Time            | Monitors the time it takes for the page to load. | Linux      | Malicious Redirects, DDoS Attacks, Content Injection | Unexpected changes in load time can indicate anomalies or performance-related issues that could indicate a security breach or compromise. | Medium (SIL of high, see assumptions) | Changes of 20% over the average load. SIL based on the fact that BIG DOG does NOT have a large Web Presence, the Linux web server being internal and outward facing (Assumption). Low impact on CIA (specifically A) but higher chance of compromise. SIL set to high. |
| MySQL Database Query Sensor| Monitors MySQL database query activity.       | Linux      |                                             |                                                                                              |                   |                                                                                                                                                                       |
| SSH Sensor                | Monitors SSH access and usage.                | Linux      |                                             |                                                                                              |                   |                                                                                                                                                                       |
| Antivirus Status Sensor   | Monitors antivirus software status.           | All        |                                             |                                                                                              |                   |                                                                                                                                                                       |
| File Sensor               | Monitors changes to files and directories.    | Linux      |                                             |                                                                                              |                   |                                                                                                                                                                       |
| Windows Event Log Sensor  | Monitors Windows event logs.                  | Windows11  |                                             |                                                                                              |                   |                                                                                                                                                                       |
| Bandwidth Usage Sensor    | Monitors network bandwidth usage.             | All        |                                             |                                                                                              |                   |                                                                                                                                                                       |

# Discussion Section:
> A discussion of each of the connections between the sensors, IoCs and thresholds.
# Recommendation Section:
> A recommendation section where you should recommend how the client might enhance the security of their systems (for example added sensors); you must cite industry best practices as you make your recommendations.
