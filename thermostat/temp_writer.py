#!/usr/bin/python

import temperature_file_writer as Writer

def set_current_temp(temperature):
    return Writer.write_temp(temperature)
