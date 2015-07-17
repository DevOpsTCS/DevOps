#!/bin/bash
if [[ -f /home/tcs/orchestrationUI.log ]] ; then
    rm -rf /home/tcs/orchestrationUI.log
    touch /home/tcs/orchestrationUI.log
fi
size_org=0

#size=$(wc -l < ~/orchestrationUI.log)

while true ; do 
    if [ -f /home/tcs/orchestrationUI.log ];then
        size=$(wc -l < /home/tcs/orchestrationUI.log)
        if [[ $size_org = $size ]] ; then
            echo "size matched"
        else
            log_tail=$(tail -1 /home/tcs/orchestrationUI.log | grep 'Not Found: /')
            if [[ ! -z $log_tail ]]; then
                echo "Need to raise a BUG now"
                sshpass -p tcs@12345 ssh -o StrictHostKeyChecking=no -l tcs 10.138.97.226 "sh -x file.sh $log_tail"
            else
                echo "No need of raising bug"
            fi
            size_org=$(wc -l < /home/tcs/orchestrationUI.log)
        fi
        sleep 10
    fi
done
exit 0
