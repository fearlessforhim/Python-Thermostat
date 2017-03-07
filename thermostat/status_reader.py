#!/usr/bin/python

import json_file_reader as R
import sys
import Adafruit_DHT
import time
import math

class Reader:

    def __init__(self):
        pass

    current_temp = 0

    def read_value(self):
        return self.current_temp
    
    def execute(self):
        #status = R.read_json('status.json')
        #return status[name]
        print 'Attempting temperature read'
        humidity, temperature_c = Adafruit_DHT.read_retry(11, 4)
        temperature_f = (temperature_c * 9/5) + 32
        temperature_sum = 0
        avg_temperature = 0
        polls = 6
        temperature_list = []
        i = 0
        
        while i < polls:
            humidity, temperature_c = Adafruit_DHT.read_retry(11, 4)
            #        print 'Read: {0:0.1f}'.format(temperature_c)
            temperature_list.append(temperature_c)
            i += 1
            time.sleep(2)
        
        j = 0

        while j < polls:
            temperature_sum += temperature_list[j]
            j += 1
        avg_temperature = temperature_sum/polls

        k = 0

        accepted_temperature_count = 0;
        accepted_temperatures = []
        while k < polls:
            if math.fabs(temperature_list[k] - avg_temperature) < 5:
                accepted_temperatures.append(temperature_list[k])
                accepted_temperature_count += 1
            k += 1

        l = 0
        accum_temperature = 0
        if accepted_temperature_count == 0:
            print 'Too much variation'
        else:
#        print 'Accepting {0} temperatures'.format(accepted_temperature_count)
            while l < accepted_temperature_count:
                accum_temperature += accepted_temperatures[l]
                l += 1
                avg_temperature = accum_temperature/accepted_temperature_count 
                #        print 'Temp: {0:0.1f} C'.format(avg_temperature)
            self.current_temp = avg_temperature
