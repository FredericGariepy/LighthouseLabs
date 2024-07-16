#!/usr/bin/python3

import threading
import re
import sys

class TriageThread(threading.Thread):
    
    # triage constructor, called when class instantiated 
    def __init__(self, log_line):
        
        # constructor of the parent Thread class
        threading.Thread.__init__(self)
        
        # class var
        self.log_line = log_line.strip()

    # When you call start() on a thread, it automatically calls this run() method
    def run(self):
        self.match_log_line(self.log_line)

    # file write paths | [!] IMPORTANT : CHANGE YOUR PATHS
    urgent_error_log_path='/home/student/Documents/log_storage/error_logs/urgent_error.log'
    standard_error_log_path='/home/student/Documents/log_storage/error_logs/standard_error.log'
    urgent_access_log_path='/home/student/Documents/log_storage/access_logs/urgent_access.log'
    standard_access_log_path='/home/student/Documents/log_storage/access_logs/standard_access.log'
    standard_unknown_log_path='/home/student/Documents/log_storage/unknown_logs/standard_unknown.log'

    # regex parses & formats into dictionary object {?P<key> : value}
    # Regular expressions for parsing Apache error and access logs
    regex_apache2_error_log = r'^(?P<date>\[\w+\s\w+\s\d+\s\d+:\d+:\d+\.\d+\s\d+\])\s(?P<loglevel>\[\w+:\w+\])\s(?P<pid>\[pid\s\d+:tid\s\d+\])\s(?P<message>.*)'
    regex_apache2_access_log =r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<verb>\w+)\s+(?P<path>[^"]+)\s+(?P<protocol>HTTP/[\d\.]+)"\s+(?P<status_code>\d+)\s+(?P<response_size>[^"]\S*)\s+"(?P<referrer>[^"]*)"\s+"(?P<user_agent>[^"]*)'


    # A static method is a method that belongs to the  class  rather than an instance of the class.
    # It doesn't require the self parameter and can be called on the class itself
    @staticmethod
    def regex_parse(regex_expression, log_line):
        match = re.match(regex_expression, log_line)
        return match.groupdict() if match else None

    # thread funciton
    def match_log_line(self, log_line):
        matched = False

        if not matched:
            try:
                access_log_line = self.regex_parse(self.regex_apache2_access_log, log_line)
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
                    #print('access log detected')

                    status_code = access_log_line['status_code']

                    important_status_codes = {'401', '403', '404', '500', '503', '504'}

                    if status_code in important_status_codes:
                        print('urgent log detected')
                        with open(self.urgent_access_log_path, 'a') as f:
                            f.write(log_line + '\n')
                    else:
                        #print('standard log detected')
                        with open(self.standard_access_log_path, 'a') as f:
                            f.write(log_line + '\n')
            except:
                pass

        if not matched:
            try:
                error_log_line = self.regex_parse(self.regex_apache2_error_log, log_line)
                if error_log_line:
                    matched = True
                    #print(error_log_line)
                    #print(error_log_line['date'])
                    #print(error_log_line['loglevel'])
                    #print(error_log_line['pid'])
                    #print(error_log_line['message'])
                    #print('error log detected')

                    if 'error' in error_log_line['loglevel']:
                        print('urgent error log detected')
                        with open(self.urgent_error_log_path, 'a') as f:
                            f.write(log_line + '\n')
                    else:
                        with open(self.standard_error_log_path, 'a') as f:
                            f.write(log_line + '\n')
            except:
                pass

        if not matched:
            with open(self.standard_unknown_log_path, 'a') as f:
                f.write(log_line + '\n')

# This part is to run triage.py standalone
#if __name__ == '__main__':
#    if len(sys.argv) < 2:
#        print("Usage: triage.py <data>")
#        sys.exit(1)
#    
#    log_line = sys.argv[1]
#    triage_thread = TriageThread(log_line)
#    triage_thread.start()
#    triage_thread.join()
