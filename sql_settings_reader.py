#!/usr/bin/python

import sqlite3

def is_heat_on():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Settings WHERE name = 'heat_on' ''')
    heat_on = cursor.fetchone()
    db.close()
    return heat_on[0] == 1

def is_fan_on():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Settings WHERE name = 'fan_on' ''')
    fan_on = cursor.fetchone()
    db.close()
    return fan_on[0] == 1
