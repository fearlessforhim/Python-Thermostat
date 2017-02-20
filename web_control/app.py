#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/thermostat')
def thermostat():
    return render_template('thermostat.html')

@app.route('/setTemperature', methods=['POST'])
def setTemperature():
    if not request.json or not 'temperature' in request.json:
        print "Request is the following: ", request.json
        return jsonify({'response': 'error'})
    
    new_temperature = int(request.json['temperature'])

    settings_file = open('/media/pi/EXT/python_scripts/pi_only/rPiThermostat/settings.json')
    data = json.load(settings_file)
    data['temporary_temperature'] = new_temperature

    with open('/media/pi/EXT/python_scripts/pi_only/rPiThermostat/settings.json', 'w') as new_file:
        json.dump(data, new_file)
        
    return jsonify({'response': 'success'})

@app.route('/runSchedule', methods=['POST'])
def runSchedule():
    settings_file = open('/media/pi/EXT/python_scripts/pi_only/rPiThermostat/settings.json')
    data = json.load(settings_file)
    data['temporary_temperature'] = None

    with open('/media/pi/EXT/python_scripts/pi_only/rPiThermostat/settings.json', 'w') as new_file:
        json.dump(data, new_file)
    return jsonify({'response': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
