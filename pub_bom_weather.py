#!/usr/bin/env python 
## Author: Kim Hawtin
## 2018-01-15

import json
from pprint import pprint
import os
import time
import random
import paho.mqtt.client as mqtt

debug = 0
host  = "localhost"
port  = "1883"

def setup():
    if debug: print "Setup()"
    ## how do we declare a global and do the connection in this scope?
    #mqttc = mqtt.Client(clean_session=True)

    
def loop():
    if debug: print "Loop()"
    while 1:
    
        cmd = 'wget -o bom.log -O bom.json http://www.bom.gov.au/fwo/IDS60901/IDS60901.94672.json'
        ## uncomment this if you want it to do work
        #os.system(cmd)
        
        data = {}
        
        with open('bom.json') as f:
            bomdata = json.load(f)
            
            for event in bomdata["observations"]["data"]:
                if event["sort_order"] == 0:
                    data["location"] = event ["name"]
                    data["windspeed"]   = event["wind_spd_kmh"]
                    data["humidity"]    = event["rel_hum"]
                    data["pressure"]    = event["press"]
                    data["temperature"] = event["air_temp"]
                    data["Cloud Type"]  = event["cloud"]
                    data["winddirection"] = event["wind_dir"].lower().encode("ascii","ignore")
                    pprint (data)
        
        json_data = json.dumps(data)
        if debug: print "%s:%s" % (host, port)
        mqttc = mqtt.Client(clean_session=True)
        mqttc.connect(host, port=int(port), keepalive=60)
        mqttc.publish("Testmyprogram", payload=bytes(json_data))
        mqttc.disconnect()
        time.sleep(1800)


def finish():
    if debug: print "Finish()"
    #print "Disconnecting..."
    #mqttc.disconnect()
    #print "Ok\n"


if __name__ == "__main__":
    setup()
    loop()
    finish()
