Readings

## Network-monitoring
[Network monitoring assets](https://www.spiceworks.com/tech/networking/articles/network-monitoring-best-practices/):

- Network devices: laptops, mobile devices, printers, routers, switches, and **firewalls**.
- Links: *Links enable devices to communicate* and include **network interfaces** and **physical wiring** such as fiber optic cables.
- Servers: Email servers, web servers, application servers, and data centers are some of the most critical assets of an organization.
- Service providers: from collaboration software such as GSuite to cloud services such as AWS.
[Makes me think of Week 2 Day 3](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) about [shared-responsibility of 3rd party platforms](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D3/lecture%20notes.md#shared-responsibility)

###### Steps involved in typical networking monitoring implementation are:
  #### Discovering and documenting the network :
  every device connected to the network. Every connection *between* these components is mapped.
> Like using [nmap](https://stationx-public-download.s3.us-west-2.amazonaws.com/nmap_cheet_sheet_v7.pdf)

#### Selecting a protocol:
The ‘protocol’ defines how these components feed information to the monitoring tool. The most common protocol is simple network management protocol (SNMP). [SNMP](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W2/D3/Simple%20Network%20Management%20Protocol.md) works by querying devices for information and maintaining them in a management information base (MIB) with unique identifiers. Monitoring tools use this information to assess network health. This querying or ‘pinging’ happens in designated intervals. 

#### Setting the baseline (Normal behavior):
Normal behavior is first established to know what an anomaly is. This means parameters such as CPU utilization threshold are decided on. The optimal intervals for pinging each network component are also established.
Choosing the network segments and components to be monitored: This ensures that the system isn’t overwhelmed at any point in time.


Network Monitoring Advantages

- Spot IoC
- SIEM Security Information Event Management
- complete network visibility 
>  eliminating beaches of unaccounted network devices by cybercriminals
- trigger remedial actions
> Balance load, foresee needed upgrades
- DRP [disaster recovery plan](https://www.spiceworks.com/it-security/vulnerability-management/articles/what-is-disaster-recovery/)

Workflow:
1. Establish baseline network behavior
2. Ensure high availability of the monitoring system
> Often, network monitoring tools themselves are hosted within the same network that they are monitoring
>
> This is in fact the case, in current local VM set-up.

>The easiest and most inexpensive way is to replicate and store all monitor data in an independent data center. The failover can trigger the automatic installation of another network monitor. This system can then be configured to fetch information from this backup in emergencies. 

3. Eliminate potential tool sprawl
- NetOps, network monitoring and streamline network-related operations.
- DevOps, automation and validation of development tasks.
**tool spraw**: handling three to ten tools at a time. highly inefficient.

4. Look out for alert storms
Alert storms occur when alerts are not placed in properly analyzed and strategic places.
>  large enterprises, the most common daisy-chained component is the switch. A failed switch may set off multiple alerts cascading down to each switch in the chain. This is called an alert storm. 
> Too many alerts can cause fatigue and lead the NetOps team to ignore legitimate alerts. Alert storms also distract them from performing other critical operations.

 5. Ensure configuration management ties in with monitoring
> fuck default values

6. Collect data from multiple network devices for a complete picture
>  Each data point, must be analyzed in conjecture with others to see what kind of insights can be derived from them. 

7. Configure and maintain a robust dashboard
-  Visualization

8. Have a documented escalation process in place
- Most incident responses start at the network monitor
[Incident Response](https://www.spiceworks.com/it-security/vulnerability-management/articles/what-is-incident-response/) has a escalation matrix.
> It is a document that defines when an escalation should happen, what processes are to be followed, and who needs to be involved at each level

9. Create reports at each layer of the network
- They validate the existing network
- They highlight historically relevant information
- They expose trends that can be used to reorganize or scale the network
- They provide regulators with proof of compliance




