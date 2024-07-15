> [!IMPORTANT]
> Dependency `sudo apt install inotify-tools`

### CRON
```bash
@reboot /bin/bash /home/student/Documents/bash_scripts/fetch_access_logs.sh &

@reboot /bin/bash /home/student/Documents/bash_scripts/fetch_error_logs.sh &
```
