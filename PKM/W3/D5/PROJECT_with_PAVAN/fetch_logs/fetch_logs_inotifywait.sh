#!/bin/bash

# directory to monitor
log_dir="/var/log/apache2"

# Function to process new log files
process_log() {
    local log_file="$1"
    tail -n 1 "$log_file"
}

# Monitor log directory for new access.log files, notice the pipe `|`
inotifywait -m -e create -e modify --format '%f' "$log_dir" |
while read -r file; do
    if [[ "$file" == "access.log" ]]; then
        process_log "$log_dir/$file"
    fi
done
