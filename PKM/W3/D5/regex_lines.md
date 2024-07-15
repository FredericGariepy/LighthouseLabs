# Regular expression for parsing Apache error logs

```python
regex_apache2_error_log = r'\[(?P<date>.*?)\] \[(?P<loglevel>.*?)\] \[client (?P<ip>.*?)\] (?P<message>.*)'

regex_ip = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
```
