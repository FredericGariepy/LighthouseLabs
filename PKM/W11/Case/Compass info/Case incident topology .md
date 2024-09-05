```mermaid
graph LR

    AttackerC2["Attacker C2 Server<br>138.68.92.163:4444/tcp"]
    AttackerExfil["Attacker Exfiltration Host<br>178.62.228.28"]

    AttackerC2 --> Internet
    AttackerExfil <--> Internet
    Internet[Internet] <--> Firewall
    Firewall <--> Router["Router External<br>134.122.33.221<br>"Router Internal<br>10.10.X.1""]

    Router <--> Switch1[Switch]
    Router <--> Switch2[Switch]
    
    subgraph Production[Production VLAN - 10.10.1.0/24]
        VLANLabel1[VLAN #1]
        Switch1 <--> Webserver["Web Server<br>premiumhouselights.com<br>10.10.1.2<br>22/tcp ssh, 80/tcp http"]
        Switch1 <--> Database["Database<br>10.10.1.3<br>22/tcp ssh, 23/tcp telnet"]
        Switch1 <--> FileServer["File Server<br>IP ?"]
    end
    
    subgraph Employees[Employees VLAN - 10.10.5.0/24]
        VLANLabel2[VLAN #2]:::noBorder
        Switch2 <--> WiFi["Employee WiFi<br>10.10.5.0/24"]
        Switch2 <--> Devices[Employee Devices]
    end
    
    classDef default fill:#fffff,stroke:#333,stroke-width:2px;
    classDef production fill:#ccf7ff,stroke:#ff0000,stroke-width:2px;
    classDef employees fill:#ccccff,stroke:#0000ff,stroke-width:2px;
    classDef attacker fill:#ff9999,stroke:#ff0000,stroke-width:2px;
    class Production production;
    class Employees employees;
    class AttackerC2,AttackerExfil attacker;
```
Case topology.
1. Exposed SSH and HTTP ports on Web Server
2. Telnet on Database (insecure protocol)
3. Unknown File Server IP (potential security gap)
4. Potential for lateral movement between VLANs
5. External attacker C2 and exfiltration servers"]
