#!/usr/bin/python

from threading import Thread
import thermostat
import time
from furnace import Furnace
from thermostat import Thermostat
from cooling_element import CoolingElement

f = Furnace()
furnaceThread = Thread(target = f.run, args = ())
furnaceThread.daemon = True
furnaceThread.start()

t = Thermostat()
thermostatThread = Thread(target = t.run, args = (f,))
thermostatThread.daemon = True
thermostatThread.start()

c = CoolingElement()
coolingThread = Thread(target = c.run, args = ())
coolingThread.daemon = True
coolingThread.start()

while True:
    time.sleep(1)
