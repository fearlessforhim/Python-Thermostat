#!/usr/bin/python

import sqlite3

def get_by_day_of_week(day_of_week):
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Status WHERE name = 'is_heat_on' ''')
    value = cursor.fetchone()
    db.close()
    return value[0] == 1

def set_is_heat_on(value):
    db = sqlite3.connect('thermostat.db')
    s_value = 1 if value else 0
    cursor = db.cursor()
    cursor.execute('''UPDATE Status SET value = ''' + str(s_value) + ''' WHERE name= 'is_heat_on' ''')
    db.commit()
    db.close()

def get_current():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Temperatures WHERE name = 'current' ''')
    value = cursor.fetchone()
    db.close()
    return value[0]

def set_current(value):
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE Temperatures SET value = ''' + str(value) + ''' WHERE name = 'current' ''')
    db.commit()
    db.close()
