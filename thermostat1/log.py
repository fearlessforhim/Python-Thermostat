#!/usr/bin/python

import datetime
import os.path

class Log:
    def log(self, target, current, is_on):
            file_name = datetime.date.today().strftime("history%m%d%Y.csv")
            if not os.path.isfile(file_name):
                fo = open("history.csv", "a")
                fo.write("Time, Target Temperature, Current Temperature, Is Furnace On\n")
                fo.close()
            fo = open(file_name, "a")
            fo.write(str(datetime.datetime.now()) + "," + str(target) + "," + str(current) + "," + str(is_on) + "\n")
            fo.close()
