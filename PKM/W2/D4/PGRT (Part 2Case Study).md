Made *with* AI (ChatGpt 3.5)
<!-- Hey fancy seeing you here -->
###### Heya LHL cohort👋 right here is the response:
➡️ [Click here: Jump to task response](#response) ⬅️
🐜
## task overview
Report Template
| Device | Sensor | Threshold | IoC |
| - | - | - | - | 
|Linux | MySQL | sends query to database server and documents response time	Upper limit, checks for long execution times | Can be used to determine if service is suffering from a higher than normal load

Create a report that organizes and presents the information above. Include the table of details on each sensor with thresholds you have chosen and why, the alert thresholds you recommend, and what IoC it is appropriate to monitor for. You will also fully document, with descriptions and screen captures, how to add a sensor and alert thresholds to PRTG.

Your report should have at least the following components:
-Title: Sensors, Alert Thresholds, and IoCs
- Executive Summary: A short summary explaining what you have done, and the top sensors and IoCs on each machine that you are monitoring for. (Choose those that you feel will give the most relevant information.)
- Process Walkthrough: Walkthrough of the process you used to set up and configure one of the sensors you are recommending in your table. Include detailed descriptions of each step and decision with reasonings and screen captures.
- Table: A table of Devices, Sensors, Thresholds (upper, lower, both as appropriate) and finally a corresponding IoC, Attack or Condition that the sensor might help detect or remediate.
___
## response
## Presentation & Feedback Discussion
# Sensors, Alert Thresholds, and IoCs
# Executive Summary
To effectively detect IoCs, it's crucial to establish baseline behavior.
Sensors monitor device health overtime and create a baseline of our network enviroment.
PRTG is a sophisticated network monitoring tool which uses sensors on netowrk devices to establish a baseline and monitor our enviroment's health.
Bellow are the walkthough of configuring sensors, and what they do.

# Process Walkthrough
*Let's be honest, this is the best tutorial:*

Use auto-detection in PGRT, or,
- [add_a_device manual](https://www.paessler.com/manuals/prtg/add_a_device)
- [add_a_sensor manual](https://www.paessler.com/manuals/prtg/add_a_sensor)

# Table overview
| Device | Sensor | Threshold | Description | IoC |
| ------ | ------ | --------- | ----------- | --- |
| Linux  | HTTP   | Upper limit, checks for long execution times | Monitors a web server using HTTP. Shows if a website or a specific website element is reachable. |  Unusually long HTTP response times, indicating potential server-side issues or slow-downs that may be indicative of a denial-of-service (DoS) attack, resource exhaustion, or inefficiencies in web application processing.|
| Linux  | PING   | Upper Error Limit (msec) 4000 / Upper Warning Limit (msec) 3500 | Monitors connectivity using ping. Shows if a device is reachable through the network using ping requests. | ping sensors alone might not detect sophisticated IoCs. 1. Network Reachability: Ping sensors can detect whether a host is reachable or not. Sudden unavailability of a host that was previously reachable might indicate a potential compromise or outage. 2. Latency Changes: An increase in latency for ping responses could indicate network congestion or abnormal behavior that might be caused by an IoC. |
