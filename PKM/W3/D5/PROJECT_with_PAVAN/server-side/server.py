#!/usr/bin/python3
import socket
import threading

from triage import TriageThread


def main():
    host = '0.0.0.0'  # listen on all interfaces
    port = 4444
    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen(1)
    print('Socket listening...')

    while True:
        conn, addr = serversocket.accept()
        received = conn.recv(1024)
        received_data = received.decode('ascii')
        
        # Create and start a new TriageThread for each connection
        triage_thread = TriageThread(received_data)
        triage_thread.start()
        
        conn.close()

if __name__ == '__main__':
    main()
