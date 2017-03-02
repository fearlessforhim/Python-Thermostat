#!/usr/bin/python

import json_file_reader as R

def read_value(name):
    status = R.read_json('status.json')
    return status[name]
