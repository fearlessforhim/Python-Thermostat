#!/bin/python
from weather_history_test import WeatherHistory
import subprocess
import sqlite3
import json
import time
from dateutil.parser import parse
import sys


w = WeatherHistory()
w.start_weather_history(sys.argv[1])
