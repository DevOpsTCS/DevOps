#!/bin/bash
if [ $# -ne 2 ];then
echo "Usage : $0 <APPID> <AUTH>"
else
APPID=${1:-NULL}
AUTH=${2:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"application.delete\",
    \"params\": [
        \"$APPID\"
    ],
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
