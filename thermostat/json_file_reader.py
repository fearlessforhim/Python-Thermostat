#!/usr/bin/python
import json

def read_status():
    data_file = open('../status.json')
    return json.load(data_file)
