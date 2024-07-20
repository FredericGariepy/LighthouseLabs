
## Table of Contents
- [Reaading](https://learningimages.lighthouselabs.ca/Cyber+BC/Cyber+BC+C4/Top_Security_Playbooks_2022.pdf)
- [Brute Force Attacks](#brute-force-attacks)
- Phishing Attacks
- Ransomware
- Command-and-Control (C2) Traffic
- Insider Threat (Data Leakage)
- Impossible Travel
- Cloud Misconfigurations
- Suspicious Logins


## Glosary 
| term | def|
|-|---|
|SOAR|Security Orchestration, Automation, Response|
|SecOps |Security Operations|


## Brute Force Attacks
Generally, the attacker has either:
a. reverse engineered or
b. purchased on the dark web legitimate usernames and applies a vast library of potential passwords to gain access

#### :one: Enrichment & Context:
- Source IP address –is it internal or external
-  Target IP and OS information

#### :two: Investigation

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


#### 3️⃣ Network based logs:
Here we assume that the product triggering the alert cannot be sure about the traffic it monitors, as it might be encrypted.

-> In this case, we only try to find out indicator of failure.

a) Find out which ports were used for the brute force.

b) Search the IP using IP reputation sites and act accordingly (_continue the next steps of this playbook to gather information for Tier 2_).

c) If the attack port does not match any listening service or and previously running service, mark the case as a ‘false positive’

(_since there is no chance of success without a service listening on the port_).

Escalate the source IP’s information to Tier 2 for further hunting, as this is still considered an indication of a malicious presence trying its ‘luck’ around the network.

#### :four: Host-based logs
(or logs from the last step of the previous section)

a) Search the logs for events indicating a ‘failure to login’ or ‘user does not exist’ (depends on the attacked service).

If such logs exist, measure the time span during which they occurred. If the time span is very short, aka mere seconds between attempts, escalate the case to Tier 2, an indication of a malicious presence trying its ‘luck’ around the network.

b) Search the logs for a successful login log entry. If such entry is found, escalate the case to Tier 2 for further investigation.

#### :five: Containment & Remediation
1. Find out all users that were used in the brute force attack. Look for any suspicious username from this list and search for
other hosts that these usernames were used on.
2. Notify the owners of the legitimate accounts and the owners of the targeted machines that a brute force attempt was made
on their assets.
3. Perform a more thorough investigation on the possibly affected hosts and act accordingly.
4. If the attacker is an external IP, block it and ensure that the firewall is configured to prevent remote login attempts
for the specific port in the case it was unnecessarily open to the public.
5. If the attacker is an internal IP, search for any malware infections and past malware alerts on the source host to see
if the host is vulnerable.
