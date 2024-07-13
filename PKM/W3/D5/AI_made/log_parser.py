# MADE BY AI (CHATGPT3.5)
#V 0
import re
import sys

# Check if a filename was provided as a command-line argument
if len(sys.argv) < 2: #sysarg0 is @script
    print("Usage: python script.py <log_file_name>") # how to use the file
    sys.exit(1)

# Get the log file name from the command-line argument
log_file_name = sys.argv[1]

# Regular expression to match Apache2 log file names
# Typically in the format: access.log, access.log.1, access.log.2.gz, etc.
log_file_pattern = r'^(access|error)\.log(\.\d+)?(\.gz)?$'

# Check if the provided filename matches the Apache2 log file pattern
if not re.match(log_file_pattern, log_file_name):
    print(f"Error: '{log_file_name}' does not appear to be a valid Apache2 log file name.")
    sys.exit(1)

print(f"Processing log file: {log_file_name}")

# Rest of your log parsing code goes here
log_pattern = r'(?P<ip>\S+) (?P<user>\S+) (?P<userid>\S+) \[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status>\d+) (?P<size>\d+)'

# Example of reading from the file (you'd need to handle gzip files separately)
try:
    with open(log_file_name, 'r') as log_file:
        for log_line in log_file:
            match = re.match(log_pattern, log_line.strip())
            if match:
                log_data = match.groupdict()
                print(log_data)
except FileNotFoundError:
    print(f"Error: File '{log_file_name}' not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to read '{log_file_name}'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
