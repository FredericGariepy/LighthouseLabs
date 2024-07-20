
## Table of Contents (Playbooks)
- [Reading](https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf)
- [Phishing Attacks](#phishing)🎣
- [Brute Force Attacks](#brute-force-attacks) 👊
> Ransomware,
> Command-and-Control (C2) Traffic,
> Insider Threat (Data Leakage),
- [Impossible Travel](#impossible-travel)
> Cloud Misconfigurations,
> Suspicious Logins


## Glosary 
| term | def|
|-|---|
|CoX |chief experience officer|
|SecOps |Security Operations|
|SOAR|Security Orchestration, Automation, Response|

## Phishing
# :wavy_dash: :fishing_pole_and_fish: :wavy_dash:
One of the most prevalent attack.

Through email, text message, impersonation of company executive, impersonation of cloudbased file storage/sharing site.

-_Playbook Start_-
#### Enrichment & Context
- Note the source and destination IP addresses and ports.
- List all the email addresses against which the alerts were found.
- Go through the email content and filter out all the URLs found.

#### Resolve all URLs to IPs and check the reputation for each IP
a) Mark ‘true positive’ if bad and escalate the collected information, otherwise

#### Analyze URLs in sandboxed environment by following them
a) Note any suspicious behavior such as:
> file downloaded,
> fake/replica/[fugazy websites](https://www.getcybersafe.gc.ca/en/resources/real-examples-fake-online-stores)
> opens, and unknown redirections Containment & Remediation

^If any of these found, mark `true positive` and escalate.^

#### Containment & Remediation
1. Once phishing is confirmed, send a security alert email to entire organization, notifying them about the targeted activity going on.
2. Block all the malicious URLs found in the alerts (and IP addresses) with firewall.
3. Run thorough anti-malware scans against the users who received the emails (found in alerts)



---
## Brute Force Attacks 
# :lock::key:
Generally, the attacker has either:
a. reverse engineered or 
b. purchased on the dark web legitimate usernames and applies a vast library of potential passwords to gain access

-_Playbook start_-
#### 1 Enrichment & Context:
- Source IP address –is it internal or external
-  Target IP and OS information

#### 2 Investigation

a) If __internal IP__:
Search of any previous alerts raised on the entity (source IP). 
The machine might be already compromised and might still be compromised.
- I) If the alerts are involving a malware alert, escalate the case to Tier 2.
- II) Tier 2: Block the traffic from the source IP, disinfect the machine, verify the source of the malware and unblock the machine once no threats are found.

> Determine which data source was used to trigger the alert.
>
>  Is the alert based on network logs or actual on-host login information?

b) If __External IP__:
Search the IP using IP reputation sites and act accordingly

(_continue the next steps of this playbook to gather information for Tier 2_).


#### 3️ Network based logs:
Here we assume that the product triggering the alert cannot be sure about the traffic it monitors, as it might be encrypted.

-> In this case, we only try to find out indicator of failure.

a) Find out which ports were used for the brute force.

b) Search the IP using IP reputation sites and act accordingly (_continue the next steps of this playbook to gather information for Tier 2_).

c) If the attack port does not match any listening service or and previously running service, mark the case as a ‘false positive’

(_since there is no chance of success without a service listening on the port_).

Escalate the source IP’s information to Tier 2 for further hunting, as this is still considered an indication of a malicious presence trying its ‘luck’ around the network.

#### 4 Host-based logs
(or logs from the last step of the previous section)

a) Search the logs for events indicating a ‘failure to login’ or ‘user does not exist’ (depends on the attacked service).

If such logs exist, measure the time span during which they occurred. If the time span is very short, aka mere seconds between attempts, escalate the case to Tier 2, an indication of a malicious presence trying its ‘luck’ around the network.

b) Search the logs for a successful login log entry. If such entry is found, escalate the case to Tier 2 for further investigation.

#### 5 Containment & Remediation
1. Find out all users that were used in the brute force attack. Look for any suspicious username from this list and search for
other hosts that these usernames were used on.
2. Notify the owners of the legitimate accounts and the owners of the targeted machines that a brute force attempt was made
on their assets.
3. Perform a more thorough investigation on the possibly affected hosts and act accordingly.
4. If the attacker is an external IP, block it and ensure that the firewall is configured to prevent remote login attempts
for the specific port in the case it was unnecessarily open to the public.
5. If the attacker is an internal IP, search for any malware infections and past malware alerts on the source host to see
if the host is vulnerable.
---
## Impossible Travel
# :hole: :business_suit_levitating:
Timely Office 365 feature that enables you to compare a user’s last known location to their current location, then judge whether the trip is normal or not given the time that has elapsed between the two coordinates.

-_Playbook start_- 
#### 1 Enrichment & Context
- Enrich the user: Gauge the risk profile of the user (i.e. traveling engineer vs CxO vs domain admin?) Has the user travelled to these countries before?
- Enrich the IP: Are the countries on a sanction list? Is the IP an approved business VPN exit point?

#### 2 Investigation
**Decide**: Consider the time of day, risk of user and
SOC analyst opinions to help decide if false positive.

#### 3 Containment and Remidiation
1. Contain the access: Remove groups/permissions to systems, disable account, block source login IP addresses, escalate user to require two-factor authentication.
2. Eradicate the access: Reset user password, notify HR/the user’s manager that the
account needs resetting.
3. Recover: Initiate automatic communication (e.g. Slack, Teams) to the user/their manager asking them to explain recent actions. Investigate how the incident could happen


