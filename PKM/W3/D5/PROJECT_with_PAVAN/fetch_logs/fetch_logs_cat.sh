#!/bin/bash

latest_log=$(ls -t /var/log/apache2/access.log* | head -1)
# ls -t : sort by newst time , -1 first line from output.
# now attacks might try to overload the current log rotation size threshold
# why? in order to burry a log file from being reported (i.e. we want the log file to skipped by the log fetching/sending function)

if [ -s "$latest_log" ] && [ -f "$latest_log" ]; then
    cat "$latest_log"
else
    echo "[Error]: NO ACCESS LOGS FOUND OR LOG IS EMPTY"
    exit 1
fi

echo "$latest_log"
echo "here as some logs i fetched. "
echo "Hi my name is jhony and i am a log."
echo "i've also kept track locally, of what log i am sending, leeping count"
echo  "maybe in the future i will also add that information for the central to know"
