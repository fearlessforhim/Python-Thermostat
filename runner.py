#!/usr/bin/python

from threading import Thread
import thermostat
import time
from furnace import Furnace
from thermostat import Thermostat
from status_reader import Reader
from status_reader_new import Reader2
from weather_history import WeatherHistory

f = Furnace()
furnaceThread = Thread(target = f.run, args = ())
furnaceThread.daemon = True
furnaceThread.start()


r = Reader2()
readerThread = Thread(target = r.execute, args = ())
readerThread.daemon = True
readerThread.start()

t = Thermostat()
thermostatThread = Thread(target = t.run, args = (f,r,))
thermostatThread.daemon = True
thermostatThread.start()

w = WeatherHistory()
weatherHistoryThread = Thread(target = w.start_weather_history, args = ())
weatherHistoryThread.daemon = True
weatherHistoryThread.start()

while True:
	time.sleep(1)
