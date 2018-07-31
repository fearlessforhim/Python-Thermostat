#!/usr/bin/python

import sqlite3
import time
import urllib2
import json

def get_history():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    rows = cursor.execute('''SELECT * FROM (SELECT strftime('%Y-%m-%d', datetime(timestamp, 'unixepoch', 'localtime')) AS mydate, COUNT(*) AS mycount FROM History WHERE is_furnace_on = 1 GROUP BY strftime('%Y-%m-%d', datetime(timestamp, 'unixepoch', 'localtime')) ORDER BY strftime('%Y-%m-%d', datetime(timestamp, 'unixepoch', 'localtime')) DESC LIMIT 30) ORDER BY mydate ASC;''')
    json_s = "{\"heatList\": ["
    rowCount = 0
    for r in rows:
        rowCount = rowCount + 1
        json_s += ("{\"date\":\"" + str(r[0]) + "\",")
        json_s += ("\"count\":"+ str(r[1]) + "},")

    if rowCount > 0:
        json_s = json_s[:-1]
    json_s += "],"

    json_s += "\"weatherList\": ["

    rows = cursor.execute('''SELECT * FROM (SELECT strftime('%Y-%m-%d', datetime(timestamp, 'unixepoch', 'localtime')) AS mydate, temp_high, temp_low FROM WeatherHistory ORDER BY strftime('%Y-%m-%d', datetime(timestamp, 'unixepoch', 'localtime')) DESC LIMIT 29) ORDER BY myDate ASC;''')

    rowCount = 0
    for r in rows:
        rowCount = rowCount +1
        json_s += ("{\"date\": \"" + str(r[0]) + "\", \"values\" : {\"high\" : " + str(r[1]) + ", \"low\": " + str(r[2]) + "}},")

    if rowCount > 0:
        json_s = json_s[:-1]
    json_s += "]}"
    
    db.close()
    return json_s

def insert_weather_history():
    print str(int(time.time()))
    print 'https://api.darksky.net/forecast/9e3462c720bac2ae701a1ba48c664603/45.7588020,-108.6041610,'+ str(int(time.time()-54000))
    response = urllib2.urlopen('https://api.darksky.net/forecast/9e3462c720bac2ae701a1ba48c664603/45.7588020,-108.6041610,'+ str(int(time.time()-54000)))
    contents = json.load(response)
    print contents["daily"]["data"][0]["temperatureHigh"]
    print contents["daily"]["data"][0]["temperatureLow"]
    query = '''INSERT INTO WeatherHistory (timestamp, temp_high, temp_low) VALUES (''' + str(int(time.time()-43200)) + ''',''' + str(contents["daily"]["data"][0]["temperatureHigh"])+ ''',''' +str(contents["daily"]["data"][0]["temperatureLow"])+ ''')'''
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    db.close()
