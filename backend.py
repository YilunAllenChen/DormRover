'''
Backend of the DormRover project. Powered by Flask and python/C++ binding utilities

Refernces:
https://flask.palletsprojects.com/en/1.1.x/quickstart/
'''

from flask import Flask, jsonify, request


def pybinding_get_sensor_data() -> dict:
    '''
    Function should use python binding to interact with pre-built c++ libraries and obtain all sensor data.

    :return: returns a dictionary of all data.
        Example format: 
        {
            'velocity_x': 1.0,
            'velocity_y': 1.5,
            'humidity': 0.63
        }
    TODO: Implement this.
    '''
    return None


def pybinding_motion_control(command: str) -> None:
    '''
    Function takes in the command and calls pre-built c++ libraries and execute those commands.

    Command of format string and backed by a parser? We can discuss this.
    TODO: Implement this.
    '''
    pass





app = Flask(__name__)

@app.route('/', methods=['GET'])
def static_web_page():
    ''' 
    Serves the static web page

    TODO: Implement this.
    '''
    return 'Hello, World!'


@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    '''
    Function should call the pybinding function to obtain sensor data, jsonify it and return it.

    TODO: Implement this.
    '''
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