#!/usr/bin/python

import temp_reader as Reader
import time
import json
import datetime
from log import Log


class Thermostat:
    def run(self, f):
        l = Log()
        flex_time = .5

        while(True):
            
            day_of_week = str(datetime.datetime.today().weekday())
            
            current_temperature = Reader.get_current_temp()

            data_file = open('settings.json')
            data = json.load(data_file)
            
            print "Current temperature is : ", current_temperature
            
            now = datetime.datetime.now()
            current_hour = now.hour
            current_minute = now.minute

            #print "Current day of week : ", day_of_week
            #print "Current hour : ", current_hour
            #print "Current minute : ", current_minute

            schedules_for_day = data["schedules"][day_of_week]

            target_temperature = 70.0

            latestValidScheduleHour = -1
            latestValidScheduleMinute = -1

            foundLaterSchedule = False
            for sched in schedules_for_day:
                if(sched["start"]["hour"] > current_hour):
                    continue
                elif(sched["start"]["hour"] == current_hour and sched["start"]["minute"] > current_minute):
                    continue
                
                if(sched["start"]["hour"] > latestValidScheduleHour):
                    foundLaterSchedule = True
                elif(sched["start"]["hour"] == latestValidScheduleHour and sched["start"]["minute"] >= latestValidScheduleMinute):
                    foundLaterSchedule = True
                    
                if(foundLaterSchedule):
                    target_temperature = sched["temperature"]
                    latestValidScheduleHour = sched["start"]["hour"]
                    latestValidScheduleMinute = sched["start"]["minute"]
                    foundLaterSchedule = False
                
            print "Target temperature is : ", target_temperature

            if(current_temperature > (target_temperature + flex_time)):
                if(f.is_on):
                    f.is_on = False
                    print "Furnace has been turned off"
            elif (current_temperature <= (target_temperature - flex_time)):
                if(not f.is_on):
                    f.is_on = True
                    print "Furnace has been turned on"

            if(f.is_on):
                print "Running..."

            print ""
            l.log(target_temperature, current_temperature, f.is_on)
            time.sleep(5)
