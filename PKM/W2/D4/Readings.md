Network monitoring assets:

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

