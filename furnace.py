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
            GPIO.setup(13, GPIO.OUT)
            if self.is_heat_on:
                #ensure we are sending a gpio out to relay
                if GPIO.input(11):
                    GPIO.output(11, False)
            else:
                if not GPIO.input(11):
                    GPIO.output(11, True)
                #ensure we are NOT sending a gpio out to relay

            if self.is_fan_on:
                if GPIO.input(13):
                    GPIO.output(13, False)
                #ensure we are sending a gpio out to fan relay
            else:
                if not GPIO.input(13):
                    GPIO.output(13, True)
            time.sleep(50/self.efficiency);
            #check every 5 seconds whether the gpio should be sending or not
