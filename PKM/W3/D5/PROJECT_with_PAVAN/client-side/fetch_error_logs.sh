#!/bin/bash
log_dir="/var/log/apache2"
client_script="/home/student/Documents/python_scripts/server_client/client.py"
# Function to process new log files
process_log() {
    local log_file="$1"
    last_line=$(tail -n 1 "$log_file")
    # feed last_line to python client script
    python3 "$client_script" "$last_line"
}
# Monitor log directory for new access.log files
inotifywait -m -e create -e modify --format '%f' "$log_dir" |
while read -r file; do
    if [[ "$file" == "error.log" ]]; then  #change this if condition to change the log fetching type (e.g. error, access)
        process_log "$log_dir/$file"
    fi
done
