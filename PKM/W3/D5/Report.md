# Log Monitoring Workflow
07.17.2024
##  Table of Contents
1. [Executive Summary](#executive-summary)
2. [Solution Section](#solutions-section-scripts--how-they-work)
3. [Iterations](#iterations)
4. [Conclusion](#conclusion)
5. [References](#references)

## Executive Summary
This is a log monitor which works on the Linux operating system. It helps keeps track of the activity on a website through the use of logs.

Log activity that is flagged as an indicator of compromsise results in a security notification.

Notifications are important in mainting good security posture and gives visibility on what's happening to your assets.

Building a Log monitoring solution is a very demanding endevour, many iterations will be required to acheive a full-bodied solution.
Consult the recommendations found at the conclusion section and learn how adopting a SIEM may help your organization.

## Solutions Section (scripts & how they work)
Please [watch the video demo](https://youtu.be/FeMmxXmpgfs) of this log monitoring project.

![log_monitor_solution](https://github.com/user-attachments/assets/f2e57d84-25b8-4fa7-b943-30b3e777df1d)
###### Above, log monitor workflow image.

### [Project files](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN)
Step-by-step explanation of the project files:

The log monitor consists of two parts: a [server-side](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side) and a [client-side](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side).

The client-side contains two bash files, one that will [fetch_access_logs](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_access_logs.sh) and another that will [fetch_error_logs](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_error_logs.sh).

Those two bash files are set as [cron jobs](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/readme.md) to start at reboot.
Both scripts use [inotifywait](https://linux.die.net/man/1/inotifywait) to monitor for access.log and error.log changes (modification and creation in the case of log rotation) inside the /var/log/apache2/ directory.

When the inotifywait events are triggered (new logs are generated), both scripts are made to call on [client.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/client.py) with the new log as a passed argument.

The client script then sends logs to the log monitor server via a socket (Lighthouse Labs, n.d.-a).

Now, on the server side, [server.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/server.py) is up and running through it's [cron](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/readme.md).
The server starts up the [access_log_monitor.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/log_monitor/access_log_monitor.py) as a seperate process and then server.py listens for log lines which were sent by the client.

When the server.py script receives a log, it starts a thread [triage.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/triage.py) and passes it the log. Having triage as a thread allows the server to continue receiving logs without blocking.

The triage script's role is to parse, analyze and *write* the log it received into the approriate directory/file.

To parse, the log is captured by regex expressions and made into a dicitonary object(Lighthouse Labs, n.d.-b).
At this point, the parts of the log can easily be manipulated to test for values, or pushed through an algorithm.
In this log monitoring project, error and access logs are simply checked for their values, i.e. triaged based on loglevel or http status code.
Based on the triage, the logs are ultimately written to endpoints. They are logged according to their security standing (urgent or standard).

Lastly, a log monitorting script, such as [access_log_monitor.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/log_monitor/access_log_monitor.py) which was spawned from [server.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/server.py) runs periodically every minute. It's purpose is to create secuity messages when certain thresholds are met.

In access_log_monitor.py for example, a message is issued when 5+ new logs are written to urgent_access.log in under one minute.
These security messages are appended to an output file (log_monitor_messages.txt).
The format of these messages includes: the indicent time, indicent message and log location that triggered the message.
The securitfy messages in turn, can then be used by other scripts or feed into applications that help notify the organization of potential IoCs.

## Iterations
Fankly, there is *a lot* of potential improvements for this log monitoring solution.

Here are *some* of the major improvements which should be applied on interation:
- **Encryption**: Log lines sent from [client.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/client.py) to [server.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/server.py) should be encrypted as they send out and received in order to proctect against [Network Sniffing](https://attack.mitre.org/techniques/T1040/)(MITRE, n.d.-a).
- **Sanitization**: Log lines received by the log monitor server should sanitized in order to protect against [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)(MITRE, n.d.-b).
- **Code structure**: The [triage.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/triage.py) file should be improved by addoptiong the [strategy design pattern](https://refactoring.guru/design-patterns/strategy)(Refactoring Guru, n.d.). As more Rules/Algortihms (filters) are developed for triage, these encpasulated filters are then applied appropriately to logs, as opposed to the current script, where developed filters are added to a growing chain of conditions that a log passes through. 
- **Code permissions**: On the client side, in both [fetch_access_logs.sh](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/) and [fetch_error_logs.sh](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_error_logs.sh), the script interacts directly with log files found in /var/log/apache2/. The scripts start in the root user's cron job, as sudo priviledges are required to access the directory. Scripts with such access run a security risk and should instead be run with the principle of [least privilege](https://csrc.nist.gov/glossary/term/least_privilege)(NIST, n.d.).
- **Improved monitorig**: The log monitor should further have scripts which monitor for diffrent log baselines and corelations of log events. More rules and/or algorithms should be developed and implemented to better analyze/correlate logs, in order to categorize/report their security standing accurately.
- **Improved log storage**: The storage method should employ a more robust solution such as a database. This will enable using queries to monitor log activity, and unlock a lot of potential for analysis.
- **Support of Windows**: This project does **not** provide a log monitoring solution for the Windows operating system and new code will required to do so.
- **Notificaiton system**: This project produces simple security messages based on log analysis. However, intergration of notication systems (emails, SMS, 3rd party alerts) should be implemented to consume the security messages generated, so as to offer better alerts.
# Conclusion
Building a log monitoring solution is a very demanding endavour.

This project delivers a rudimentary [working system](https://www.youtube.com/watch?v=FeMmxXmpgfs&feature=youtu.be) for log monitoring on Linux operating systems.
The organization would greatly benefit from adopting the use of a security information and event management [(SIEM)](https://www.microsoft.com/en-ca/security/business/security-101/what-is-siem) system (Microsoft, n.d.). Such systems can monitor the organizations's assets (both Linux and Windows machines) and send security notifications.

SIEMs are [not only great tools for log management](https://www.crowdstrike.com/cybersecurity-101/observability/siem-vs-log-management/) (CrowdStrike, n.d.) but also provide incident monitoring and response as well as log analysis/corellations to detect and respond to potential threats. All functions which fit the organization's needs and offer great return on investment.

There are many SIEMs available on the market. [Splunk](https://www.splunk.com/) is a SIEM which offers a *free tier* that your organization can test out (Splunk, n.d.-a). Feel free to further contact me in order to implement Splunk as solution to your security needs. There is additonally great [official documentation](https://docs.splunk.com/Documentation) to assist your implementation (Splunk, n.d.-b).

# References
MITRE. (n.d.-a). Network sniffing. MITRE ATT&CK. Retrieved July 17, 2024, from https://attack.mitre.org/techniques/T1040/

MITRE. (n.d.-b). Exploitation of remote services. MITRE ATT&CK. Retrieved July 17, 2024, from https://attack.mitre.org/techniques/T1210/

National Institute of Standards and Technology. (n.d.). Information Technology Laboratory Computer Security Resource Center. Glossary - Least privilege. Retrieved July 17, 2024, from https://csrc.nist.gov/glossary/term/least_privilege

Refactoring Guru. (n.d.). Strategy design pattern. Retrieved July 17, 2024, from https://refactoring.guru/design-patterns/strategy

Microsoft. (n.d.-a). What is SIEM? Microsoft Security. Retrieved July 17, 2024, from https://www.microsoft.com/en-ca/security/business/security-101/what-is-siem

CrowdStrike. (n.d.). SIEM vs log management. Cybersecurity 101 - Observability. Retrieved July 17, 2024, from https://www.crowdstrike.com/cybersecurity-101/observability/siem-vs-log-management/

Splunk. (n.d.-a). Splunk. Retrieved July 17, 2024, from https://www.splunk.com/

Splunk. (n.d.-b). Splunk documentation. Retrieved July 17, 2024, from https://docs.splunk.com/Documentation

OSSEC. (n.d.). Log samples from Apache. Retrieved July 17, 2024, from https://www.ossec.net/docs/log_samples/apache/apache.html

Lighthouse Labs. (n.d.-a). Find security vulnerabilities with Python. Lighthouse Labs. Retrieved July 17, 2024, from https://web.compass.lighthouselabs.ca/p/cyber/days/w03d5/activities/2947

Lighthouse Labs. (n.d.-b). Finding basic security issues in logs. Lighthouse Labs. Retrieved July 17, 2024, from https://web.compass.lighthouselabs.ca/p/cyber/days/w03d5/activities/2945




The widely accepted citation format in the cyber security industry is the APA format. Use this format for all projects in the program. Once you enter the industry, you may follow a different citation style if instructed by your organization.
Note

Examples: A guide to digital forensics and cybersecurity tools. Forensics Colleges. (2022, May 19). https://www.forensicscolleges.com/blog/resources/guide-digital-forensics-tools

Whitman, M., & Mattord, H. (2017). Principles of information security (6th ed.). CENGAGE Learning Custom Publishing.


