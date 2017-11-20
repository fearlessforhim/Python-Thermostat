#!/usr/bin/python

import datetime
import os.path

class Log:
    def logHistory(self, target, current, is_on):
            file_name = datetime.date.today().strftime("history%m%d%Y.csv")
            fo = open(file_name, "a")
            fo.write(str(datetime.datetime.now()) + "," + str(target) + "," + str(current) + "," + str(is_on) + "\n")
            fo.close()
            
    def log(self, text):
        file_name = datetime.date.today().strftime("log%m%d%Y.txt")
        fo = open(file_name, "a")
        fo.write(text + "\n")
        fo.close()

    def logApp(self, text):
        file_name = datetime.date.today().strftime("log%m%d%Y.txt")
        fo = open(file_name, "a")
        fo.write(text + "\n")
        fo.close()
