# MQTT+Redis IoT Sensor Data Pipeline

# MQTT Publisher : temperature reading every 2 seconds to the topic
# sensors/temperature in JSON 
import paho.mqtt.client as mqtt
import json
import time

MQTT_BROKER="localhost"
MQTT_PORT=1883

client=mqtt.Client()
client.connect(MQTT_BROKER,MQTT_PORT)

data={
    "device_id":"sensor_01",
    "value":27.5,
    "ts": int(time.time())
}
message=json.dumps(data)

client.publish('sensors/temperature',message)

print("Message sent")