#!/bin/bash
if [ $# -ne 4 ];then
echo "Usage : $0 <APP ID> <IP ADDRESS> <AUTH> <HOST ID>"
else
APPID=${1:-NULL}
HOSTID=${4:-NULL}
HOSTURL="http://${2:-NULL}:1234"
AUTH=${3:-NULL}

curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"webcheck.create\",
    \"params\": {
        \"name\": \"NextGen-${2:-NULL}\",
        \"applicationid\": \"$APPID\",
        \"hostid\": \"$HOSTID\",
        \"delay\":\"5\",
        \"agent\":\"Mozilla 5.0 (X11; Linux i686; rv:8.0) Gecko 20100101 Firefox 8.0\",
        \"steps\": [
            {
                \"name\": \"Application Home Page\",
                \"url\": \"$HOSTURL\",
                \"status_codes\": 200,
                \"no\": 1
            },
            {
                \"name\": \"Application VLD Page\",
                \"url\": \"$HOSTURL/vld\",
                \"status_codes\": 200,
                \"no\": 2
            },
            {
                \"name\": \"Application VNFD Page\",
                \"url\": \"$HOSTURL/vnfd\",
                \"status_codes\": 200,
                \"no\": 3
            },
            {
                \"name\": \"Application NSD Page\",
                \"url\": \"$HOSTURL/nsd\",
                \"status_codes\": 200,
                \"no\": 4
            }
        ]
    },
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
