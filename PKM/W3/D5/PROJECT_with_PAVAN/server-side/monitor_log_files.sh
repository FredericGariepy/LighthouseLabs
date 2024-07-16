#!/bin/bash

# List of files to monitor
files=(
     # file write paths
    '/Your/path/to/log_storage/error_logs/urgent_error.log'
    '/Your/path/to/log_storage/error_logs/standard_error.log'
    '/Your/path/to/log_storage/access_logs/urgent_access.log'
    '/Your/path/to/log_storage/access_logs/standard_access.log'
    '/Your/path/to/log_storage/unknown_logs/standard_unknown.log'
)

# Function to monitor a single file
monitor_file() {
    file="$1"
    echo "Monitoring file: $file"
    inotifywait -m -q -e modify "$file" |
    while read -r directory event filename; do
        echo "File $filename was modified"
        # Add your action here, e.g., trigger another script/function
    done
}

# Loop through the list of files and monitor each one
for file in "${files[@]}"; do
    monitor_file "$file" &
done

# Wait for all background monitoring processes to finish
wait
