#!/usr/bin/python
import json

def write_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
