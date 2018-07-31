#!/usr/bin/python

import datetime
import os.path
import sqlite3
import time

class Log:
    def logHistory(self, target, current, is_on):
        file_name = datetime.date.today().strftime("history%m%d%Y.csv")
        fo = open("history/" + file_name, "a")
        fo.write(str(datetime.datetime.now()) + "," + str(target) + "," + str(current) + "," + str(is_on) + "\n")
        fo.close()
        
        db = sqlite3.connect('thermostat.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO History (timestamp, target_temp, current_temp, is_furnace_on) VALUES (''' + str(int(time.time())) + ''',''' + str(target) + ''', ''' + str(current) + ''', ''' + str(1 if is_on else 0) + ''') ''')
        db.commit()
        db.close()
        
    def log(self, text):
        #print(str(datetime.datetime.now()) + " " + text)
        file_name = datetime.date.today().strftime("log%m%d%Y.txt")
        fo = open("logs/" + file_name, "a")
        if(text == ""):
            fo.write("\n")
        else:
            fo.write(str(datetime.datetime.now()) + " " + text + "\n")
        fo.close()

    def logTemperatureRead(self, text):
        file_name = datetime.date.today().strftime("%m%d%Y-tempLog.txt")
        fo = open("temperatureLogs/" + file_name, "a")
        if(text == ""):
            fo.write("\n")
        else:
            fo.write(str(datetime.datetime.now()) + " " + text + "\n")
        fo.close()
