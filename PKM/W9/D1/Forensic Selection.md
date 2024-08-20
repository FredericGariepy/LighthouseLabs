## Key Takeaways
- IoCs are the first point of defense for forensics.
- Threat intelligence can provide insight into what should be monitored.
- Monitoring should be tailored to the environment and operating capacity of the client.


## data types for forensic
1. __File System Data__: on hard/flash drives, file, folder, directories (metadata, timestamp, sizes, permissions)
2. __Registry data__: system settings, user preferences, and application configurations.
3. __Internet history__: history, cookies, search queries, others.
4. __Email and messaging data__ : email message, instant message, mesages header, etc.
5. __Network traffic__: IP addresses, ports, protocols, packet payloads.
6. __Cloud data__: data stored in cloud-based services, such as email, file storage, and collaboration tools, adding additional nuances to the investigation

Data collected can vary, may involve PII.

## Making IoC selections
- __Relevance__: IoCs should be relevant to organization security posture & threats it faces
- __Effectiveness__: effective at indentifying incidents
- __Scalability__: monitoring solution should be scalable
- __Cost__: cost-effective monitoring with goood ROI.

Selection criteria for forensic investigation:
- IoCs: malware e.g. signatures (reported hash)
- Vulnerabilties: e.g. Automated tests, reported/discovered vulnerability
- Threat intelligence: e.g. TTP, Actor profiles (APTs), CTI 


