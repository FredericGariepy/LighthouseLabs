#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Usage: triage_script.py <data>")
    sys.exit(1)  # Exit the script with an error code

received_data = sys.argv[1]

print("Triage: "+received_data)
# data arrives here from the server.py file (main loop)
# it should be regexed, analyzed, deposited.
                                 
