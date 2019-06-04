#!/usr/bin/env python 
## Author: Ginger Mudd (based on Kim Hawtins original BOM 2018)
## 2019-05-02

import json
from pprint import pprint
import os
import time
import random
import paho.mqtt.client as mqtt

debug = 0
#host  = "iot-lab.flinders.edu.au"
host = "iot-lab.flinders.edu.au"
port  = "1883"

def setup():
    if debug: print "Setup()"
    ## how do we declare a global and do the connection in this scope?
    #mqttc = mqtt.Client(clean_session=True)

    
def loop():
    if debug: print "Loop()"
    while 1:
    
        #cmd = 'wget -o bom.log -O bom.json http://www.bom.gov.au/fwo/IDS60901/IDS60901.94672.json'
        ## uncomment this if you want it to do work
        #os.system(cmd)
        
        data = {}

        with open('suunto.json') as f:
            bomdata = json.load(f)
            
            for event in bomdata["data_records"]["data"]:
                if event["timestamp"] <>10:
                    data["Timestamp"]  = event ["timestamping"]
                    data["altitude"]   = event["altitude"]
                    data["heart_rate"] = event["heart_rate"]
                    data["vertical_speed"]    = event["vertical_speed"]
                    pprint (data)
        
        json_data = json.dumps(data)
        if debug: print "%s:%s" % (host, port)
        mqttc = mqtt.Client(clean_session=True)
        mqttc.connect(host, port=int(port), keepalive=60)
        mqttc.publish("Suunto9", payload=bytes(json_data))
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
