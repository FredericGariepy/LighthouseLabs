#!/bin/bash
#Efficiency: inotifywait is generally more efficient than continuously running tail -f with sleep 1 in terms of CPU and I/O usage because it operates on an event-driven model.

log_dir="/var/log/apache2"

# Function to process new log files

process_log() {

    local log_file="$1" # $1 = arg 1, argument passed (this is a file path)

    echo "New log file detected: $log_file"

    # Add your processing logic here (e.g., send to a server, analyze content)

    # this is where the file gets sent to server

}

# Monitor log directory for new files or modifications

# inotifywait = command-line tool that waits for file/dir changes (event based, Linux's inotify interface)

# -m = monitot, run indefinetely.

# -e = Event to monitor (create, modify)

# --format %f = specify the format of inotifywait's output to show filename which triggered event

# | = pipe

inotifywait -m -e create -e modify --format '%f' "$log_dir" |

while read -r file; do

    if [[ -f "$log_dir/$file" ]]; then

        process_log "$log_dir/$file"

    fi

done

# while read -r file =  while loop to read the input i.e; file (output from inotifywait)

# if [[-f log_dir/file ]] =  -f: file exists and file type, log_dir/file =  path_to_apache_logs/file_that_just_changed

# process_log $path/to/$file = this calls the process_log() funciton and passes it the argument 
