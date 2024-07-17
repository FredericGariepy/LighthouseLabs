> [!IMPORTANT]
> In **fetch_error_log.sh**  &  **fetch_access_log.sh** : *change* `client_script=/your/path/to/client.py`

> [!NOTE]
> Here two log fetching solutions. One for error logs, another for access log.
>
> *Run both in background*. They feed to the same client.py file.

client.py gets called from the two .sh scripts in cron bellow
### CRON (as root)
> @reboot /Your/path/to/fetch_access_logs.sh &
>
> @reboot /Your/path/to/fetch_error_logs.sh &
##### These crons must be configured (`crontab -e`) as **Root**, since scripts access /var/log/apache2/
