# Log Monitoring Workflow
07.17.2024
##  Table of Contents
1. .
2. .
3. .
4. 

## Executive Summary
This is a log monitor. It helps keeps track of the activity on a website through the use of logs.

Log activity that is flagged as an indicator of compromsise results in a security notification.

Notifications are important in mainting good security posture and gives visibility to what's happening to your assets.

Building a Log monitoring solution is a very demanding endevour, many iterations will be required to acheive a full-bodied solution.
Consult the recommendations found at the end and learn how adopting a SIEM may help your organization.


## Solutions Section (scripts & how they work)
Please [watch the video demo](https://youtu.be/FeMmxXmpgfs) of this log monitoring project.

After watching the video,

please consult the workflow image bellow before continuing.
![log_monitor_solution](https://github.com/user-attachments/assets/f2e57d84-25b8-4fa7-b943-30b3e777df1d)

### [Project files](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN)

The log monitor consists of two part: a [server-side](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN/server-side) and a [client-side](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side)

The [client-side](https://github.com/FredericGariepy/LighthouseLabs/tree/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side) contains
two bash files, one that will [fetch_access_logs.sh](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_access_logs.sh) and another that will [fetch_error_logs.sh](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_error_logs.sh)

a [client.py](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/client.py),
which receives  sends logs to the log monitor server.

2. Two files which monitor the apache log files for changes adn 
 (https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_access_logs.sh)
- (https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W3/D5/PROJECT_with_PAVAN/client-side/fetch_error_logs.sh)

    Code should include essential commands with explanatory comments.
    Identify flag elements for manager alerts, linked to Indicators of Compromise (IoCs).
    


# Potential iterations Section (where you discuss potential improvements) 
# Conclusion 
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


