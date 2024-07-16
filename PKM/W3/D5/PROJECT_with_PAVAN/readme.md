> [!IMPORTANT]
> Dependency `sudo apt install inotify-tools`

### CRON
```bash
@reboot /Your/path/to/server.py &
* * * * * /Your/path/to/log_monitor.py

#Optional
# >/dev/null 2>&1
# to run in silence, standard out and standard error to /dev/null

```
