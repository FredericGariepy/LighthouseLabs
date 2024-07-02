#!/bin/bash

# Function to start tcpdump in the background
start_tcpdump() {
    sudo tcpdump -i eth0 host <ip_address> -w capture.pcap 
    # -i : interface -w: write 
    # The '&' ensures that tcdump PID is captured instead of bg PID
    # Store the PID of the tcpdump process
    TCPDUMP_PID=$!
}

# Function to stop tcpdump
stop_tcpdump() {
    # Kill the tcpdump process
    sudo kill $TCPDUMP_PID
    # Here there should be added a check for the kill status of TCPDUMP_PID
    # Also some kill options dependng on TCPDUMP_PID status
}

# Main script execution
echo "Starting tcpdump capture..."
start_tcpdump # call function

# Execute your command here (replace with your actual command)
echo "Executing command..."
# Here there should be $1 = windows IP/subnet
# Scan for $1

# Stop tcpdump after command execution
echo "Stopping tcpdump..."
stop_tcpdump # call function

echo "Capture complete."
