#!/usr/bin/python

import sqlite3

def get_target():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Temperatures WHERE name = 'temporary_target' ''')
    value = cursor.fetchone()
    db.close()
    return value[0]

def set_target(value):
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE Temperatures SET value = ''' + str(value) + ''' WHERE name= 'temporary_target' ''')
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
