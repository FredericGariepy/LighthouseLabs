Here's the information formatted in Markdown:

## Main Office
- **1,500 Desktop Computers**: Client machines running Windows 10, used by employees for daily tasks. They are part of the Active Directory domain (DHA.com).

## Servers
- **2 Domain Controllers (DCI, DC2)**: Manage Active Directory services, including authentication and authorization, and replicate directory information between each other for redundancy and load balancing.
- **1 File Server (FSI)**: Stores and manages file data. Users access shared files and folders stored here.
- **1 WSUS Server (WSUSI)**: Windows Server Update Services server that manages and distributes updates for Microsoft products to the client computers in the network.
- **1 DNS Server (DHADNS)**: Resolves domain names to IP addresses for internal network resources and external internet access.

## Branch Office
- **1 Branch Office Server**: Provides local services and resources to branch office users, likely similar to the main office server roles but on a smaller scale.

## Remote Access
- **1 VPN Router**: Facilitates secure remote connections for remote workers to access the main office network.
- **L2TP VPN Client**: Used by remote workers to establish secure VPN connections to the main office network using Layer 2 Tunneling Protocol (L2TP).

## Operating Systems
- **Windows Server 2019 (all servers)**: The server operating system running on all servers, providing core services and applications.
- **Windows 10 (all clients)**: Client operating system running on all desktop computers.

## Software
- **Office 365 (all company-issued computers)**: Cloud-based suite of productivity applications (Word, Excel, Outlook, etc.) used by employees for various tasks.

## Infrastructure
- **Rackspace and AWS Infrastructure**: Cloud services and hosting environments used for various applications, possibly including backups, additional compute resources, or hosting web applications.

## Active Directory
- **Active Directory Domain (DHA.com)**: Centralized directory service that manages users, computers, and other network resources, providing authentication and authorization across the network.

## Load-Balancing and Cluster Management
- **Load-Balancing**: Distributes network or application traffic across multiple servers to ensure no single server becomes overwhelmed, improving performance and reliability.
- **Cluster Management**: Manages a group of servers (cluster) that work together to provide high availability and reliability for services and applications.

## Central Monitoring System
- **Central Monitoring System**: Monitors the health and performance of network infrastructure, servers, and applications, providing alerts and reports on issues or anomalies.
