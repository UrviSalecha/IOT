# MQTT Subscriber 
# that receives sensor messages and stores them in Redis using a list per device.
# Limit each list to the last 100 readings using LTRIM

import paho.mqtt.client as mqtt
import json
import redis

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print("Temperature:", data["temperature"])
    print("Humidity:", data["humidity"])

# Redis 
r=redis.Redis(host='localhost', port=6379, db=0)

def on_message(client, userdata,msg):
    data=json.loads(msg.payload.decode())
    device_id=data["device_id"]
    r.rpush(f"device:{device_id}:readings", msg.payload.decode())
    r.ltrim(f"device:{device_id}:readings", -100, -1)

client=mqtt.Client()
client.on_message=on_message
client.connect("localhost",1883)
client.subscribe("sensors/temperature")
client.loop_forever()
