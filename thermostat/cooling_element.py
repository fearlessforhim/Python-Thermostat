#!/usr/bin/python

import status_reader as r
import status_writer as w
import time

class CoolingElement:

    def __init__(self):
        pass

    def run(self):
        while True:
            current_temperature = float(r.read_value('temperature'))
            new_temperature = (current_temperature - .1)
            w.write_value('temperature', round(new_temperature, 1))
            time.sleep(30);
