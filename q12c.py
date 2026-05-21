# Redis query script that retrieves the last 10 readings for sensor_01 and computes average

import redis
import json 

r=redis.Redis(host='localhost',port=6379,db=0)

sensor_readings=r.lrange('device:sensor_01 readings',-10,-1)

temperature=[json.loads(reading)['value'] for reading in sensor_readings]

if temperature:
    avg_temp=sum(temperature)/len(temperature)
    print(f"Average for sensor_01 :{avg_temp}")
else:
    print("No readings found for sensor_01")    

# Question 12 part d) 
# Redis data type to store only unique ids is Set