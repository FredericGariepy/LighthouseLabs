# OSI Model for Network Troubleshooting

## Layer 1: Physical

| Layer   | Protocol Types          | Solutions                                                                                                 |
|---------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| Physical| Ethernet, Wi-Fi         | Check all physical components in the network: Ensure everything is plugged in correctly and working. Check for damaged cabling, connectors, or terminations. |

## Layer 2: Data Link

| Layer    | Protocol Types                   | Solutions                                                                                                 |
|----------|----------------------------------|-----------------------------------------------------------------------------------------------------------|
| Data Link| Ethernet, MAC , Switches, VLANs  | Verify switch and VLAN configurations, MAC addresses, look for IP address conflicts, and eliminate duplicate IPs. Check Spanning Tree Protocol (STP) for network loops. |

## Layer 3: Network

| Layer   | Protocol Types                   | Solutions                                                                                                 |
|---------|----------------------------------|-----------------------------------------------------------------------------------------------------------|
| Network | IP, ICMP, ARP, Routing Protocols | Troubleshoot network addressing and routing issues. Use PING to locate network issues. Utilize ICMP tools like Tracert/Traceroute to aid troubleshooting. Check for damaged networking devices or wrong configurations. |

## Layer 4: Transport

| Layer    | Protocol Types | Solutions                                                                                                 |
|----------|----------------|-----------------------------------------------------------------------------------------------------------|
| Transport| TCP, UDP       | Verify that firewalls aren't blocking TCP/UDP ports. Check for blocked or damaged ports. Ensure Quality of Service (QoS) settings are correct. |

## Layers 5 and 6: Session and Presentation

| Layer             | Protocol Types | Solutions                                                                                                 |
|-------------------|----------------|-----------------------------------------------------------------------------------------------------------|
| Session, Presentation | N/A         | Issues are rare at these layers as they complement the Network layer functionalities. |

## Layer 7: Application

| Layer      | Protocol Types                       | Solutions                                                                                                 |
|------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Application| SMTP, HTTP, POP3, FTP, DNS           | Troubleshoot client-server and service-related applications. Use NSLOOKUP to verify DNS functionality. Utilize TCPDUMP and Wireshark for filtering and analyzing TCP/IP packets in real-time or offline. |
