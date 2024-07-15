#!/usr/bin/python3

import sys
import re

if len(sys.argv) < 2:
    print("Usage: triage_script.py <data>")
    sys.exit(1)  # Exit the script with error code

LOG_LINE_RegEx = r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<timestamp>.*)\]\s"(?P<verb>[A-Z]+)\s(?P<path>[\w\/\.-]+)\s+(?P<protocol>[\w\/\.]+)"\s(?P<status_code>\d+)\s(?P<response_size>\d+).*'

# data received from server.py (main loop)
received_data = sys.argv[1]

print("Triage: "+received_data)

def regex_parse(log_line):
    match = re.match(LOG_LINE_RegEx, log_line)
    if match:
        return match.groupdict()
    else:
        pass

try:
    log_line = regex_parse(received_data.strip())
    print(log_line['IP'])
    print(log_line['timestamp'])
    print(log_line['verb'])
    print(log_line['path'])
    print(log_line['protocol'])
    print(log_line['status_code'])
    print(log_line['response_size'])

    # use the above to make some logic
except:
    pass
