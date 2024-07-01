#!/bin/bash

# Function to start tcpdump in the background
start_tcpdump() {
    sudo tcpdump -i eth0 host <ip_address> -w capture.pcap &
    # Store the PID of the tcpdump process
    TCPDUMP_PID=$!
}

# Function to stop tcpdump
stop_tcpdump() {
    # Kill the tcpdump process
    sudo kill $TCPDUMP_PID
}

# Main script execution
echo "Starting tcpdump capture..."
start_tcpdump

# Execute your command here (replace with your actual command)
echo "Executing command..."
# Example command execution
nmap -sS

# Stop tcpdump after command execution
echo "Stopping tcpdump..."
stop_tcpdump

echo "Capture complete."
