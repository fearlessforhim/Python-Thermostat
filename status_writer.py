#!/usr/bin/python

import json_file_reader as r
import json_file_writer as w

def write_value(name, value):
    status = r.read_json('status.json')
    status[name] = value
    w.write_json(status, 'status.json');

