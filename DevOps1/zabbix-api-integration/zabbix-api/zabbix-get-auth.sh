#!/bin/bash
curl -X POST -H 'Content-Type:application/json' -d'{"jsonrpc": "2.0","method":"user.authenticate","params":{"user":"Admin","password":"zabbix"},"auth": null,"id":0}' http://10.125.155.220/zabbix/api_jsonrpc.php
