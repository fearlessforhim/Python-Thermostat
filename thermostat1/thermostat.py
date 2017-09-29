#!/usr/bin/python

import json_file_reader as file_reader
import status_writer as w
import time
from log import Log
import copy
import scheduler as schedule

class Thermostat:
    def run(self, f, r):
        l = Log()
        flex_temperature = .5

        while True:
            
            data = file_reader.read_json('settings.json')

            target_temperature = schedule.get_scheduled_target_temperature(data)

            if "temporary_temperature" in data and data["temporary_temperature"] is not None:
                print "Temporary target temperature is set"
                target_temperature = data["temporary_temperature"]

            current_temperature = None
            while current_temperature is None:
                current_temperature = r.read_value()

            w.write_value("temperature", current_temperature)
                
            should_run_heat = data["heat"]
            should_run_fan = data["fan"]
            print "Current temperature is : ", current_temperature
            print "Target temperature is : ", target_temperature
            print "Furnace heat setting is on: ", should_run_heat
            print "Furnace fan setting is on: ", should_run_fan

            if should_run_heat:
                if current_temperature > (target_temperature + flex_temperature):
                    if f.is_heat_on:
                        f.is_heat_on = False
                        print "Furnace has been turned off"
                elif current_temperature <= (target_temperature - flex_temperature):
                    if not f.is_heat_on:
                        f.is_heat_on = True
                        print "Furnace has been turned on"
            else:
                f.is_heat_on = False

            f.is_fan_on = should_run_fan

            if f.is_heat_on:
                print "Running..."

            print ""
            l.log(target_temperature, current_temperature, f.is_heat_on)
            time.sleep(5)
