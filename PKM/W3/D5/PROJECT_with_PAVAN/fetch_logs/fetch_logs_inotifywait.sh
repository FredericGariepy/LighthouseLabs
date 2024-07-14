#!/bin/bash
# NOTE:
# 1. this script works.
# 2. this script outputs new lines 

# directory to monitor
log_dir="/var/log/apache2"


#-----Function to process new log files---
process_log() {
    local log_file="$1" #arg 1 passed from monitor
    tail -n 1 "$log_file" # output last line (newest line)
}
# Future improvements: consider 'lags' in inotifywait's calls (i.e. possible* skipping lines due to extremely fast writes)
#----------------------------------------

#---------- Monitoring-------------------
# Monitor log directory for new access.log files, notice the pipe `|`
inotifywait -m -e create -e modify --format '%f' "$log_dir" | # NOTE: monitors (-m) modify and create events (-e). --format affects output
while read -r file; do # read the output of inotifywait
    if [[ "$file" == "access.log" ]]; then # NOTE: call funciton IF file is access.log, in log rotation: this will always be the newest file
        process_log "$log_dir/$file" # call function
    fi
done
#-----------------------------------------
