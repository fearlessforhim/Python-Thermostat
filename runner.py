#!/usr/bin/python

from threading import Thread
import thermostat
import time
from furnace import Furnace
from thermostat import Thermostat
from status_reader import Reader

f = Furnace()
furnaceThread = Thread(target = f.run, args = ())
furnaceThread.daemon = True
furnaceThread.start()


r = Reader()
readerThread = Thread(target = r.execute, args = ())
readerThread.daemon = True
readerThread.start()

t = Thermostat()
thermostatThread = Thread(target = t.run, args = (f,r,))
thermostatThread.daemon = True
thermostatThread.start()

while True:
	time.sleep(1)
