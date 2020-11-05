'''
Backend of the DormRover project. Powered by Flask and python/C++ binding utilities
'''


from flask import Flask, jsonify, request, send_from_directory, Response
from firmware_wrapper import *
from camera_utils import vid_gen
from time import sleep
from random import choice
app = Flask(__name__)


# Front page
@app.route('/', methods=['GET'])
def static_web_page():
    ''' 
    Serves the static web page
    '''
    return send_from_directory('Frontend/', 'index.html')



@app.route('/sensor_data/<sensor_name>', methods=['GET'])
def get_sensor_data(sensor_name):
    '''
    Function should call the pybinding function to obtain sensor data, jsonify it and return it.
    TODO: Implement this.
    '''
    data = {
        "placeholder": "foobar"
    }
    if sensor_name == "imu":
        data = get_IMU()
    else:
        data = {"ERROR": "Not supported or not implemented"}
    return jsonify(data)


@app.route('/command', methods=['POST'])
def command():
    '''
    Function should call the pybinding function to execute motor commands.
    '''
    print('request data', request.json)

    key = request.json['key']
    if key == 'w':
        go_straight()
        sleep(1)
    elif key == 's':
        go_backward()
        sleep(1)
    elif key == 'a':
        turn_left()
        sleep(1)
    elif key == 'd':
        turn_right()
        sleep(1)
    stop()
    return jsonify({
        "payload": "foobar"
    })
    


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(vid_gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')  


if __name__ == "__main__":
    app.run(host='0.0.0.0')