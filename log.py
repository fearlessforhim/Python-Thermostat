#!/usr/bin/python

import datetime
import os.path

class Log:
    def logHistory(self, target, current, is_on):
        file_name = datetime.date.today().strftime("history%m%d%Y.csv")
        fo = open("history/" + file_name, "a")
        fo.write(str(datetime.datetime.now()) + "," + str(target) + "," + str(current) + "," + str(is_on) + "\n")
        fo.close()
            
    def log(self, text):
        #print(str(datetime.datetime.now()) + " " + text)
        file_name = datetime.date.today().strftime("log%m%d%Y.txt")
        fo = open("logs/" + file_name, "a")
        if(text == ""):
            fo.write("\n")
        else:
            fo.write(str(datetime.datetime.now()) + " " + text + "\n")
        fo.close()
