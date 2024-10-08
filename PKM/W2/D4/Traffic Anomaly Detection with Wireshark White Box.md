Made *with* AI (ChatGPT 3.5)
## Traffic Anomaly Detection with Wireshark Black Box
### Table of Contents:
- [nmap detection display filters](#in-wireshark-nmap-detection-display-filters) <- *that's the intresting part*
- [tcp flags to hex](#tcp-flags-to-hex)
- [task command line](#part-1-performing-endpoint-scan-with-nmap)
- [task command stdout](#in-practice-results)
- [nmap cheatsheet](https://stationx-public-download.s3.us-west-2.amazonaws.com/nmap_cheet_sheet_v7.pdf)

## In Wireshark: nmap detection display filters

### Detect: TCP ACK SCAN (-sA) | TCP ACK port scan
- display filter: `ip.dst == <Attacker IP> and tcp.flags.ack==1 and tcp.flags.reset == 1`
> Narrow down the IP DST to the attackers if possible, else take it out.
- heuristics/Signs: Static IP SRC,DST. Dynamic port.
<img src="https://github.com/FredericGariepy/LighthouseLabs/assets/96602008/afa0664d-fca5-46ad-b99c-6433df7afcd4" alt="image" width="300" height="200">

### Detect:  ARP scan (-PR) | network scan:
- display filter: `eth.src == <Attacker MAC> and arp`
> To find Attacker MAC, I first narrowed it down from other detections. Else, just use arp.
- heuristics/Signs: Large arp volume, static MAC SRC, Dynamic & iterating IP info request.

### Detect an intense port scan:
- display filter: `tcp.flags.syn==1 and tcp.flags.ack==0`
- high volume of SYN packets to different ports on the same host, often combined with other types of packets (e.g. ICMP, UDP)

## Part 1: Performing Endpoint Scan with Nmap:
```bash
# A network scan to discover hosts
nmap -sn 192.168.1.0/24

# A host port scan to see what ports are open on a specific host
nmap -p- 192.168.1.10

# A host scan to discover the OS running on the device
nmap -O 192.168.1.10

# An intense port scan
nmap -T4 -A -v 192.168.1.10
```

## In practice, results
```bash
┌──(student㉿kali)-[~]
└─$ ip a 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:1b:76:b0 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.8/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 493sec preferred_lft 493sec
    inet6 fe80::a00:27ff:fe1b:76b0/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default                                                           
    link/ether 02:42:89:90:b7:30 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
                                                                   
┌──(student㉿kali)-[~]
└─$ nmap -sn 10.0.02.0/24                       
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 20:38 EDT
Nmap scan report for 10.0.2.1
Host is up (0.0025s latency).
Nmap scan report for 10.0.2.8
Host is up (0.00045s latency).
Nmap scan report for 10.0.2.25
Host is up (0.0075s latency).
Nmap done: 256 IP addresses (3 hosts up) scanned in 3.18 seconds
                                                                             
                                                                             
┌──(student㉿kali)-[~]
└─$ sudo nmap -p- 10.0.2.25
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 20:39 EDT
Nmap scan report for 10.0.2.25
Host is up (0.0011s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
8080/tcp open  http-proxy
MAC Address: 08:00:27:CB:20:4A (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 130.23 seconds
                                                                             
┌──(student㉿kali)-[~]
└─$ sudo nmap -O 10.0.2.25
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 20:42 EDT
Nmap scan report for 10.0.2.25
Host is up (0.0026s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
8080/tcp open  http-proxy
MAC Address: 08:00:27:CB:20:4A (Oracle VirtualBox virtual NIC)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|phone
Running (JUST GUESSING): Microsoft Windows 11|10|2022|Phone|2008 (97%)
OS CPE: cpe:/o:microsoft:windows_10 cpe:/o:microsoft:windows cpe:/o:microsoft:windows_server_2008::sp1
Aggressive OS guesses: Microsoft Windows 11 21H2 (97%), Microsoft Windows 10 (92%), Microsoft Windows Server 2022 (91%), Microsoft Windows Phone 7.5 or 8.0 (88%), Microsoft Windows Server 2008 SP1 (88%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.71 seconds

┌──(student㉿kali)-[~]
└─$ nmap -T4 -A -v 10.0.2.25
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 20:42 EDT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 20:42
Completed NSE at 20:42, 0.00s elapsed
Initiating NSE at 20:42
Completed NSE at 20:42, 0.00s elapsed
Initiating NSE at 20:42
Completed NSE at 20:42, 0.00s elapsed
Initiating Ping Scan at 20:42
Scanning 10.0.2.25 [2 ports]
Completed Ping Scan at 20:42, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 20:42
Completed Parallel DNS resolution of 1 host. at 20:42, 0.02s elapsed
Initiating Connect Scan at 20:42
Scanning 10.0.2.25 [1000 ports]
Discovered open port 80/tcp on 10.0.2.25
Discovered open port 8080/tcp on 10.0.2.25
Completed Connect Scan at 20:43, 4.95s elapsed (1000 total ports)
Initiating Service scan at 20:43
Scanning 2 services on 10.0.2.25
Completed Service scan at 20:44, 96.72s elapsed (2 services on 1 host)
NSE: Script scanning 10.0.2.25.                                              
Initiating NSE at 20:44                                                      
Completed NSE at 20:44, 5.07s elapsed                                        
Initiating NSE at 20:44                                                      
Completed NSE at 20:44, 1.04s elapsed                                        
Initiating NSE at 20:44                                                      
Completed NSE at 20:44, 0.00s elapsed                                        
Nmap scan report for 10.0.2.25                                               
Host is up (0.0020s latency).                                                
Not shown: 998 filtered tcp ports (no-response)                              
PORT     STATE SERVICE    VERSION                                            
80/tcp   open  http       Microsoft IIS httpd 10.0                           
|_http-server-header: Microsoft-IIS/10.0                                     
| http-methods:                                                              
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows
8080/tcp open  http-proxy PRTG
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: 36B3EF286FA4BEFBB797A0966B456479
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 302 Moved Temporarily
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 54
|     Date: Sat, 06 Jul 2024 00:43:11 GMT
|     Expires: 0
|     Cache-Control: no-cache
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     Server: PRTG
|     Location: /public/login.htm?loginurl=%2Fnice%20ports%2C%2FTrinity.txt.bak&errorid=0
|     <HTML><BODY><B>302 Moved Temporarily</B></BODY></HTML>
|   GetRequest, HTTPOptions, RTSPRequest: 
|     HTTP/1.1 302 Moved Temporarily
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 54
|     Date: Sat, 06 Jul 2024 00:43:11 GMT
|     Expires: 0
|     Cache-Control: no-cache
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     Server: PRTG
|     Location: /index.htm
|     <HTML><BODY><B>302 Moved Temporarily</B></BODY></HTML>
|   SIPOptions: 
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 48
|     Date: Sat, 06 Jul 2024 00:43:51 GMT
|_    <HTML><BODY><B>400 Bad Request</B></BODY></HTML>
| http-title: Welcome | PRTG Network Monitor (WINDOWS11-DESKT)
|_Requested resource was /index.htm
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-server-header: PRTG
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.94SVN%I=7%D=7/5%Time=6688931E%P=x86_64-pc-linux-gnu%r(
SF:GetRequest,157,"HTTP/1\.1\x20302\x20Moved\x20Temporarily\r\nConnection:
SF:\x20close\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Le
SF:ngth:\x2054\r\nDate:\x20Sat,\x2006\x20Jul\x202024\x2000:43:11\x20GMT\r\
SF:nExpires:\x200\r\nCache-Control:\x20no-cache\r\nX-Content-Type-Options:
SF:\x20nosniff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nServer:\x20PRTG
SF:\r\nLocation:\x20/index\.htm\r\n\r\n<HTML><BODY><B>302\x20Moved\x20Temp
SF:orarily</B></BODY></HTML>")%r(HTTPOptions,157,"HTTP/1\.1\x20302\x20Move
SF:d\x20Temporarily\r\nConnection:\x20close\r\nContent-Type:\x20text/html;
SF:\x20charset=utf-8\r\nContent-Length:\x2054\r\nDate:\x20Sat,\x2006\x20Ju
SF:l\x202024\x2000:43:11\x20GMT\r\nExpires:\x200\r\nCache-Control:\x20no-c
SF:ache\r\nX-Content-Type-Options:\x20nosniff\r\nX-XSS-Protection:\x201;\x
SF:20mode=block\r\nServer:\x20PRTG\r\nLocation:\x20/index\.htm\r\n\r\n<HTM
SF:L><BODY><B>302\x20Moved\x20Temporarily</B></BODY></HTML>")%r(RTSPReques
SF:t,157,"HTTP/1\.1\x20302\x20Moved\x20Temporarily\r\nConnection:\x20close
SF:\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x20
SF:54\r\nDate:\x20Sat,\x2006\x20Jul\x202024\x2000:43:11\x20GMT\r\nExpires:
SF:\x200\r\nCache-Control:\x20no-cache\r\nX-Content-Type-Options:\x20nosni
SF:ff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nServer:\x20PRTG\r\nLocat
SF:ion:\x20/index\.htm\r\n\r\n<HTML><BODY><B>302\x20Moved\x20Temporarily</
SF:B></BODY></HTML>")%r(FourOhFourRequest,196,"HTTP/1\.1\x20302\x20Moved\x
SF:20Temporarily\r\nConnection:\x20close\r\nContent-Type:\x20text/html;\x2
SF:0charset=utf-8\r\nContent-Length:\x2054\r\nDate:\x20Sat,\x2006\x20Jul\x
SF:202024\x2000:43:11\x20GMT\r\nExpires:\x200\r\nCache-Control:\x20no-cach
SF:e\r\nX-Content-Type-Options:\x20nosniff\r\nX-XSS-Protection:\x201;\x20m
SF:ode=block\r\nServer:\x20PRTG\r\nLocation:\x20/public/login\.htm\?loginu
SF:rl=%2Fnice%20ports%2C%2FTrinity\.txt\.bak&errorid=0\r\n\r\n<HTML><BODY>
SF:<B>302\x20Moved\x20Temporarily</B></BODY></HTML>")%r(SIPOptions,C0,"HTT
SF:P/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\nContent-Type
SF::\x20text/html;\x20charset=utf-8\r\nContent-Length:\x2048\r\nDate:\x20S
SF:at,\x2006\x20Jul\x202024\x2000:43:51\x20GMT\r\n\r\n<HTML><BODY><B>400\x
SF:20Bad\x20Request</B></BODY></HTML>");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

NSE: Script Post-scanning.
Initiating NSE at 20:44
Completed NSE at 20:44, 0.00s elapsed
Initiating NSE at 20:44
Completed NSE at 20:44, 0.00s elapsed
Initiating NSE at 20:44
Completed NSE at 20:44, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 108.45 seconds
```



## tcp flags to hex
Taken from Johnny
| TCP Flag | Hexadecimal | Description | Wireshark Filter Equivalent          |
|----------|-------------|-------------|-------------------------------------|
| flag | HEX | How to use HEX : `tcp.flags == HEX` | `tcp.flag == 0x10` | 
| FIN      | 0x01        | Finish flag - indicates end of data transmission. | `tcp.flags.fin == 1`                |
| SYN      | 0x02        | Synchronize flag - used to initiate a connection. | `tcp.flags.syn == 1`                |
| RST      | 0x04        | Reset flag - resets the connection.   | `tcp.flags.reset == 1`              |
| PSH      | 0x08        | Push flag - pushes buffered data to the receiving application. | `tcp.flags.push == 1`               |
| ACK      | 0x10        | Acknowledgment flag - acknowledges receipt of data. | `tcp.flags.ack == 1`                |
| URG      | 0x20        | Urgent flag - indicates urgent data. | `tcp.flags.urg == 1`                |
| ECE      | 0x40        | ECN-Echo flag - used for explicit congestion notification. | `tcp.flags.ecn == 1`                |
| CWR      | 0x80        | Congestion Window Reduced flag - indicates sender has reduced its congestion window. | `tcp.flags.cwr == 1`                |
