#!/bin/bash
if [ $# -ne 1 ];then
    echo "Usage : $0 <AUTH_ID>"
else
AUTH=${1:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"host.get\",
    \"params\": {
        \"output\": \"extend\",
        \"filter\": {
            \"host\": [
                \"Zabbix server\"
            ]
        }
    },
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
