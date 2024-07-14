import socket
import sys
import os
def Main():
  host = '0.0.0.0' # listen all interfaces
  port = 4444
  serversocket = socket.socket()
  serversocket.bind((host,port))
  serversocket.listen(1)
  print('Socket listening')


  while True:
     conn,addr = serversocket.accept() # 2
     print("HELLLOOO PAAAAAVVV %s" % str(addr)) 
     
     received = conn.recv(1024).decode('ascii') # receive 1024 bytes
     print(received+"LOLOLOLOLO")

     msg = 'Connecting Established'+ "\r\n"
     conn.send(msg.encode('ascii')) #3
     conn.close()



if __name__ == '__main__':
  Main()
