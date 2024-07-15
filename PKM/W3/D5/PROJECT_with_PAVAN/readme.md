> [!IMPORTANT]
> Dependency `sudo apt install inotify-tools`

### CRON
```bash
@reboot /bin/bash /Your/path/to/fetch_access_logs.sh &

@reboot /bin/bash /Your/path/to/fetch_error_logs.sh &
```
