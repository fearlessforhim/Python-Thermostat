#!/usr/bin/python
import json

def write_status(data):
    with open('../status.json', 'w') as outfile:
        json.dump(data, outfile)
