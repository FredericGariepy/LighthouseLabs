## Linux
### FIND maximum number of PID
`cat /proc/sys/kernel/pid_max`

### FIND interpreter
`which <shell>`
> e.g. `which python3 `, `which bash`

### FIND IP addresses to hostnames
`sudo cat /etc/hosts`
> This command will display the contents of the /etc/hosts file, which typically contains mappings of IP addresses to hostnames used for local hostname resolution.

###  `python3 server.py&`
 **`&`** run server in background
#### `Ctr+Z` suspend job, `bg` resume in background.
To put a foreground job back into the background, you can use the Ctrl+Z shortcut to suspend the job, followed by the bg command to resume it in the background.


` ss -tuln | grep "LISTEN"`
 ```
tcp   LISTEN 0      128        127.0.0.1:631        0.0.0.0:*          
tcp   LISTEN 0      4096   127.0.0.53%lo:53         0.0.0.0:*          
tcp   LISTEN 0      70         127.0.0.1:33060      0.0.0.0:*          
tcp   LISTEN 0      151        127.0.0.1:3306       0.0.0.0:*          
tcp   LISTEN 0      128            [::1]:631           [::]:*          
tcp   LISTEN 0      511                *:80               *:*   
```

## Windows
### FIND interpreter
`where <shell>`
> e.g. `where python3 `, `where bash`

