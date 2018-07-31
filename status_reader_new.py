#!/usr/bin/python

import sys
import Adafruit_MCP9808.MCP9808 as MCP9808
import time
import math
import RPi.GPIO as GPIO
from log import Log

class Reader2:

    def __init__(self):
        pass

    current_temp = 0
    queue = list()

    def read_value(self):
        log = Log()
        if len(self.queue) < 20:
            return 0;

        flat_sum = 0
        flat_sum += (self.queue[0] * 5)
        flat_sum += (self.queue[1] * 5)
        flat_sum += (self.queue[2] * 5)
        flat_sum += (self.queue[3] * 5)
        flat_sum += (self.queue[4] * 5)
        flat_sum += (self.queue[5] * 5)
        flat_sum += (self.queue[6] * 5)
        flat_sum += (self.queue[7] * 5)
        flat_sum += (self.queue[8] * 5)
        flat_sum += (self.queue[9] * 5)
        flat_sum += (self.queue[10] * 5)
        flat_sum += (self.queue[11] * 5)
        flat_sum += (self.queue[12] * 5)
        flat_sum += (self.queue[13] * 5)
        flat_sum += (self.queue[14] * 5)
        flat_sum += (self.queue[15] * 5)
        flat_sum += (self.queue[16] * 5)
        flat_sum += (self.queue[17] * 5)
        flat_sum += (self.queue[18] * 5)
        flat_sum += (self.queue[19] * 5)
        
        bell_sum = 0
        bell_sum += (self.queue[0] * 1)
        bell_sum += (self.queue[1] * 1)
        bell_sum += (self.queue[2] * 2)
        bell_sum += (self.queue[3] * 3)
        bell_sum += (self.queue[4] * 4)
        bell_sum += (self.queue[5] * 6)
        bell_sum += (self.queue[6] * 8)
        bell_sum += (self.queue[7] * 10)
        bell_sum += (self.queue[8] * 12)
        bell_sum += (self.queue[9] * 13)
        bell_sum += (self.queue[10] * 13)
        bell_sum += (self.queue[11] * 12)
        bell_sum += (self.queue[12] * 10)
        bell_sum += (self.queue[13] * 8)
        bell_sum += (self.queue[14] * 6)
        bell_sum += (self.queue[15] * 4)
        bell_sum += (self.queue[16] * 3)
        bell_sum += (self.queue[17] * 1)
        bell_sum += (self.queue[18] * 1)
        bell_sum += (self.queue[19] * 1)

        left_bell_sum = 0
        left_bell_sum += (self.queue[0] * 1)
        left_bell_sum += (self.queue[1] * 6)
        left_bell_sum += (self.queue[2] * 9)
        left_bell_sum += (self.queue[3] * 11)
        left_bell_sum += (self.queue[4] * 13)
        left_bell_sum += (self.queue[5] * 13)
        left_bell_sum += (self.queue[6] * 12)
        left_bell_sum += (self.queue[7] * 9)
        left_bell_sum += (self.queue[8] * 7)
        left_bell_sum += (self.queue[9] * 6)
        left_bell_sum += (self.queue[10] * 5)
        left_bell_sum += (self.queue[11] * 5)
        left_bell_sum += (self.queue[12] * 4)
        left_bell_sum += (self.queue[13] * 4)
        left_bell_sum += (self.queue[14] * 3)
        left_bell_sum += (self.queue[15] * 3)
        left_bell_sum += (self.queue[16] * 3)
        left_bell_sum += (self.queue[17] * 2)
        left_bell_sum += (self.queue[18] * 2)
        left_bell_sum += (self.queue[19] * 2)

        right_bell_sum = 0
        right_bell_sum += (self.queue[0] * 2)
        right_bell_sum += (self.queue[1] * 2)
        right_bell_sum += (self.queue[2] * 2)
        right_bell_sum += (self.queue[3] * 3)
        right_bell_sum += (self.queue[4] * 3)
        right_bell_sum += (self.queue[5] * 3)
        right_bell_sum += (self.queue[6] * 4)
        right_bell_sum += (self.queue[7] * 4)
        right_bell_sum += (self.queue[8] * 5)
        right_bell_sum += (self.queue[9] * 5)
        right_bell_sum += (self.queue[10] * 6)
        right_bell_sum += (self.queue[11] * 7)
        right_bell_sum += (self.queue[12] * 9)
        right_bell_sum += (self.queue[13] * 12)
        right_bell_sum += (self.queue[14] * 13)
        right_bell_sum += (self.queue[15] * 13)
        right_bell_sum += (self.queue[16] * 11)
        right_bell_sum += (self.queue[17] * 9)
        right_bell_sum += (self.queue[18] * 6)
        right_bell_sum += (self.queue[19] * 1)

        return ((flat_sum/100) * 1.8) + 32
    
    def execute(self):
        log = Log()
        
        sensor = MCP9808.MCP9808()
        sensor.begin()

        count = 0;
        
        while True:

            if self.queue is not None:
                if len(self.queue) > 20 :
                    self.queue.pop(0)

            try:
                temperature_c = sensor.readTempC()
                self.queue.append(temperature_c)
                time.sleep(1)
            except IOError as ex:
                log.log(str(ex))

            if count == 20 :
                count = 0
                self.read_value()
            count += 1
