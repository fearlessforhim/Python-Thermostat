#!/bin/python

import urllib2

contents = urllib2.urlopen('https://api.darksky.net/forecast/9e3462c720bac2ae701a1ba48c664603/45.7588020,-108.6041610').read()
print contents
