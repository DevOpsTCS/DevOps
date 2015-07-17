#!/bin/bash
if [ $# -eq 0 ];then
    echo "Usage : $0 <IP_ADDRESS>"
else
FILE_PATH="/home/tcs/zabbix-api-integration/zabbix-api"
IP=$1
file="zabbix-conf-$IP"
AUTH=$(awk '/AUTH/ {print $NF}' ${FILE_PATH}/$file)
APPID=$(awk '/APPID/ {print $NF}' ${FILE_PATH}/$file)
HTTPTESTID=$(awk '/HTTPTESTID/ {print $NF}' ${FILE_PATH}/$file)
TRIGGERID=$(awk '/TRIGGERID/ {print $NF}' ${FILE_PATH}/$file)
ACTIONID=$(awk '/ACTIONID/ {print $NF}' ${FILE_PATH}/$file)

sh ${FILE_PATH}/zabbix-delete-action.sh "$AUTH" "$ACTIONID"
sh ${FILE_PATH}/zabbix-delete-trigger.sh "$AUTH" "$TRIGGERID"
sh ${FILE_PATH}/zabbix-delete-web-scenarios.sh "$HTTPTESTID" "$AUTH"
sh ${FILE_PATH}/zabbix-delete-application.sh "$APPID" "$AUTH"
fi
