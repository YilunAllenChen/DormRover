'''
Backend of the DormRover project. Powered by Flask and python/C++ binding utilities

Refernces:
https://flask.palletsprojects.com/en/1.1.x/quickstart/
'''

from flask import Flask, jsonify, request
from interface import *




app = Flask(__name__)

@app.route('/', methods=['GET'])
def static_web_page():
    ''' 
    Serves the static web page

    TODO: Implement this.
    '''
    return 'Hello, World!'


@app.route('/sensor_data/<str:sensor_name>', methods=['GET'])
def get_sensor_data(sensor_name):
    '''
    Function should call the pybinding function to obtain sensor data, jsonify it and return it.

    TODO: Implement this.
    '''
    if sensor_name == "IMU":
        data = {}
    elif sensor_name == "camera":
        data = {}
    data = pybinding_get_sensor_data()
    return jsonify(data)


@app.route('/command', methods=['POST'])
def command(COMMAND):
    '''
    Function should call the pybinding function to execute motor commands.

    TODO: Implement this.
    '''
    params = request.form # request.form should be of dict format
    pybinding_motion_control(params)
    return





if __name__ == "__main__":
    app.run()