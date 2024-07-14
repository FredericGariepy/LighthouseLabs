## CLIENT
student@linux-server:~/Documents/python_scripts/server_client$ nc -zv 192.168.56.101 4444

nc: connect to 192.168.56.101 port 4444 (tcp) failed: Connection refused

student@linux-server:~/Documents/python_scripts/server_client$ 

## SERVER
┌──(student㉿kali)-[~/Documents/python_scripts/server_client]
└─$ netstat -tuln | grep 4444

tcp        0      0 127.0.1.1:4444          0.0.0.0:*               LISTEN     
                                                                             
┌──(student㉿kali)-[~/Documents/python_scripts/server_client]
└─$ jobs
[1]  + running    python3 server_backdoor.py
                                                                             

