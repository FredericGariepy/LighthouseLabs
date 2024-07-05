**task**
Research the following common IoCs that affect network baselines and locate,
capture, and cite at least one scenario for each in your PKM:

- Changes in bandwidth utilization
Changes in bandwidth can captured by sensors. Sensors measure bps, Mps, or Gps depending on *what* asset is being monitored.
Noticable changes may indiacate exfiltration of data,or improper application behaviour. IoC and other unusual high bandwidth behaviour can be caught by sensor thresholds.
- Numerous communications sent to sequential sets of IP addresses or port numbers
Port/Device scanning can be an IoC of [Reconnaissance](https://attack.mitre.org/tactics/TA0043/).
Sensors can listen to port status, data transfer speed. A centralized log can correlate multiple interactions initiated from a single source, SRC IP.
- Unusual port number access
port connectivity activities that fall outside baseline can be monitored , e.g. [xfiltration Over Alternative Protoco](https://attack.mitre.org/techniques/T1048/)
- Large quantity of transmission control protocol (TCP) conversations being requested or refused
IN network monitor: protocol monitoring. IoC [Active Scanning](https://attack.mitre.org/techniques/T1595/)
- Large quantity of address resolution protocol (ARP) requests taking place in a short period of time or from a single source host
monitor: ARP request/second, ARP IP SRC, ARP messages /ARP responces.  [Network Sniffing](https://attack.mitre.org/techniques/T1040/)

