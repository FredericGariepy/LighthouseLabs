#!/usr/bin/python3
import socket
import threading
from triage import TriageThread
import multiprocessing
import subprocess

def start_log_monitor():
    script_path = '/home/student/Documents/python_scripts/log_monitor_script/access_log_monitor.py'
    subprocess.Popen(['python3', script_path], start_new_session=True)

def main():
    # Start the log monitor in a separate process, it will track changes that are started by the logs comming into the server here.
    log_monitor_process = multiprocessing.Process(target=start_log_monitor)
    log_monitor_process.start()

    host = '0.0.0.0'  # listen on all interfaces
    port = 4444 # this port can be changed
    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen(1)
    print('Socket listening...')
    
    while True:
        conn, addr = serversocket.accept()
        received = conn.recv(1024)
        received_data = received.decode('ascii')
        
        # Create and start a new TriageThread for each connection 
        # threads are non-blocking, so this would be the best way to haddle log monitoring at busy times
        triage_thread = TriageThread(received_data)
        triage_thread.start()
        
        conn.close()

if __name__ == '__main__':
    main()
