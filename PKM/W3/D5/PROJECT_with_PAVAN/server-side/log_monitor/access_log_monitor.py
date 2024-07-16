#!/usr/bin/python3
import datetime
import time
import os

# file paths
monitor_file = '/home/student/Documents/log_storage/access_logs/urgent_access.log'
output_file = '/home/student/Documents/log_monitor_messages/log_monitor_messages.txt'

def monitor_logs():
    while True:
        current_time = time.time()
        all_recent = True
        
        with open(monitor_file, 'r') as file:
            last_5_lines = file.readlines()[-5:]
            
            for line in last_5_lines:
                # extract  the time stamp from apache2 urgent_access.log
                timestamp_str = line.split('[')[1].split(']')[0]
                log_time = datetime.datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
                log_time_epoch = log_time.timestamp()
                
                if current_time - log_time_epoch > 60:
                    all_recent = False
                    break
        
        if all_recent:
            with open(output_file, 'a') as out_file:
                out_file.write(f"[INCIDENT TIME : {current_time}] [INCIDENT MESSAGE : 5 NEW ERROR IN LESS THAN 1 MINUTE] [LOG LOCATION : {monitor_file}]\n")
        
        time.sleep(60)

if __name__ == "__main__":
    monitor_logs()
