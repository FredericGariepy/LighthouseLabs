nmap scan: \
https://nmap.org/book/port-scanning-options.html
- basic commands* (maybe)
Example: \
`nmap 192.168.1.0/24` scan IP range in subnet \
`nmap -A <IP>` Aggressive scan: (services, OS, script scanning) \
`nmap -O <IP>` Operating system of target \
`nmap -oN output.txt <IP>` output simple scan to output.txt \

OpenVAS
- report components (OpenVAS generated report: CVSS, CVE, mitigations, etc...)
- https://web.compass.lighthouselabs.ca/p/cyber/projects/cat-vulnerabilities

Incident Response
- steps:
Prepare, Detection + Analysis, Containment + Eradication + Recovery, Post-Incident Activity
- https://web.compass.lighthouselabs.ca/p/cyber/projects/ir-playbook

- "IR plan"
> a.k.a. Walk me through the steps, what happens at each step
- Team members at different IR steps
- Policies
- Playbook
- ...

Logging in Windows & Linux (general)
- Windows: Event Viewer (`eventvwr.msc`), Event IDs, etc.. \
Windows event log location is `C:\WINDOWS\system32\config\ folder.` \
https://www.solarwinds.com/resources/it-glossary/windows-event-log
- Linux: `/var/log/syslog`, log rotation, etc.. 

Risk Assessment 
- metrics, tables
- https://web.compass.lighthouselabs.ca/p/cyber/projects/risk-management

Encyrption (general)
- make a ssh key pair `ssh-keygen` for user in the .ssh folder
- explain specific flags
Example:
`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

Firewalls, in linux `ufw`:
- Go to 1:35: https://web.compass.lighthouselabs.ca/activities/3267/lectures/14544
- read man pages : https://manpages.ubuntu.com/manpages/focal/en/man8/ufw.8.html
Examples: \
`sudo ufw status` \
`sudo ufw allow <something>` \
`sudo ufw enable` \
`sudo ufw allow from <IP> protocol tcp to any port 22` \

Programing:
- syntax flaws (python, bash)
