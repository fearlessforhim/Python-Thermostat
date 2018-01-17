#/usr/bin/python

import datetime
import sqlite3

def get_scheduled_target_temperature(day_of_week, hour, minute):
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    query = '''SELECT hour, minute, temperature, id FROM Schedule WHERE day_of_week = ''' + str(day_of_week) + ''' AND hour <= ''' + str(hour) + ''' AND minute <= ''' + str(minute) + ''' ORDER BY hour DESC, minute DESC'''
    cursor.execute(query)
    value = cursor.fetchone()
    db.close()
    if value is not None :
        return int(value[2]), int(value[3])
    else :
        if day_of_week > 0:
            return get_scheduled_target_temperature(day_of_week - 1, 23, 59)
        else :
            return get_scheduled_target_temperature(6, 23, 59)

def get_schedule():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM Schedule''')
    return cursor.fetchall()

def set_schedule_by_json(json_data):
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    for sched in json_data:
        query = '''UPDATE Schedule SET hour = ''' + str(sched['hour']) + ''', minute = ''' + str(sched['minute']) + ''', temperature =  ''' + str(sched['temperature']) + ''' WHERE id = ''' + str(sched['id'])
        cursor.execute(query)
    db.commit()
    db.close()
        
