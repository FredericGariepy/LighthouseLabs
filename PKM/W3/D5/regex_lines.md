# Regular expression for parsing Apache error & access logs

```python
# Regular expressions for parsing Apache error and access logs
regex_apache2_error_log = r'\[(?P<date>.*?)\] \[(?P<loglevel>.*?)\] \[client (?P<ip>.*?)\] (?P<message>.*)'

regex_apache2_access_log =r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<verb>\w+)\s+(?P<path>[^"]+)\s+(?P<protocol>HTTP/[\d\.]+)"\s+(?P<status_code>\d+)\s+(?P<response_size>[^"]\S*)\s+"(?P<referrer>[^"]*)"\s+"(?P<user_agent>[^"]*)'

regex_ip = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

regex_apache2_error_log_other = r'\[(?P<timestamp>(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{2} \d{2}:\d{2}:\d{2} \d{4})\] \[(?P<log_level>\w+)\] (?P<message>.*?)(?:\s*\[|$)'

```
