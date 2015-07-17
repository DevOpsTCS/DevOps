#!/bin/bash
if [ $# -eq 0 ];then
    echo "Usage : $0 <AUTH_ID> <TRIGGER ID>"
else
AUTH=${1:-NULL}
TRIGGERID=${2:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"trigger.delete\",
    \"params\": [
        \"$TRIGGERID\"
    ],
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
