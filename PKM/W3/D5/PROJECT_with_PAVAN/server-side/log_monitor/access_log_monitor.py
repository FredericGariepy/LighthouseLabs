#!/usr/bin/python3
import datetime
import time

# file paths
monitor_file = '/home/student/Documents/log_storage/access_logs/urgent_access.log'
output_file = '/home/student/Documents/log_monitor_messages/log_monitor_messages.txt'


last_write_time = time.time()
count = 0
while True:
    time.sleep(60)
    count = 0
    current_time = time.time()
    with open(monitor_file, 'r') as file:
        last_5_lines = file.readlines()[-5:]
        for line in last_5_lines:
            # extract  the time stamp from apache2 urgent_access.log
            timestamp_str = line.split('[')[1].split(']')[0]
            log_time = datetime.datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
            log_time_epoch = log_time.timestamp()
            if (log_time_epoch - last_write_time > 0):
                count +=1
        if (count >=5 ):
            with open(output_file, 'a') as out_file:
                out_file.write(f"[INCIDENT TIME : {current_time}] [INCIDENT MESSAGE : 5 NEW ERROR IN LESS THAN 1 MINUTE] [LOG LOCATION : {monitor_file}]\n")
    last_write_time = current_time
