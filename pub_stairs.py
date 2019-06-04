#!/usr/bin/env python 
## Author: Kim Hawtin
## 2018-01-15

import os
import os.path
import csv
import time
import datetime

source = "immotion.csv"

def setup():
    print "setup("
    print ")"


def loop():
    while True:
        print ( "loop( " )
        print ( "  " + time.strftime("%H:%M:%S") )
        get_data()
        send_mqtt()
        time.sleep(300)
        print (")")

 
def get_data():
    print("  get_data(")
    if os.path.exists(source):
        # print("Purging old data")
        os.remove(source)
        
    # dates are the day to measure, and the next day; start_date=$DAY, end_date=$DAY+1
    # location is the position in the device list
    # should match the Hub entry in the list
    # position is the counter location
    # type is A or B, we allocate "up"/"down" or "in"/"out"
    # this depends on the stair or door where the counter is installed
    # time on spreadsheet downloaded is "Melbourne time", not local time.
    # this means that looking at our local time in hours and pulling the hour will not allign! grrr
    
    now      = datetime.datetime.now()
    now1     = now + datetime.timedelta(days=1)
    today    = now.strftime("%Y-%m-%d")
    tomorrow = now1.strftime("%Y-%m-%d")
    hour     = format(now.hour, "02d") + ":00:00" 
    hour1     = format(now.hour+1, "02d") + ":00:00" 
    #print "    hour: " + hour
    #print "Today: " + today
    #print "Tomorrow: " + tomorrow

    location = ['1', '3', '5', '6']
    l_name   = ['',  '',  '',  'H1-L5']

    # stair traffic temp storage for this time slot
    data = {}
    data["up"]   = 0
    data["down"] = 0
    data["in"]   = 0
    data["out"]  = 0
    
    for l in location:
        print ("    location: " + l)
        #url = "https://flinders.sensorserver.com.au/export/export_v1.php?interval=hourly\&start_date=" + today + "\&end_date=" + tomorrow + "\&location=" + l
        url = "https://flinders.sensorserver.com.au/export/export_v1.php?interval=all\&start_date=" + today + "\&end_date=" + tomorrow + "\&location=" + l + "\&startTime" + hour + "\&endTime" + hour1
        cmd = "wget -o immotion.log -O immotion.csv " + url
        print( cmd ) # give us the whole URL so we can check the dates are correct
        rc = os.system(cmd)
        if rc > 0:
            exit()

        if os.path.isfile(source):
            with open(source) as csvfile:
                # yes the source file uses semicolons! >.>
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    print( "    date: "+row["Date"]+" time: "+row["Time"] + " status: " + row["Status"] + " location: "+ row["Location Code"]+" type: " + row["Type"]+" count: "+row["Count"]+  " position: " + row["Position"] + " sensor: "+ row["Sensor"])
                    sensor = row["Sensor"]
                    if sensor == "UP":
                        data["up"]   += int(row["Count"])
                    if sensor == "DOWN":
                        data["down"] += int(row["Count"])
                    if sensor == "IN":
                        data["in"]   += int(row["Count"])
                    if sensor == "OUT":
                        data["out"]  += int(row["Count"])
                    if sensor == "UP/IN":
                        data["up"]   += int(row["Count"])
                        data["in"]   += int(row["Count"])
                    if sensor == "DOWN/OUT":
                        data["down"] += int(row["Count"])
                        data["out"]  += int(row["Count"])

        # display what our tally looks like, keeping in mind this is only valid for a single run of this function at the moment
        print( "      in:"+format(data["in"], "04d"))
        print( "     out:"+format(data["out"], "04d"))
        print( "      up:"+format(data["up"], "04d"))
        print( "    down:"+format(data["down"], "04d"))
    print( "  )")
    


def send_mqtt():
    print ("  send_mqtt( not implemented )")


if __name__ == "__main__":
    setup()
    loop()
