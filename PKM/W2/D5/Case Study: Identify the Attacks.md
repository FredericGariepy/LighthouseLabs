
1. [PCAP file **1**](#pcap-file-1--cyberbcc243)
2. [PCAP file **2**](#pcap-file-2--cyberbcc244)

# Title of report

Incident report 01001
Date filed
Date of incident (as reported)
Incident description (as reported)
Executive summary
Description of actual incident
What was discovered as a result of the scan
Attacker IP(s)
Attacker MAC(s)
Time of attack (first packet of attack)
Packet number of first packet in attack
Protocol(s) used in attack
Suspected Nmap/scan configuration
List any NVD records that may apply to the attack; describe how they are related
Screen captures from Wireshark showing attack with explanations (Appendix A)

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
- MAC SRC:  00:50:56:9f:66:38
- MAC IP: 172.16.14.3
- Likely commmand used `nmap -PR <victim IP>`

#### Victim response:
- Display filter: eth.dst == 00:50:56:9f:66:38 and arp
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
- victim responce shows open port: 135,139, 445, 3389

Reference in MITRE ATT&CK Framework:
- Tactic: Discovery
- Technique: [Network Service Scanning (T1046)](https://attack.mitre.org/techniques/T1046/)
---
# PCAP File 2 : Cyber+BC+C2.4.4
### First IoC, Sign of ARP scan
> 2023-06-06 17:36:44.327281317	VMware_9f:66:38		Broadcast		ARP	60	Who has 172.16.14.1? Tell 172.16.14.3

#### Attacker profile 
- Display filter: `eth.src == 00:50:56:9f:66:38 and arp`
- Total display rows 1026. 
- MAC SRC:  00:50:56:9f:66:38
- MAC IP: 172.16.14.3
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

### Third IoC, sign of Port Scan

- Display filter: `ip.src == 172.16.14.3 and tcp.dstport == 80 and ip.dst == 172.16.14.52`
Following the TCP stream between attacker IP and victim IP on victim port 80:
- Starting at display filter: `tcp.stream eq 2019`
We can see that attacker IP is using Nmap
```
POST /sdk HTTP/1.1
Host: 172.16.14.52
Connection: close
Content-Length: 441
User-Agent: Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
```




<!--
# References
Gariepy, F. (2024). Understanding Network Security. Github. https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D4/Traffic%20Anomaly%20Detection%20with%20Wireshark%20White%20Box.md
-->
