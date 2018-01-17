#!/usr/bin/python

import sqlite3

def get_is_heat_on():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Settings WHERE name = 'heat_on' ''')
    heat_on = cursor.fetchone()
    db.close()
    return heat_on[0] == 1

def set_is_heat_on(value):
    db = sqlite3.connect('thermostat.db')
    s_value = 1 if value else 0
    cursor = db.cursor()
    cursor.execute('''UPDATE Settings SET value = ''' + str(s_value) + ''' WHERE name= 'heat_on' ''')
    db.commit()
    db.close()


def get_is_fan_on():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Settings WHERE name = 'fan_on' ''')
    fan_on = cursor.fetchone()
    db.close()
    return fan_on[0] == 1


def set_is_fan_on(value):
    db = sqlite3.connect('thermostat.db')
    s_value = 1 if value else 0
    cursor = db.cursor()
    cursor.execute('''UPDATE Settings SET value = ''' + str(s_value) + ''' WHERE name= 'fan_on' ''')
    db.commit()
    db.close()

def get_is_temporary_set():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Settings WHERE name = 'is_temporary_set' ''')
    is_temporary_set = cursor.fetchone()
    db.close()
    return is_temporary_set[0] == 1

def set_is_temporary_set(value):
    db = sqlite3.connect('thermostat.db')
    s_value = 1 if value else 0
    cursor = db.cursor()
    cursor.execute('''UPDATE Settings SET value = ''' + str(s_value) + ''' WHERE name= 'is_temporary_set' ''')
    db.commit()
    db.close()

def get_is_temperature_held():
    db = sqlite3.connect('thermostat.db')
    cursor = db.cursor()
    cursor.execute('''SELECT value FROM Settings WHERE name = 'is_held' ''')
    is_held = cursor.fetchone()
    db.close()
    return is_held[0] == 1

def set_is_temperature_held(value):
    db = sqlite3.connect('thermostat.db')
    s_value = 1 if value else 0
    cursor = db.cursor()
    cursor.execute('''UPDATE Settings SET value = ''' + str(s_value) + ''' WHERE name= 'is_held' ''')
    db.commit()
    db.close()
