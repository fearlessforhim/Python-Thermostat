#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import json
import json_file_reader as reader
import json_file_writer as writer

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/thermostat')
def thermostat():
    return render_template('thermostat.html')

@app.route('/setTemperature', methods=['POST'])
def set_temperature():
    if not request.json or not 'temperature' in request.json:
        print "Request is the following: ", request.json
        return jsonify({'response': 'error'})
    
    settings = reader.read_json('../settings.json')
    settings['temporary_temperature'] = int(request.json['temperature'])
    writer.write_json(settings, '../settings.json')

    status = reader.read_json('../status.json')
    status['temporary'] = True
    writer.write_json(status, '../status.json')
        
    return jsonify({'response': 'success'})

@app.route('/runSchedule', methods=['POST'])
def run_schedule():
    settings = reader.read_json('../settings.json')
    settings['temporary_temperature'] = None
    writer.write_json(settings, '../settings.json')
    
    status = reader.read_json('../status.json')
    status['temporary'] = False
    writer.write_json(status, '../status.json')

    return jsonify({'response': 'success'})

@app.route('/currentState', methods=['GET'])
def get_current_state():
    # temperature_file = open('../temperature.txt')
    # t = temperature_file.read(10)
    # temperature_file.close()
    status = reader.read_json('../status.json')
    settings = reader.read_json('../settings.json')
    return jsonify({"temperature": status['temperature'], "temporary": settings['temporary_temperature']})
    # return reader.read_json('../status.json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
