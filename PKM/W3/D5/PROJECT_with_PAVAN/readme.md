> [!IMPORTANT]
> Dependency `sudo apt install inotify-tools`

### CRON
```bash
@reboot /bin/bash /Your/path/to/fetch_access_logs.sh &

@reboot /bin/bash /Your/path/to/fetch_error_logs.sh &

@reboot /usr/bin/python3 /Your/path/to/server.py &

# >/dev/null 2>&1
# to run in silence, standard out and standard error to /dev/null

```
