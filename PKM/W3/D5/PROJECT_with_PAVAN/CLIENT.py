#!/usr/bin/python3
import sys
import os
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# change host(server_addr)
server_addr= '192.168.56.101' #server addressse
port = 4444

s.connect((server_addr, port))

# fetch log data 
bash_script='/home/student/Documents/bash_scripts/fetch_acces_logs.sh'
#os.system(bash_script)
output = os.popen(bash_script).read()
print("sending log...")
message=output

s.send(message.encode('ascii')) 

msg = s.recv(1024) # 4   receive

s.close()
print (msg.decode('ascii'))
