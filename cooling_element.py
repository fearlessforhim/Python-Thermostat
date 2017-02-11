#!/usr/bin/python

import temp_reader as Reader
import temp_writer as Writer
import time

class CoolingElement:

    def run(self):
        while(True):
            current_temperature = float(Reader.get_current_temp())
            new_temperature = (current_temperature - .1)
            Writer.set_current_temp(new_temperature)
            time.sleep(30);
