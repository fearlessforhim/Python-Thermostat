#!/usr/bin/python

def read_temp():
    fo = open("temperature.txt", "r+")
    str = fo.read(10)
    fo.close()
    return float(str)
