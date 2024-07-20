## Resources:
- [x] Playbook [Phishing Attack](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W4/D5/Project/reading/Top%20Security%20Playbooks%202022-23.md#phishing)
- [ ] [InfoStealer logs](https://bolster.ai/blog/stealer-logs)

Storyline:




## Communications
Contact stipulations:
1. On case of suspected breach both Client and Client's Third-Party provider must be sent specific communications.
- Client (now, Box) must receive an executive summary.
- Box Production Manager must receive information highlighting major security breach events, and listed potential impacts on company operations.
- Third-Party provider must a receive full report, with actionable items included.

#
Playbook Phishing attack in PLAY

#### IP Source, flaged BAD, Destination,Port
true positive

Source IP: 154.59.26.3

Flagged as **bad**

Flagged bad by [abuseipdb.com](https://www.abuseipdb.com/check/154.59.26.3), [spamhaus.org](https://www.spamhaus.org/ip-reputation?ip=154.59.26.3).

Classified as mail server and dictionary attacker by [projecthoneypot](https://www.projecthoneypot.org/ip_154.59.26.3).
destination IP: 203.0.113.10 (Mail Server)

Destination Port: 993 (IMAPS)

#### List all the email addresses against which the alerts were found.
minka@box.cat, info@box.cat, contact@box.cat, support@web.com, sales@web.com, billing@web.com, feedback@box.cat, hr@cat.com

#### Go through the email content and filter out all the URLs found.

One of the most prevalent attack.

Through email, text message, impersonation of company executive, impersonation of cloudbased file storage/sharing site.

-Playbook Start-
Enrichment & Context

    Note the source and destination IP addresses and ports.
    List all the email addresses against which the alerts were found.
    Go through the email content and filter out all the URLs found.

Resolve all URLs to IPs and check the reputation for each IP

a) Mark ‘true positive’ if bad and escalate the collected information, otherwise
Analyze URLs in sandboxed environment by following them

a) Note any suspicious behavior such as:

    file downloaded, fake/replica/fugazy websites opens, and unknown redirections Containment & Remediation

^If any of these found, mark true positive and escalate.^
Containment & Remediation

    Once phishing is confirmed, send a security alert email to entire organization, notifying them about the targeted activity going on.
    Block all the malicious URLs found in the alerts (and IP addresses) with firewall.
    Run thorough anti-malware scans against the users who received the emails (found in alerts)




Subject: We have a surprise for Marriott customers.
"We have a surprise for Marriott customers."(projecthoneypot n.d.)
