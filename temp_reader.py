#!/usr/bin/python

import temperature_file_reader as Reader

def get_current_temp():
    return Reader.read_temp()
