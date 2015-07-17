#!/bin/bash
if [ $# -ne 2 ];then
echo "Usage : $0 <HTTPTESTID> <AUTH>"
else
HTTPTESTID=${1:-NULL}
AUTH=${2:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"httptest.delete\",
    \"params\": [
        \"$HTTPTESTID\"
    ],
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
