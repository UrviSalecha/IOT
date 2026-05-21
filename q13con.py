# Kafka Consumer consumes from app-logs topic filters noly line containg the keyword ERROR
# appends them to errors_only.log file
from kafka import KafkaConsumer

consumer=KafkaConsumer('app-logs',bootstrap_servers='localhost:9092')

with open('errors_only.log','a') as f:
    for message in consumer:
        line=message.value.decode('utf-8')
        if 'ERROR' in line:
            f.write(line)

f.close()
# Bash Script to check whether consumer process is running 
# restart if not found # logging with a timestamp to monitor.log file 
# repeats this check every 30 minutes