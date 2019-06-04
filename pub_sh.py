## Author: Gihan Gunasekara
## 2019-05-20

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
from sense_hat import SenseHat
from datetime import datetime

Broker = "iot-lab.flinders.edu.au"
Port  = "1883"

pub_topic = "SenseHat1"

#Stimestamp = datetime.now()
#delay = 2

sense = SenseHat()

#Read SenseHat Sensors
def get_sense_data():
    sense_data = []
    sense_data.append ({'Temperature':(round (sense.get_temperature()))})
    sense_data.append ({'Pressure':(round (sense.get_pressure()))})
    sense_data.append ({'Humidity':(round (sense.get_humidity()))})
    sense_data.append(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    return sense_data

#Message when connecting
def on_connect(client, userdata, flags, rc):
    print("Connected with result code"+str(rc))
    client.subscribe(sub_topic)

client = mqtt.Client()
client.on_connect = on_connect
client.connect(Broker, Port, keepalive=60)
client.loop_start()

while True:
    sense_data = [(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),({'Temperature':(round (sense.get_temperature()))}), ({'Pressure':(round (sense.get_pressure()))}), ({'Humidity':(round (sense.get_humidity()))})]
    client.publish("SenseHat1", str((sense_data)))
    print(sense_data)
    time.sleep(60)
     
    
    


