#!/usr/bin/python3
import socket
import subprocess
#import sys
#import os

# NOTE!: change this path to your triage script path
# path to triage script
path_triage_script='/home/student/Documents/python_scripts/server_client/triage_script.py'

def Main():
  host = '0.0.0.0' # listen all interfaces
  port = 4444
  serversocket = socket.socket()
  serversocket.bind((host,port))
  serversocket.listen(1)
  print('Socket listening...')


  while True:
     conn,addr = serversocket.accept() 
     #print("Accepted connection from  %s" % str(addr)) 
    
     
     received = conn.recv(1024) # received bytes encoded
     #print(f"Received {len(received)} bytes from {str(addr)}")

     received_data=received.decode('ascii') # decoded data | access.log is type <'str'>
     #print(received_data)
     
     #call the triage script with received decoded data
     subprocess.run(['python3', path_triage_script, received_data])

     # SEND ACK
     #msg = 'Connecting Established'+ "\r\n"
     #conn.send(msg.encode('ascii'))
     conn.close()

if __name__ == '__main__':
  Main()
