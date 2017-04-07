#!/usr/bin/python

import json_file_reader as R
import sys
import Adafruit_DHT
import time
import math
import dht11
import RPi.GPIO as GPIO

class Reader:

    def __init__(self):
        pass

    current_temp = 0

    def read_value(self):
        return self.current_temp
    
    def execute(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        
        while True:
            instance = dht11.DHT11(pin=7)
            temperature_sum = 0
            avg_temperature = 0
            polls = 12
            temperature_list = []
            i = 0
            
            while i < polls:
                result = instance.read()
                humidity = result.humidity
                temperature_c = result.temperature
                if result.is_valid():
                    temperature_list.append(temperature_c)
                    i += 1
                time.sleep(1)
                
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
                print 'Too much variation'
            else:
                while l < accepted_temperature_count:
                    accum_temperature += accepted_temperatures[l]
                    l += 1

                avg_temperature = accum_temperature/accepted_temperature_count 
            #print "New temperature is ", avg_temperature
            self.current_temp = (avg_temperature * 1.8) + 32
