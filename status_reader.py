#!/usr/bin/python

import json_file_reader as R
import sys
import Adafruit_MCP9808.MCP9808 as MCP9808
import time
import math
import RPi.GPIO as GPIO
from log import Log

class Reader:

    def __init__(self):
        pass

    current_temp = 0

    def read_value(self):
        return self.current_temp
    
    def execute(self):
        log = Log()
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        sensor = MCP9808.MCP9808()
        sensor.begin()
        
        while True:
            temperature_sum = 0
            avg_temperature = 0
            polls = 20
            temperature_list = []
            i = 0
            
            while i < polls:
                try:
                    temperature_c = sensor.readTempC()
                    temperature_list.append(temperature_c)
                    i += 1
                    time.sleep(1)
                except IOError as ex:
                    log.log(str(ex))
                
            j = 0
            
            while j < polls:
                temperature_sum += temperature_list[j]
                j += 1
            avg_temperature = temperature_sum/polls
            
            k = 0
            
            accepted_temperature_count = 0;
            accepted_temperatures = []
            while k < polls:
                if temperature_list[k] != 0:
                    accepted_temperatures.append(temperature_list[k])
                    accepted_temperature_count += 1
                k += 1
                        
            l = 0
            accum_temperature = 0
            if accepted_temperature_count == 0:
                log.log("Too much variation")
            else:
                while l < accepted_temperature_count:
                    accum_temperature += accepted_temperatures[l]
                    l += 1

                avg_temperature = accum_temperature/accepted_temperature_count 
            self.current_temp = (avg_temperature * 1.8) + 32
