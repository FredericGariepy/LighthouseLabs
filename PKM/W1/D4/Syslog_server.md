# The Syslog Server
The Syslog Server is also known as the *syslog collector or receiver*.

###### Reminder Note
> Syslog uses the User Datagram Protocol (UDP), port 514, to communicate.
>
> Syslog servers **do not send back an acknowledgment** of receipt of the messages

Syslog messages are sent from the generating device to the collector.

The **IP address of the destination syslog server must be configured on the device** itself,
either by command-line or via a conf file. 

Once configured, all syslog data will be sent to that server.
There is no mechanism within the syslog protocol for a different server to request syslog data.


While most Unix implementations and network vendors, like Cisco, have their own barebones syslog collectors,
there are several others available as well.


Paessler’s PRTG monitoring software offers a built-in Syslog Receiver Sensor.
The receiver collects all Syslog messages delivered.
To use the function, the administrator needs to add the Syslog Receiver and then configure the IP address of that server as the destination server
for syslog data on all devices to be monitored.


Once gathered, the dashboard shows:

- The number of received syslog messages per second.
- The number of messages categorized as “warning” per second.
- The number of messages categorized as “error” per second.
- The number of dropped packets per second.
 
The syslog protocol can generate a lot of messages.

Syslog simply forwards messages as quickly as it generates them.

As a result, the *most important ability for a syslog server is*:

-> the ability to properly filter and react to incoming syslog data.


The PRTG Syslog Receiver Sensor offers the ability to set filtering rules.
These rules allow syslog messages to be included or excluded as warnings or errors,
regardless of how they were originally generated on the device.

This filtering ensures that administrators get notified about all the errors they want to know about
without being overwhelmed by less important errors.

## Security
- The syslog protocol offers no security mechanism.

There is no authentication built-in to ensure that messages are coming from the device claiming to be sending them.

There is no encryption to conceal what information is being sent to the server.

It is particularly susceptible to so-called “playback attacks”:

where an attacker generates a previous stream of warnings to illicit a response.

## Device configuration
Most syslog implementations are configurable with respect to which facilities and which severity numbers will generate syslog events that are forwarded to the syslog server.

It is important to configure this properly to avoid flooding the server (and the network) with unnecessary traffic.

For example, *Debug should never be set to send messages except during testing.*

It is advisable to set the syslog parameters to require the highest possible (lowest numbered) facility and severity to minimize traffic. 

While a router error might indicate that an interface is down and thus definitely needs to be reported,
a less important network printer might be configured to only generate syslog traffic for critical events.

## Windows
Windows systems do not implement syslog within the standard Event Log system.
##### The events generated within the Windows logging system can be gathered and forwarded to a syslog server using third-party utilities.
These utilities monitor the Event Log, use the information to create a syslog formatted event,
and forward the events using the standard syslog protocol.

## Limitations
One major limitation of the syslog protocol is that the device being monitoring must be up and running and connected to the network to generate and send a syslog event.

-> A critical error from the kernel facility may never send an error at all as the system goes offline.

In other words,
#### syslog is not a good way to monitor the up and down status of devices.

While syslog is not a good way to monitor the status of networked devices,

-> it can be a good way to monitor the overall health of network equipment.

While network monitoring software like PRTG offers a suite of utilities to watch over a network,
nothing tells an administrator that there is a problem faster than an event log filling up with warnings.
Properly configured syslog monitoring will detect the sudden increase in event volume and severity,
possibly providing notice before a user-detectable problem occurs.

## Security/authorization/auditing
The average corporate network contains numerous devices that no one should be trying to gain access to on an average day.
If a remote switch that only gets logged into once per audit cycle suddenly has daily login attempts (successful or otherwise),
it bears checking out.

On these types of devices, syslog can be set to forward authentication events to a syslog server,
without the overhead of having to install and configure a full monitoring agent.

Syslog also provides a way to ensure that critical events are logged and stored off the original server.
An attacker’s first effort after compromising a system is to cover the tracks left in the log.
Events forwarded via syslog will be out of reach.

## Application monitoring
There are plenty of ways to monitor how an application is running on a server.
However, those monitors can overlook how the application is affecting other processes on the server.
While high CPU or memory utilization is easy enough to detect with other monitors,
logged events can help show more possible issues.

- Is an application continuously trying to access a file that is locked?
- Is there an attempted database write generating an error?

Events like these may go undetected when caused by applications that do a good job of working around errors,
but they shouldn’t be ignored.
Syslog will make sure those logged events get the attention they deserve.

## Syslog as part of overall network monitoring
Complete network monitoring requires using multiple tools.

Syslog is an important pillar in network monitoring because:
- it ensures that events occurring without a dramatic effect do not fall through the cracks.

Best practice is to use a software that combines all the tools to always have an overview of what is happening in the network.
