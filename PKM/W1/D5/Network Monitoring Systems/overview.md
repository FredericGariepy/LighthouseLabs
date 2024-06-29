Offical Docs
[Wireshark](https://www.wireshark.org/docs/)

# Network Monitoring System (NMS)

An NMS provides five essential functions:
1. Discover
2. Map
3. Monitor
4. Alert
5. Report

## Discover
NMSs discover the devices on the network, such as:
- routers, switches, firewalls, servers, printers, and running services.

The NMSs can include a library of monitoring templates,
which define which part or how to monitor a device and its services.

All these functions are typically vendor-specific.
For example, when you monitor a Cisco router,
it will be different than when you monitor an Enterasys router,
so when an NMS completes the discovery process,
it automatically assigns an appropriate device role to each discovered device, independent of the brand.

A monitoring system with *Layer 2/3 discovery* will discover
port-to-port connectivity between devices on the network,
including MAC and IP addresses.

For effective network monitoring, more information is needed to know what is working on the network,
and it is important for you to understand how and where everything is connected.

-> Why?

Because a performance issue with one device or a port can affect the performance of another connected device.
For example, when a switch fails, all devices connected to that switch cannot communicate over the network.

## Map
NMSs generate network maps,
a powerful first-response tool that allows network administrators to visualize their networks.
Visualizing your network can save you hours and even days of troubleshooting network issues. 
Unfortunately, network wiring can get complex and messy, 
limiting the network's administrative ability to view the network and preventing troubleshooting.

Many NMSs require significant manual processing to create a network map
but there is some software that provides a drawing tool.
To fully utilize this type of software, a network administrator's knowledge and time will be important
to map the network topology.

## Monitor
NMSs expose network administrators to many monitors and templates.

As a starting point, network administrators want to monitor the five necessary items for any device on the network, such as:
- availability
- latency
-  CPU
-  memory
-  disk
-  interface utilization

Most network monitoring tools, monitor other hardware components such as power supplies, temperature, and fan speed.

When properly configured, an NMS will usually provide a visual dashboard
of how the devices on the network are functioning,
which will provide real-time awareness of failures.
And may provide advance warning of imminent failure.
Visual or audio feedback (flashing lights, colour changes, audible alarms, or text/email warnings)
will alert administrators to the hardware issues that may result in physical failure of the network.

In addition, activity on a device that is outside the scope of its ordinary usage
may indicate an attack or other threat. 
little-used server that suddenly sees a huge spike in its uptime or CPU usage
warrants investigation into the cause of the change in the device's behaviour.

## Alert
The central and essential feature is monitoring and notifying when something goes wrong.

Performance metrics like CPU, memory and interface utilization can fluctuate throughout the day,
but they may exceed the limits by a few seconds or minutes during peak usage periods.
Threshold-based alerting allows network administrators to respond to issues before they impact users,
applications, or the business.

For example, the monitoring system is configured to issue an alert when CPU utilization on a router exceeds 80%,
which allows the network administrator to investigate and respond before the router fails.

## Central Alert Management:
NMSs provide real-time and historical monitoring data to support the lifecycle.
This information allows network administrators to:

- Validate that network projects are delivering desired results.
- Expose trends that could impact the network's ability to deliver the performance required by users,
  applications and businesses.
- Quickly isolate and fix performance issues.
- Prove the availability of the network and the connected devices.

##### TIP:
> Most NMSs are customizable,
> and you can create profile-based dashboards for managers,
> line-of-business owners, Help Desk, and applications.
>
> NMSs differ in their capabilities for each function, but they have the same result.

## How Network Monitoring Tools Collects Information
Network monitoring tools collect information on the network by

-> using poll connection over the network devices and servers.

They receive information about the performance data using standard protocols such as:
- Agents: using specific agents in the case of servers
- SNMP
- Windows Management Instrumentation (WMI)
  > WMI implementation is a proprietary protocol for Windows-based systems and applications
  > of Web-Based Enterprise Management, a software industry initiative to develop a standard
  > for accessing management information across the enterprise.
  >
  > This protocol creates an OS interface that receives information from devices running a WMI agent.
  > WMI gathers details about the OS, hardware or software data,
  > the status and properties of remote or local systems,
  > configuration and security information, and process and service information.
  >
  > It then passes all these details to the network management software,
  > which monitors the network's health, performance, and availability.
- Sniffing the traffic and flow of pieces of information
- Remote SSH for Unix and Linux servers


#### `Warning` WMI
Microsoft has changed its policy regarding the code it uses to execute WMI,
which is important if PowerShell is being used.
There is no indication what the PowerShell users should be aware of.
**Some** *WMI commands in PowerShell are no longer supported*,
and they *should be replaced with CIM cmdlets (commandlets) code*.

## Monitoring the Network with Wireshark
Wireshark allows the user to analyze packets transmitted over the network,
displaying the information in detail in a graphical interface.
With this, it is possible to identify, with more details about everything that happens
in the data exchange between the client and host.

-> The program's *graphical interface is the main difference between **Wireshark** and the **TCPDUMP** (command-line interface)* tool.

​​*TCPDUMP provides the same details* of network packet information while
Wireshark simply presents the data in a dashboard visual
TCPDUMP is included in the OS as a command-line tool, meaning it's free to use.

###### Note:
> -> Network administrators can therefore choose which option suits their style and budget.

Wireshark offers a series of facilities depending on the user's knowledge level rather than the graphic resources.
You can also run it using command lines.
Both solutions use the same library (**libpcap**),
which is specialized for capturing and sending packets or files over a network.
Therefore, *Wireshark supports TCPDUMP capture documents*.

With a wide range of functionalities and features, Wireshark has boost functionality, such as:
- Real-time data reading:
  > All packet contents sent/received by the server are captured in real time by Wireshark.
  > User interaction with your network can be monitored anytime.
  > This is an essential feature for tracking suspicious events.
- vailability and interoperability for multiple OSs:
  > All popular OSs like Linux, Mac and Windows have a compatible version of Wireshark.
  > ###### Note:
  > > The tool is also available for FreeBSD, NetBSD, Solaris, HP-UX, etc.
- Applying Filters:
  > Easy and intuitive filters to understand the total traffic and network communication.
  > Among the most remarkable things you can do in Wireshark is to apply content filters.
  > All you have to do through them is type the terms following a syntax or use certain filters that make the process easier.
---
### Here are five practical examples of how to inspect traffic closely.

#### Example 1 (Filter ip.src ip.dst)
If you wanted to filter packets by source/destination IP or monitor traffic from an IP address

In Wireshark, we can do this via the source and/or destination IP, as per the examples:
`ip.src==192.168.1.15`
`ip.dst==192.168.16.69`

###### Note
> There is a handy filter to refine the search, restricting it to local network traffic,
>  thus reducing the amount of information displayed in the results.

Wireshark screen indicating display filters go in the text bar above the captured packets list
A green display filter bar indicates a successful filter.

### Example 2 (subnets, and)
Below, we apply the conditional and, as a reference, the IP 192.168.0.0/24 common in local networks.
`ip.src==192.168.1.0/24 and ip.dst==192.168.16.0/24`

### Example 3 (contains)
Suppose you are looking for a particular package in an extensive set of packages.
To find strings over the packet:
Wireshark will identify the packages that contain the string to confirm the existence and check the inner contents of the packet.

Knowing that the URL of our blog is present in the transaction, you can use it as a reference by typing:

`http contains "www.lighthouselabs.ca"`

### Example 4 (TCP UDP)
To filter packets from TCP or UDP ports:
Searching for packets using as a reference a port (TCP or UDP) used in the manipulation is very simple.

In the example below, you use the filter port:

`tcp. port==357`
`udp. port-=4113`

### Example 5 (|| or)
Monitor traffic on Apache and MySQL networks: Wireshark allows us to condition the use of resources.

In a network installed by the LAMP suite, for example,
know the corresponding server networks by the LAMP and web database (MySQL or MariaDB).
`tcp.port==80 || tcp.port==3306`
