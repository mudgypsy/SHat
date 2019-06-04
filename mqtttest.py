import json
from pprint import pprint
import os
import time
import random
import paho.mqtt.client as mqtt

broker = "iot-lab.flinders.edu.au"
port  = "1883"

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("Connected OK")
        print(client.client_id)
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True

mqtt.Client.connected_flag=False#create flag in class
mqtt.Client.bad_connection_flag=False #
broker="iot-lab.flinders.edu.au"
client = mqtt.Client("python1")             #create new instance 
client.on_connect=on_connect  #bind call back function
client.loop_start()
print("Connecting to broker ",broker)
client.connect(broker, port)      #connect to broker
try:
    client.connect(broker,port) #connect to broker
except:
    print("Connection failed")
while not client.connected_flag and not client.bad_connection_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
if client.bad_connection_flag:
    client.loop_stop()    #Stop loop
    sys.exit()
print("in Main Loop")
client.loop_stop()    #Stop loop 
client.disconnect() # disconnect