#!/bin/bash
if [ $# -ne 3 ];then
echo "Usage : $0 <IP ADDRESS> <AUTH> <HOST ID>"
else
VMNAME="DevopsUI-${1:-NULL}"
HOSTID=${3:-NULL}
AUTH=${2:-NULL}
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"application.create\",
    \"params\": {
        \"name\": \"$VMNAME\",
        \"hostid\": \"$HOSTID\"
    },
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
