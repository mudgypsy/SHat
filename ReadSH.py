## Author: Gihan Gunasekara
## 2019-05-20
from sense_hat import SenseHat
from datetime import datetime

timestamp = datetime.now()
delay = 2

sense = SenseHat()

def get_sense_data():
    sense_data = []
    sense_data.append ({'Temperature':(round (sense.get_temperature()))})
    sense_data.append ({'Pressure':(round (sense.get_pressure()))})
    sense_data.append ({'Humidity':(round (sense.get_humidity()))})
    sense_data.append(datetime.now())
    return sense_data

while True:
    sense_data = get_sense_data()
    dt=sense_data[-1] - timestamp
    if dt.seconds > delay:
        print(get_sense_data())
        timestamp=datetime.now()