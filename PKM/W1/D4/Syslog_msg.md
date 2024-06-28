# Syslog Message
## Syslog transmission
Traditionally, Syslog uses the **UDP protocol on port 514** but can be configured to use any port.

In addition, *some devices* will use **TCP 1468** to send syslog data to get confirmed message delivery.

Syslog packet transmission is asynchronous.

What causes a syslog message to be generated is configured within the router, switch, or server itself.

Unlike other monitoring protocols, such as SNMP, there is no mechanism to poll the syslog data.

In some implementations, SNMP may be used to set or modify syslog parameters remotely.

## Syslog message format. Parts: `PRI` `HEADER` `MSG`
The syslog message consists of three parts: 
- PRI (a calculated priority value)
- HEADER (with identifying information)
- and MSG (the message itself).

The PRI data sent via the syslog protocol comes from **two numeric values** that help categorize the message.
1. The **first** is the Facility value. Basically, the **[TYPE]**.

> This value is one of 15 predefined values or various locally defined values in the case of 16 to 23.
> These values categorize the type of message or which system generated the event.

[See value table](https://www.paessler.com/it-explained/syslog)

2. The **second label** of a syslog message categorizes the *importance or severity* of the message in a numerical code from 0 to 7
[See value table](https://www.paessler.com/it-explained/syslog)

#### The values of both labels do not have hard definitions.
> Thus, it is up to the system or application to determine how to log an event
> (for example, as a warning, notice, or something else)
> and on which facility.

Within the same application or service, *lower numbers should correspond to more severe issues* relative to the specific process.

The two values are combined to produce a Priority Value sent with the message. The Priority Value is calculated by multiplying the Facility value by eight and then adding the Severity Value to the result. The lower the PRI, the higher the priority.

### `(Facility Value * 8) + Severity Value = PRI`
 

> In this way, a kernel message receives lower value (higher priority) than a log alert,
>  regardless of the severity of the log alert.
> 
> Additional identifiers in the packet include the hostname, IP address, process ID, app name, and timestamp of the message.
> The actual verbiage or content of the syslog message is not defined by the protocol.
> Some messages are simple, readable text, others may only be machine readable.

Syslog messages are typically no longer than 1024 bytes.

---

## Example of a Syslog message

`<165>1 2017-05-11T21:14:15.003Z mymachine.example.com appname[su] - ID47 [exampleSDID@32473 iut="3" eventSource=" eventID="1011"] BOMAn application log entry...`
 
Parts of the syslog message:

| Part            | Value                                                               | Information                                                                                                    |
|-----------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| PRI             | 165                                                                 | Facility = 20, Severity = 5                                                                                   |
| VERSION         | 1                                                                   | Version 1                                                                                                      |
| TIMESTAMP       | 2017-05-11T21:14:15.003Z                                            | Message created on 11 May 2017 at 09:14:15 pm, 3 milliseconds into the next second                            |
| HOSTNAME        | mymachine.example.com                                               | Message originated from host "mymachine.example.com"                                                          |
| APP-NAME        | su                                                                  | App-Name: "su"                                                                                                |
| PROCID          | -                                                                   | PROCID unknown                                                                                                |
| MSGID           | ID47                                                                | Message-ID: 47                                                                                                |
| STRUCTURED-DATA | [exampleSDID@32473 iut="3" eventSource=" eventID="1011"]            | Structured Data Element with a non-IANA controlled SD-ID of type "exampleSDID@32473", which has three parameters |
| MSG             | BOMAn application log entry...                                      | BOM indicates UTF-8 encoding, the message itself is "An application log entry..."                              |

> To get Facility and Severity from PRI:
> 
> Facility = int(PRI/8)
> 
> Severity = PRI mod 8



