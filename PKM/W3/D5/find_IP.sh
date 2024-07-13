#!/bin/bash

input_file="$1" # $1 = first arg, so on for following args $2, $3 ...

# check if input file is provided
if [ ! -e "$input_file" ]; then # ! -e meaning: does not exist

    echo "How to use: $0 <input_file>" # $0 = script name

    exit 1 # exit with status 1, status: error
fi

# regex string
regex_ip='([0-9]{1,3}\.){3}[0-9]{1,3}'

# Use grep to find IP addresses and store them in variable
# -E extended, egrep is equivalent. -o Select only match
ips=$(grep -E -o "$regex_ip" "$input_file")

# pass list of IPs, sort, find uniques and -c for count
uniq_ips=$(echo "$ips" | sort | uniq -c)

echo "  count | ip"
