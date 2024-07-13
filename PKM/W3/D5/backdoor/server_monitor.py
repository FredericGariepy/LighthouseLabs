# SERVER SIDE MONITOR
import socket
def Main():
  host = socket.gethostname()
  port = 4444
  serversocket = socket.socket()
  serversocket.bind((host,port))
  serversocket.listen(1)
  print('Socket listening')


  while True:
     conn,addr = serversocket.accept()
     print("Got connection from %s" % str(addr))
     msg = 'Connecting Established'+ "\r\n"
     conn.send(msg.encode('ascii'))
     conn.close()
if __name__ == '__main__':
  Main()
