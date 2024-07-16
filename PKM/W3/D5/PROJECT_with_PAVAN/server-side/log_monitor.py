#!/usr/bin/python3
import datetime
import time
import os

def monitor_logs():
    monitor_file = '/Your/path/to/log_storage/access_logs/urgent_access.log'
    output_file = '/Your/path/to/log_monitor_messages/log_monitor_messages.txt'
    
    current_time = time.time()
    print(f"Current Time: {current_time}")

    all_recent = True
    
    with open(monitor_file, 'r') as file:
        last_5_lines = file.readlines()[-5:]
        
        for line in last_5_lines:
            timestamp_str = line.split('[')[1].split(']')[0]
            log_time = datetime.datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
            log_time_epoch = log_time.timestamp()
            
            print(f"Log entry timestamp: {timestamp_str}")
            print(f"Log Time: {log_time}")
            print(f"Log Time (Epoch): {log_time_epoch}")
            
            if current_time - log_time_epoch < 60:
                print("Log entry is within the last 60 seconds.")
            else:
                print("Log entry is older than 60 seconds.")
                all_recent = False
                break
    
    if all_recent:
        print(f"Appending 'LOL' to {output_file}")
        with open(output_file, 'a') as out_file:
            out_file.write("LOL\n")
    else:
        print("Not all entries are recent.")

if __name__ == "__main__":

    monitor_logs()
