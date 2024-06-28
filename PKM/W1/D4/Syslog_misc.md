Since an increasing number of organizations are moving to the cloud,
### The need for log management tools and services has never been greater!!

Here are log files of high priority that you should always keep track of.

The log files include:

 - /var/log/messages–Contains most system messages
 - /var/log/secure–Authentication messages
 - /var/log/cron–Logs Cron job activities
 - /var/log/maillog–Mail transactions

There may be some packet loss if there is a large burst of network traffic.
Remeber Syslog operates on UDP.

#### If you have a geographic network:
then you should have a local loghost—at each location– that sends data to the central loghost.

---

## ELK Stack
ELK Stack:
> Open-source solution that offers powerful log management and analytics capabilities through
> Elasticsearch, Logstash, and Kibana.

The ELK Stack consists of three open-source products:
- Elasticsearch
- Logstash
- Kibana

### Elasticsearch
Description:
> A distributed, RESTful search and analytics engine
> capable of storing and searching large volumes of data quickly.

Role in ELK:
- Serves as the centralized storage and search engine for all log data.
- It indexes the log data and makes it searchable in real-time.

### Logstash
Description:
> A server-side data processing pipeline that ingests data from multiple sources simultaneously,
> transforms it, and sends it to a "stash" like Elasticsearch.

Role in ELK:
- Acts as the data collector and processor.
- It can parse, enrich, and normalize log data before forwarding it to Elasticsearch.

### Kibana
Description:
> A data visualization tool that allows you to explore, visualize,
> and share insights from your data stored in Elasticsearch.

Role in ELK:
- Provides a user-friendly web interface to create visualizations like charts and graphs,
- and dashboards for easy monitoring and analysis of log data

---

### Splunk:
> A commercial, feature-rich platform designed for log management,
> monitoring, and data analysis with advanced search, visualization,
> and machine learning capabilities.
