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
                                                                             

┌──(student㉿kali)-[~/Documents/python_scripts/server_client]
└─$ sudo iptables -L -n
```bash
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy DROP)
target     prot opt source               destination         
DOCKER-USER  0    --  0.0.0.0/0            0.0.0.0/0           
DOCKER-ISOLATION-STAGE-1  0    --  0.0.0.0/0            0.0.0.0/0           
ACCEPT     0    --  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
DOCKER     0    --  0.0.0.0/0            0.0.0.0/0           
ACCEPT     0    --  0.0.0.0/0            0.0.0.0/0           
ACCEPT     0    --  0.0.0.0/0            0.0.0.0/0           

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         

Chain DOCKER (1 references)
target     prot opt source               destination         

Chain DOCKER-ISOLATION-STAGE-1 (1 references)
target     prot opt source               destination         
DOCKER-ISOLATION-STAGE-2  0    --  0.0.0.0/0            0.0.0.0/0           
RETURN     0    --  0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-ISOLATION-STAGE-2 (1 references)
target     prot opt source               destination         
DROP       0    --  0.0.0.0/0            0.0.0.0/0           
RETURN     0    --  0.0.0.0/0            0.0.0.0/0           

Chain DOCKER-USER (1 references)
target     prot opt source               destination         
RETURN     0    --  0.0.0.0/0            0.0.0.0/0     
```
