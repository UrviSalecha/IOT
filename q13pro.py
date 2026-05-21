# Kafka Producer log processing pipeline
# A) read lines from a log file and each line as a message to topic app-logs

from kafka import KafkaProducer
import time

# Producer
producer=KafkaProducer(bootstrap_servers='localhost:9092')

with open('app.log','r') as f:
    try:
        for line in f:
            producer.send('app-logs',line.encode('utf-8'))
            time.sleep(1)
            break
    except FileNotFoundError:
        print("File not found")
