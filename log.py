#!/usr/bin/python

import datetime
import os.path

class Log:
    def log(self, target, current, isOn):
            if(not os.path.isfile("history.csv")):
                fo = open("history.csv", "a")
                fo.write("Time, Target Temperature, Current Temperature, Is Furnace On\n")
                fo.close()
            fo = open("history.csv", "a")
            fo.write(str(datetime.datetime.now()) + "," + str(target) + "," + str(current) + "," + str(isOn) + "\n")
            fo.close()
