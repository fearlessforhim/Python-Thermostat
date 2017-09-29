#!/usr/bin/python
import json

def read_json(path):
    data_file = open(path)
    return json.load(data_file)
