#!/usr/bin/python

import temp_reader as Reader
import temp_writer as Writer
import time

class Furnace:

    is_heat_on = False
    is_fan_on = False
    efficiency = 10

    def run(self):
        while(True):
            if(self.is_heat_on):
                #ensure we are sending a gpio out to relay
                current_temperature = float(Reader.get_current_temp())
                new_temperature = (current_temperature + .1)
                Writer.set_current_temp(new_temperature)
            #else:
                #ensure we are NOT sending a gpio out to relay

            if(self.is_fan_on):
                #ensure we are sending a gpio out to fan relay
                pass
            time.sleep(50/self.efficiency);
            #check every 5 seconds whether the gpio should be sending or not
