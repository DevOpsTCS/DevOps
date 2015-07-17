#!/bin/bash
if [ $# -eq 0 ];then
    echo "Usage : $0 <IP_ADDRESS>"
else
FILE_PATH="/home/tcs/zabbix-api-integration/zabbix-api"
IP=$1
AUTH=$(sh ${FILE_PATH}/zabbix-get-auth.sh | cut -d, -f2 | cut -d\" -f4)
HOSTID=$(sh ${FILE_PATH}/zabbix-get-hostid.sh "$AUTH" | cut -d, -f3 | cut -d\" -f4)
APPID=$(sh ${FILE_PATH}/zabbix-create-application.sh "$IP" "$AUTH" "$HOSTID" | cut -d, -f2 | cut -d\" -f6)
HTTPTESTID=$(sh ${FILE_PATH}/zabbix-create-web-scenarios.sh "$APPID" "$IP" "$AUTH" "$HOSTID" | cut -d, -f2 | cut -d\" -f6)
TRIGGERID=$(sh ${FILE_PATH}/zabbix-create-trigger.sh "$AUTH" "$IP" | cut -d, -f2 | cut -d\" -f6)
ACTIONID=$(sh ${FILE_PATH}/zabbix-create-action.sh "$AUTH" "Alert when service is down" "$IP" | cut -d, -f2 | cut -d\" -f6) 

echo "AUTH : $AUTH" > $FILE_PATH/zabbix-conf-$IP
echo "HOSTID : $HOSTID" >> $FILE_PATH/zabbix-conf-$IP
echo "APPID : $APPID" >> $FILE_PATH/zabbix-conf-$IP
echo "HTTPTESTID : $HTTPTESTID" >> $FILE_PATH/zabbix-conf-$IP
echo "TRIGGERID : $TRIGGERID" >> $FILE_PATH/zabbix-conf-$IP
echo "ACTIONID : $ACTIONID" >> $FILE_PATH/zabbix-conf-$IP

fi
