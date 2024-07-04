
## (SNMP) [Simple Network Management Protocol](https://www.paessler.com/it-explained/snmp)
It is a protocol for management information transfer in networks,
for use in LANs especially, depending on the chosen version.

## Versions
Currently, there are three major versions of SNMP.

The first version was developed rather quickly in the late ´80s when network administration lacked suitable network administration tools that were not dependent on hardware manufacturers.

SNMP v1 was defined in 1988 and was based on SGMP (RFC 1028).
> Then, it was broadly accepted and used. It is still used today, almost 30 years later, which is nearly an eternity in IT. SNMP v1 provides the basic functionalities for data polling and is relatively easy to use. It doesn't create much overhead because it doesn't include any encryption algorithms. So, for security reasons, use SNMP v1 in LANs only. Its biggest limitation is its 32-bit counter architecture, which is not enough for today’s gigabyte networks or larger.

If users want to manage networks in a WAN, the CMISE/CMIP protocol is the right protocol to go for.

SNMP v2 supports 64-bit counters but still sends critical data as clear text, so it does not really enhance security. And if users come across SNMP v2, it is mostly "SNMP v2c" that manufacturers or networkers are talking about, with the "c" standing for "community". Two other SNMP v2 versions exist, SNMP v2p and SNMP v2u, but they are only implemented in rare cases.
