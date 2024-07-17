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

The client script then sends logs to the log monitor server via a socket.

Now, on the server side, [server.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/server.py) is up and running through it's [cron](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/readme.md).
The server starts up the [access_log_monitor.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/log_monitor/access_log_monitor.py) as a seperate process and then server.py listens for log lines which were sent by the client.

When the server.py script receives a log, it starts a thread [triage.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/triage.py) and passes it the log. Having triage as a thread allows the server to continue receiving logs without blocking.

The triage script's role is to parse, analyze and *write* the log it received into the approriate directory/file.

To parse, the log is captured by regex expressions and made into a dicitonary object.
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
- **Encryption**: Log lines sent from [client.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/client.py) to [server.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/server.py) should be encrypted as they send out and received in order to proctect against [Network Sniffing](https://attack.mitre.org/techniques/T1040/).
- **Sanitization**: Log lines received by the log monitor server should sanitized in order to protect against [Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/).
- **Code structure**: The [triage.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side/server-client/triage.py) file should be improved by addoptiong the [strategy design pattern](https://refactoring.guru/design-patterns/strategy). As more Rules/Algortihms (filters) are developed for triage, these encpasulated filters are then applied appropriately to logs, as opposed to the current script, where developed filters are added to a growing chain of conditions that a log passes through. 
- **Code permissions**: On the client side, in both [fetch_access_logs.sh](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/) and [fetch_error_logs.sh](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_error_logs.sh), the script interacts directly with log files found in /var/log/apache2/. The scripts start in the root user's cron job, as sudo priviledges are required to access the directory. Scripts with such access run a security risk and should instead be run with the principle of [least privilege](https://csrc.nist.gov/glossary/term/least_privilege).
- **Improved monitorig**: The log monitor should further have scripts which monitor for diffrent log baselines and corelations of log events. More rules and/or algorithms should be developed and implemented to better analyze/correlate logs, in order to categorize/report their security standing accurately.
- **Improved log storage**: The storage method should employ a more robust solution such as a database. This will enable using queries to monitor log activity, and unlock a lot of potential for analysis.
- **Support of Windows**: This project does **not** provide a log monitoring solution for the Windows operating system and new code will required to do so.

# Conclusion
Building a log monitoring solution is a very demanding endavour.

This project delivers a rudimentary [working system](https://www.youtube.com/watch?v=FeMmxXmpgfs&feature=youtu.be) for log monitoring on Linux operating systems.
The organization would greatly benefit from adopting the use of a security information and event management [SIEM](https://www.microsoft.com/en-ca/security/business/security-101/what-is-siem)system. Such systems can monitor the organizations's assets (both Linux and Windows machines) and send security notifications.

SIEMs are [not only great tools for log management](https://www.crowdstrike.com/cybersecurity-101/observability/siem-vs-log-management/) but also provide incident monitoring and response as well as log analysis/corellations to detect and respond to potential threats. All functions which fit the organization's needs and offer great return on investment.

There are many SIEMs available on the market. [Splunk](https://www.splunk.com/) is a SIEM which offers a *free tier* that your organization can test out. Feel free to further contact me in order to implement Splunk as solution to your security needs. There is additonally great [official documentation](https://docs.splunk.com/Documentation) to assist your implementation.

# References
References

Workflow: a short description of the steps to be taken to successfully monitor and document the logs in the network
Consider what you will monitor, when, and how often.
  
Programming: Outline what programming tools you will use to successfully complete the task. Be sure to include key commands and/or scripts that you will use or create.
Expected Output: What are the expected results of the commands or scripts you are planning to use? Why are they important or useful?
Documentation: How will you capture and document the monitoring process? Consider the timing and how you will share it with your manager.
Unusual Behaviour: Identify what elements in your monitoring would constitute a “flag” to alert your manager.
Potential Iterations: What elements of your workflow would you want to improve, and why? Identify some ways you could develop skills to support this improvement.


https://www.ossec.net/docs/log_samples/apache/apache.html



Report Format

Organize all the information you gathered into a report and be sure to include the following: * Table of Contents * Introduction * Solutions Section (Where you discuss your script and how it functions) * Potential iterations Section (where you discuss potential improvements) * Conclusion * References
References

References are crucial for credibility, validating arguments, and avoiding plagiarism. References enable readers to verify information; build on existing knowledge, and uphold ethical standards while promoting transparency. All the resources you access should be listed in a References List at the end of your work.

You may use tools, like Citation Machine, to generate citations for your work.
Instruction

The widely accepted citation format in the cyber security industry is the APA format. Use this format for all projects in the program. Once you enter the industry, you may follow a different citation style if instructed by your organization.
Note

Examples: A guide to digital forensics and cybersecurity tools. Forensics Colleges. (2022, May 19). https://www.forensicscolleges.com/blog/resources/guide-digital-forensics-tools

Whitman, M., & Mattord, H. (2017). Principles of information security (6th ed.). CENGAGE Learning Custom Publishing.


