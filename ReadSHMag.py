## Author: Ginger Mudd
## 2019-06-04
from sense_hat import SenseHat
from datetime import datetime

timestamp = datetime.now()
delay = 2

sense = SenseHat()

def get_sense_data():
    sense_data = []
    sense_data.append ({'Temperature':(round (sense.get_temperature()))})
#    sense_data.append ({'TemperatureH':(round (sense.get_temperature_from_humidity()))})
    sense_data.append ({'Pressure':(round (sense.get_pressure()))})
#    sense_data.append ({'TemperatureP':(round (sense.get_temperature_from_pressure()))})
    sense_data.append ({'Humidity':(round (sense.get_humidity()))})
    sense_data.append ({'Compass North':(round (sense.get_compass()))})
#    sense_data.append ({'Raw':(sense.get_compass_raw())})
#    sense_data.append ({'Raw':(sense.get_gyroscope_raw())})
    sense_data.append(datetime.now())
    return sense_data

while True:
    sense_data = get_sense_data()
    dt=sense_data[-1] - timestamp
    if dt.seconds > delay:
        print(get_sense_data())
        timestamp=datetime.now()