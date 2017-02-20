#!/usr/bin/python

def write_temp(temperature):
    fo = open("temperature.txt", "r+")
    fo.write(str(temperature))
    fo.close()
