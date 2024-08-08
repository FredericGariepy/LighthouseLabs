## Capture filters
host IP-address: limits the capture to traffic originating from and destined to the IP address.
net 192.168.0.0/24: captures all traffic on the subnet.
dst host IP-address: captures packets sent to the specified host.
port 53: captures traffic only on port 53.
port not 53 and not arp: captures all traffic except DNS and ARP traffic.


## Display filters
https://wiki.wireshark.org/DisplayFilters \
The most useful view filter (based on experience) is:

`ip.src==IP-address and ip.dst==IP-address`

This filter shows packets from one computer (ip.src) to another (ip.dst). \
It is also possible to use ip.addr to show packets originating from and destined to an IP address.

`tcp.port eq 25`: will show all traffic on port 25, which is usually SMTP traffic.

`icmp`: will display only ICMP traffic in the capture (it probably pings).

`ip.addr != IP_address`: displays all traffic except traffic to or from the specified computer.

Analysts even create filters to detect specific attacks, such as the following filter to detect Sasser: \
`ls_ads.opnum==0x09` \
https://en.wikipedia.org/wiki/Sasser_(computer_worm)


## Sniffing can be used to:

- Capture sensitive data such as login credentials.
- Listen to chat messages.
- Capture files that were transmitted over a network.
- Follow protocols that are vulnerable to sniffing:
- Telnet
- rlogin
- HTTP
- SMTP
- NNTP
- POP
- FTP
- IMAP





