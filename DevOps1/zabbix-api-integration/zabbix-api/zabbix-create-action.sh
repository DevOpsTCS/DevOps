#!/bin/bash
if [ $# -ne 3 ];then
echo "Usage : $0 <AUTH> <TRIGGER_NAME> <IP ADDRESS>"
else
AUTH=${1:-NULL}
TRIGGER_NAME=${2:-NULL}
IP=${3:-NULL}
OPERATION_COMMAND="sh -x file.sh ISSUE"
curl -X POST -H 'Content-Type: application/json' -d \
"{
    \"jsonrpc\": \"2.0\",
    \"method\": \"action.create\",
    \"params\": {
        \"name\": \"Trigger_action-$IP\",
        \"eventsource\": 0,
        \"evaltype\": 1,
        \"status\": 0,
        \"esc_period\": 120,
        \"def_shortdata\": \"{TRIGGER.NAME}: {TRIGGER.STATUS}\",
        \"def_longdata\": \"{TRIGGER.NAME}: {TRIGGER.STATUS}\r\nLast value: {ITEM.LASTVALUE}\r\n\r\n{TRIGGER.URL}\",
        \"conditions\": [
            {
                \"conditiontype\": 3,
                \"operator\": 2,
                \"value\": \"$TRIGGER_NAME\"
            },
            {
                \"conditiontype\": 5,
                \"operator\": 0,
                \"value\": 1
            }

        ],
        \"operations\": [
            {
                \"operationtype\": 1,
                \"esc_period\": 120,
                \"esc_step_from\": 1,
                \"esc_step_to\": 1,
                \"evaltype\": 0,
                \"opcommand_hst\": [
                    {
                        \"hostid\": 0
                    }
                ],
                \"opcommand\": {
                    \"command\": \"sshpass -p tcs@12345 ssh -o StrictHostKeyChecking=no -l tcs 10.125.155.220 $OPERATION_COMMAND\",
                    \"type\": 0,
                    \"execute_on\": 1
                    }
            }
        ]
    },
    \"auth\": \"$AUTH\",
    \"id\": 1
}" \
http://10.125.155.220/zabbix/api_jsonrpc.php
fi
#                \"opconditions\": [
#                  {
#                        \"conditiontype\": 14,
#                        \"value\": \"1\",
#                        \"operator\": 0
#                    }
#                ],

