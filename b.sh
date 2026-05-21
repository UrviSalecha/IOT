# Bash Script to check whether consumer process is running 
# restart if not found # logging with a timestamp to monitor.log file 
# repeats this check every 30 minutes
# for this we will follow the following steps :
# As per my windows :
# 1. I will use the docker desktop 
# run the container in my case container name is " mystifying_haibt"
# Open terminal
# docker exec -it mystifying_haibt bash 
# container running 
# now apt update nano
# touch monitor.log
# nano monitor.sh
# nano command helps to write the code in the bash file 
# in bash file 

#!/bin/bash
# write the code as 
while true; do
    if ! pgrep -x "consumer" > /dev/null
    then 
        echo "$(date): Consumer not found" >> monitor.log
        # resatrt of not found
        # command to restart the consumer process
        # we can call it
        retart_consumer_command
    else
        echo "$(date): Consumer is running" >> monitor.log
    fi
    sleep 1000 
done

# then in terminal write chmod 777 monitor.sh
# run using ./monitor.sh

