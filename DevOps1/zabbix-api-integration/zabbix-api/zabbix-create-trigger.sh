#!/bin/bash
if [ $# -eq 0 ];then
    echo "Usage : $0 <AUTH_ID> <IP_ADDRESS>"
else
AUTH=${1:-NULL}
IP=${2:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"trigger.create\",
    \"params\": {
        \"description\": \"Alert when service is down (Host : $IP)\",
        \"expression\": \"{Zabbix server:web.test.rspcode[NextGen-$IP,Application Home Page].last()}#200 | {Zabbix server:web.test.rspcode[NextGen-$IP,Application NSD Page].last()}#200 | {Zabbix server:web.test.rspcode[NextGen-$IP,Application VLD Page].last()}#200 | {Zabbix server:web.test.rspcode[NextGen-$IP,Application VNFD Page].last()}#200\",
        \"priority\": 3
    },
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
