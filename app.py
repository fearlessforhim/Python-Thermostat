#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import json_file_reader as reader
import json_file_writer as writer
import scheduler as schedule
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/thermostat')
def render_thermostat():
    return render_template('thermostat.html')

@app.route('/playground')
def render_schedule():
    return render_template('playground.html')

@app.route('/setTemperature', methods=['POST'])
def set_temperature():
    if not request.json or not 'temperature' in request.json:
        return jsonify({'response': 'error'})
    
    settings = reader.read_json('settings.json')
    settings['temporary_temperature'] = int(request.json['temperature'])
    writer.write_json(settings, 'settings.json')
        
    return jsonify({'response': 'success'})

@app.route('/runSchedule', methods=['POST'])
def run_schedule():
    settings = reader.read_json('settings.json')
    settings['temporary_temperature'] = None
    writer.write_json(settings, 'settings.json')

    return jsonify({'response': 'success'})

@app.route('/currentState', methods=['GET'])
def get_current_state():
    status = reader.read_json('status.json')
    settings = reader.read_json('settings.json')
    message = reader.read_json('message.json')
    
    target_temp = schedule.get_scheduled_target_temperature(settings)
    using_temporary_temperature = settings['temporary_temperature'] is not None
    
    if using_temporary_temperature:
        target_temp = settings['temporary_temperature']

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    is_heat_off = GPIO.input(11)
#    is_heat_off = True
        
    return jsonify({"curTemp": status['temperature'], "usingTemporary": using_temporary_temperature, "targetTemp": target_temp, "isHeatOn": is_heat_off == 0, "allowingHeat" : settings['heat'], "allowingFan" : settings['fan'], "message" : message['message']})

@app.route('/toggleHeat', methods=['POST'])
def toggle_heat():
    settings = reader.read_json('settings.json')
    settings['heat'] = not settings['heat']
    writer.write_json(settings, 'settings.json')

    return jsonify({'response': 'success'})

@app.route('/toggleFan', methods=['POST'])
def toggle_fan():
    settings = reader.read_json('settings.json')
    settings['fan'] = not settings['fan']
    writer.write_json(settings, 'settings.json')

    return jsonify({'response': 'success'})

@app.route('/schedule_data', methods=['GET'])
def get_schedule_data():
    return jsonify(reader.read_json('settings.json'))

@app.route('/setSchedule', methods=['POST'])
def set_schedule():
    if not request.json:
        return jsonify({'response': 'error'})
    
    settings = reader.read_json('settings.json')
    settings['schedules'] = request.json
    writer.write_json(settings, 'settings.json')
        
    return jsonify({'response': 'success'})

@app.route('/getMessage', methods=['GET'])
def get_message():
    message = reader.read_json('message.json')
    return jsonify({"message": message["message"]})

if __name__ == '__main__':
    config = reader.read_json('config.json')
    portNum = int(config["portNum"])
    app.run(debug=False, host='0.0.0.0', port=portNum)
