#! /usr/bin/python 
from sense_hat import SenseHat
import time
sense = SenseHat()
temp = sense.get_temperature()
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temperature is %d C Humidity is %d percent Pressure is %d mbars' %(temp,humidity,pressure)
sense.show_message(message,scroll_speed=(0.08),text_colour=[200,0,200],back_colour=[0,0,200])
print(message)
