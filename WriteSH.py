## Author: Gihan Gunasekara
## 2019-05-20

import json
from sense_hat import SenseHat
from datetime import datetime

enco = lambda obj:(
    obj.isoformat()
    if isinstance(obj, datetime)
    or isinstance(obj, date)
    else None )
timestamp = datetime.now()
delay = 2

sense = SenseHat()
                           
def get_sense_data():
    sense_data = []
    sense_data.append(round (sense.get_temperature()))
    sense_data.append(round (sense.get_pressure()))
    sense_data.append(round (sense.get_humidity()))
    sense_data.append(datetime.now())
    return sense_data

while True:
    sense_data = get_sense_data()
    dt=sense_data[-1] - timestamp
    if dt.seconds > delay:
        print(get_sense_data())
        timestamp=datetime.now()
        sense_data = {}
        sense_data['SH_Sensors']=[]
        sense_data['SH_Sensors'].append({
        'Temperature':(round (sense.get_temperature())),
        'Pressure':(round (sense.get_pressure())),
        'Humidity':(round (sense.get_humidity())),
        'Time' :(datetime.now())})
        with open('SH.json', 'a') as outfile:
            json.dump(sense_data, outfile, indent=2, sort_keys=True, default=enco)
