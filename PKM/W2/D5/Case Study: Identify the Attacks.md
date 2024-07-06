Overview
1. [PCAP file Analysis **1**](#pcap-file-1--cyberbcc243)
2. [PCAP file Analysis **2**](#pcap-file-2--cyberbcc244) <- *This is the most intresting part*
3. [Incident Report](#incident-report)

Download Wireshark pcap:

4. [PCAP 1](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D5/Cyber%2BBC%2BC2.4.3.pcapng)
5. [PCAP 2](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D5/Cyber%2BBC%2BC2.4.4.pcapng)
---
Workflow
1. Open PCAP.
2. Add timestamp
3. Overview, find signs of IoC.
4. Apply filters from [Traffic anomally detection source](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D4/Traffic%20Anomaly%20Detection%20with%20Wireshark%20White%20Box.md)
5. Correlate diplayed captures with nmap and or IoCs.

# PCAP File 1 : Cyber+BC+C2.4.3
### First IoC, Sign of ARP scan
> 46	2023-06-06 21:36:44.553028	VMware_9f:66:38		Broadcast		ARP	60	Who has 172.16.14.1? Tell 172.16.14.3

#### Attacker profile 
- Display filter: `eth.src == 00:50:56:9f:66:38 and arp`
- Total display rows 1026. 
- MAC:  00:50:56:9f:66:38
- IP: 172.16.14.3
- Likely commmand used `nmap -PR <victim IP>`

#### Victim response:
- Display filter: `eth.dst == 00:50:56:9f:66:38 and arp`
- Total display rows 9.
- victim responce: 172.16.14.53 is at 50:01:00:04:00:00
- Attacker discovers 1 host.

### Second IoC, sign of Port Scan
> 569	2023-06-06 21:36:46.669280	172.16.14.3	46880	172.16.14.53	1025	TCP	60	46880 → 1025 [SYN] Seq=0 Win=1024 Len=0 MSS=1460

#### Attacker profile 
- Display filter: `ip.src == 172.16.14.3 and tcp.flags.syn`
- Total display rows 2037. 
- MAC SRC:  00:50:56:9f:66:38
- MAC IP: 172.16.14.3
- Likely commmand used `nmap -sS <Vivtim IP>` ([Half-open scanning](https://nmap.org/book/man-port-scanning-techniques.html))

#### Victim response:
- Display filter: `ip.dst == 172.16.14.3 and tcp.flags.syn == 1 and tcp.flags.ack == 1`
- Total display rows 14.
- victim responce shows open port: 135, 139, 445, 3389.

Reference in MITRE ATT&CK Framework:
- Tactic: Discovery
- Technique: [Network Service Scanning (T1046)](https://attack.mitre.org/techniques/T1046/)

### Third IoC, Remote Services: Remote Desktop Protoco

- Display filter: `copt || rdp `
- Total display rows 2.
- Port 3389 is dedicated to Remote Desktop Protocol (RDP).
Reference in MITRE ATT&CK Framework:
- Tactic: Remote Service
- Technique: [Remote Services: Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001/)
Adversaries may use Valid Accounts to log into a computer using the Remote Desktop Protocol (RDP).
The adversary may then perform actions as the logged-on user.

RPD was unsuccesfull, as there is NO COTP (Connection-Oriented Transport Protocol) CR (Connection Request) and CC (Connection Confirm)

---
# PCAP File 2 : Cyber+BC+C2.4.4

## Confirming Attacker is using NMAP
- Display filter: `ip.src == 172.16.14.3 and tcp.dstport == 80 and ip.dst == 172.16.14.52`
Following the TCP stream between attacker IP and victim IP on victim port 80:
- Starting at display filter: `tcp.stream eq 2019`
We can see that attacker IP is using Nmap in their POST request to victim's port 80
```
POST /sdk HTTP/1.1
Host: 172.16.14.52
Connection: close
Content-Length: 441
User-Agent: Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
```

### First IoC, Sign of ARP scan
> 2023-06-06 17:36:44.327281317	VMware_9f:66:38		Broadcast		ARP	60	Who has 172.16.14.1? Tell 172.16.14.3

#### Attacker profile 
- Display filter: `eth.src == 00:50:56:9f:66:38 and arp`
- Total display rows 1026. 
- MAC:  00:50:56:9f:66:38
- IP: 172.16.14.3
- Likely commmand used `nmap -PR <victim IP>`

#### Victim response:
- Display filter: eth.dst == 00:50:56:9f:66:38 and arp
- Total display rows 4.
- victim responce: 172.16.14.52 is at 50:01:00:05:00:00
- Attacker discovers 1 host.
> Difference between PCAP 1 & 2 are the victim host discovered by attacker (172.16.14.3)

### Second IoC, sign of Port Scan
> 524	2023-06-06 17:36:46.443167278	172.16.14.3	46880	172.16.14.52	1025	TCP	60	46880 → 1025 [SYN] Seq=0 Win=1024 Len=0 MSS=1460

#### Attacker profile 
- Display filter: `ip.src == 172.16.14.3 and tcp.flags.syn`
- Total display rows 2170. 
- MAC SRC:  00:50:56:9f:66:38
- MAC IP: 172.16.14.3
- Likely commmand used `nmap -sS <Vivtim IP>` ([Half-open scanning](https://nmap.org/book/man-port-scanning-techniques.html))

#### Victim response:
- Display filter: `ip.dst == 172.16.14.3 and tcp.flags.syn == 1 and tcp.flags.ack == 1`
- Total display rows 32.
- victim responce shows open port: 80, 3389, 9200

### Third IoC, Remote Services: Remote Desktop Protoco

- Display filter: `copt || rdp `
- Total display rows 4.
- Port 3389 is dedicated to Remote Desktop Protocol (RDP).
MITRE ATT&CK : [Remote Services: Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001/)
Adversaries may use Valid Accounts to log into a computer using the Remote Desktop Protocol (RDP).
The adversary may then perform actions as the logged-on user.

**RPD was SUCCESSFUL**, as there is COTP (Connection-Oriented Transport Protocol) CR (Connection Request) and CC (Connection Confirm)

### Fourth IoC, Remote Services: 

- Display filter: `http`
- Total display rows 18.
- Port 80 is dedicated to unencryted HTTP
MITRE ATT&CK : [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

Adversaries may attempt to exploit a weakness in an Internet-facing host or system to initially access a network. The weakness in the system can be a software bug, a temporary glitch, or a misconfiguration.

GET requests to suspicious endpoints
- /evox/about
- /HNAP1
> HNAP (Home Network Administration Protocol) is a protocol developed by Cisco for remote management of home networking devices.
Command injection vulnerability [CVE-2022-44808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44808) through well-designed /HNAP1 requests.

### Fifth IoC, Remote Services: potentially exfiltration, API exploit, cloud storage

- Display filter: `ip.src == 172.16.14.3 and tcp.dstport == 9200`
- Port 9200 is dedicated to Elasticsearch.
- Total displayed rows: 110
> Elasticsearch is a distributed search and analytics engine built on Apache Lucene. 
>
> Most popular search engine and is commonly used for log analytics, full-text search, security intelligence, business analytics, and operational intelligence use cases.

You can send data in the form of JSON documents to Elasticsearch using the API - [source](https://aws.amazon.com/what-is/elasticsearch/)

MITRE ATT&CK :
- Potentially [Exfiltration](https://attack.mitre.org/tactics/TA0010/)
The adversary is trying to steal data.

- Potentially [Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)
Adversaries may access data from cloud storage.

- Potentially [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
Adversaries may attempt to exploit a weakness in an Internet-facing host or system to initially access a network. The weakness in the system can be a software bug, a temporary glitch, or a misconfiguration.

Potential CVE:
- [CVE-2023-20034](https://nvd.nist.gov/vuln/detail/CVE-2023-20034)
> Vulnerability in the Elasticsearch database used in the of Cisco SD-WAN vManage software could allow an unauthenticated, remote attacker to access the Elasticsearch configuration database of an affected device with the privileges of the elasticsearch user.

---
# Incident report
###### Date format (yyyy-mm-dd)
Report filed on 2024-07-06.

Incident occured on 2023-06-06.

## Incident description:
An adversary machine on the network found two hosts.

The attacker succesfully connected to one machine through remote desktop.

Attacker interacted with Elasticsearch in possible data exfiltration of cloud storage data.

## Executive summary:

On 2023-06-06 at 17:36,

A machine (attacker) on the network scanned the network for hosts (victims).
The attaker found one victim.

The attacker, **succesfully** connected remotely to the victim using Remote Desktop Protocol.
The attacker then looked for vulnerabilties on the victims' webserver, but was unsuccesful.
The attacker sucesfully used Elasticsearch on the victim, **potentially exfiltrating data** from cloud services.

4 hours later,
2023-06-06 at 21:36, the same attacker, scanned the network for victims again. 
The attacker found one new victim.

The attacker unsucessfully attempted to connect remotely to the new victim.

## Description of actual incident:

On 2023-06-06 at 17:36,

Attacker IP 172.16.14.3 made an nmap ARP scan on the network, found victim host 172.16.14.**52**.

Attacker then performed an nmap port scan on the victim, ports found: 80, 3389, 9200.

Attacker looked for vulnerable endpoints on victim's webserver at port 80, was unsucessfull as shown by victim's HTTP 404 reply.

Attacker connected with RPD on port 3389, and was **SUCCESSFUL**, as shown by COTP's Attacker CR and Victim CC.

Attacker used Elastic search sucesfully through request on victim's port 9200. Due to TLS.1v3, conversation is encrypted but conversations on 110 packets seems to indicate that data flowed succesfully.

4 hours later, 

Attacker IP 172.16.14.3 made an nmap ARP scan on the network, found victim host 172.16.14.**53**.

Again, attacker made a port scan on the victim, found ports: 135, 139, 445, 3389.

Attacker probed ports 135, 139, 445 unsucessfully.

Attacker attempted to RDP connect on port 3389, unsucesfully.

## What was discovered as a result of the scan:

- Attacker IP(s) : 172.16.14.3
- Attacker MAC : 00:50:56:9f:66:38
- first packet of attack:
> 46	2023-06-06 21:36:44.553028	VMware_9f:66:38		Broadcast		ARP	60	Who has 172.16.14.1? Tell 172.16.14.3
- Time of attack: 023-06-06 21:36:44.55302
- Packet number of first packet in attack: 43
- Protocol(s) used in attack: ARP
- Suspected Nmap/scan configuration: `nmap -PR <victim IP>`
- List of NVD records apply to the attack:

[Get /HNAP](#fourth-ioc-remote-services)
- Home Network Administration Protocol is a protocol developed by Cisco for remote management of home networking devices.
- Command injection vulnerability [CVE-2022-44808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44808) through well-designed /HNAP1 requests.
- Unsuccessful probe of this service was done by the attacker.

Potential CVE:
- [CVE-2023-20034](https://nvd.nist.gov/vuln/detail/CVE-2023-20034)
> Vulnerability in the Elasticsearch database used in the of Cisco SD-WAN vManage software could allow an unauthenticated, remote attacker to access the Elasticsearch configuration database of an affected device with the privileges of the elasticsearch user.
- Attacker did use Elasticsearch on victim port 9200.

<!--
# References
Gariepy, F. (2024). Understanding Network Security. Github. https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D4/Traffic%20Anomaly%20Detection%20with%20Wireshark%20White%20Box.md
-->
