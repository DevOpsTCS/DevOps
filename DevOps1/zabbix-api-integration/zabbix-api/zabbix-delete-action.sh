#!/bin/bash
if [ $# -ne 2 ];then
echo "Usage : $0 <AUTH> <ACTION ID>"
else
AUTH=${1:-NULL}
ACTIONID=${2:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"action.delete\",
    \"params\": [
        \"$ACTIONID\"
    ],
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
