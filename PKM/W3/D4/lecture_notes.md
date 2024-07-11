[Python cert up for grabs, fuck its 200$](https://pythoninstitute.org/pcpp1)

[Best Tips for Monitoring and Filtering Your Web Server Logs](https://www.papertrail.com/solution/tips/best-tips-for-monitoring-and-filtering-your-web-server-logs/)

Importance of Web Server Logs:
> Logs are crucial for identifying errors, optimizing performance, and enhancing user experience.
> They provide insights into server activities like requests, errors, and traffic patterns.

Monitoring Apache Server Logs:
> Apache logs are typically located in `/var/log/apache/` or similar paths.
Use tail -f to monitor logs in real-time:

```bash
sudo tail -f /var/log/apache2/error.log
```
Use egrep to filter out unwanted log entries:

```bash
tail -f /var/log/apache2/error.log | egrep -v "(.gif|.jpg|.png|.swf|.ico)"
```
Use grep to search for specific entries (e.g., errors containing "syntax error"):

```bash
grep "syntax error" /var/log/apache2/error.log
```
Monitoring NGINX Server Logs:
> NGINX logs are typically found in `/var/log/nginx/`
View log contents with cat:
```bash
cat /var/log/nginx/error.log
```
Filter logs using grep:
```bash
grep "syntax error" /var/log/nginx/error.log
```
