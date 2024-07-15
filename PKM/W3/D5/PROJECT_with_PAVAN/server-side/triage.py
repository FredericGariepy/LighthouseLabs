#!/usr/bin/python3

# The purpose of this script is to receive raw client logs from server.py
# 1. logs are received
# 2. logs are parsed
# 3. logs are categorized/stored (In the real world, this should be done in a database)

# impports
import sys
import re

if len(sys.argv) < 2:
    print("Usage: triage_script.py <data>")
    sys.exit(1)  # Exit the script with error code

# regex parses & formats into dictionary object {?P<key> : value}
# Regular expressions for parsing Apache error and access logs


regex_apache2_error_log = r'^(?P<date>\[\w+\s\w+\s\d+\s\d+:\d+:\d+\.\d+\s\d+\])\s(?P<loglevel>\[\w+:\w+\])\s(?P<pid>\[pid\s\d+:tid\s\d+\])\s(?P<message>.*)'
regex_apache2_access_log =r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<verb>\w+)\s+(?P<path>[^"]+)\s+(?P<protocol>HTTP/[\d\.]+)"\s+(?P<status_code>\d+)\s+(?P<response_size>[^"]\S*)\s+"(?P<referrer>[^"]*)"\s+"(?P<user_agent>[^"]*)'


#-----------------------------------------------------


# data received from server.py (main loop)
received_data = sys.argv[1]
log_line = received_data.strip()
#-----------------------------------------------------

# Support funtion: Parse with regex and return dictionary object
def regex_parse(regex_expression, log_line):
    match = re.match(regex_expression, log_line)
    if match:
        return match.groupdict()
    else:
        return None
#-----------------------------------------------------




#-----------------------------------------------------

# Main function: match the log line to a regex expression, store it in a file by sub category
def match_log_line(log_line):

    matched = False

    if not matched:
    # Parse as Apache access log (most frequent)
        try:
            access_log_line = regex_parse(regex_expression=regex_apache2_access_log, log_line=log_line)
            if access_log_line:
                matched = True
                ##print(access_log_line)
                #print(access_log_line['IP'])
                #print(access_log_line['timestamp'])
                #print(access_log_line['verb'])
                #print(access_log_line['path'])
                #print(access_log_line['protocol'])
                #print(access_log_line['status_code'])
                #print(access_log_line['response_size'])
                #print(access_log_line['referrer'])
                #print(access_log_line['user_agent'])
        except:
            pass

    if not matched:
    # Parse as Apache error log
        try:
            error_log_line = regex_parse(regex_expression=regex_apache2_error_log, log_line=log_line)
            if error_log_line:
                matched = True
                #print(error_log_line) 
                #print(error_log_line['date'])
                #print(error_log_line['loglevel'])
                print(error_log_line['pid'])
                #print(error_log_line['message'])
        except:
            pass


    if not matched:
        pass
        #print(log_line)

#-----------------------------------------------------
#print(log_line)
match_log_line(log_line)
#-----------------------------------------------------
