#!/usr/bin/python

import datetime
import time
import urllib2
import json
import sqlite3

class WeatherHistory:

    def __init__(self):
        pass

    def start_weather_history(self, t):
        now = datetime.datetime.now()
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        tomorrow = tomorrow.replace(hour=3, minute=0)
        now_timestamp = time.mktime(now.timetuple())
        tomorrow_timestamp = time.mktime(tomorrow.timetuple())

#        print "Sleeping: " + str(tomorrow_timestamp - now_timestamp)
#        time.sleep(tomorrow_timestamp - now_timestamp)
#        while True:
        self.do_weather_history_check(t)
#            print "Sleeping till tomorrow"
#            time.sleep(86400)

    def do_weather_history_check(self, t):
        response = urllib2.urlopen('https://api.darksky.net/forecast/9e3462c720bac2ae701a1ba48c664603/45.7588020,-108.6041610,'+ str(t))
        contents = json.load(response)
        query = '''INSERT INTO WeatherHistory (timestamp, temp_high, temp_low) VALUES (''' + str(t) + ''',''' + str(contents["daily"]["data"][0]["temperatureHigh"])+ ''',''' +str(contents["daily"]["data"][0]["temperatureLow"])+ ''')'''
        db = sqlite3.connect('thermostat.db')
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        db.close()
