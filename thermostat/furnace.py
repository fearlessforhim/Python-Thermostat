#!/usr/bin/python

import status_reader as r
import status_writer as w
import time
import RPi.GPIO as GPIO

class Furnace:

    def __init__(self):
        pass

    is_heat_on = False
    is_fan_on = False
    efficiency = 10

    def run(self):
        GPIO.setmode(GPIO.BOARD)
        while True:
            GPIO.setup(11, GPIO.OUT)
            if self.is_heat_on:
                #ensure we are sending a gpio out to relay
                #current_temperature = float(r.read_value('temperature'))
                #new_temperature = (current_temperature + .1)
                #w.write_value('temperature', round(new_temperature, 1))
                if not GPIO.input(11):
                    GPIO.output(11, True)
            else:
                if GPIO.input(11):
                    GPIO.output(11, False)
                #ensure we are NOT sending a gpio out to relay

            if self.is_fan_on:
                pass
                # w.write_value('fan_on', True)
                #ensure we are sending a gpio out to fan relay
            else:
                pass    
                # w.write_value('fan_on', False)
            #GPIO.cleanup()
            time.sleep(50/self.efficiency);
            #check every 5 seconds whether the gpio should be sending or not
