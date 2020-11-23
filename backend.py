'''
Backend of the DormRover project. Powered by Flask and python/C++ binding utilities
'''


from flask import Flask, jsonify, request, send_from_directory, Response
from flask_cors import CORS
from firmware_wrapper import *
from requests import get
from time import sleep
from random import choice
import os
import socket
app = Flask(__name__, 
    template_folder=os.path.abspath("./Frontend/"),
    static_folder=os.path.abspath("./Frontend/static"))
CORS(app)



# Front page
@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def static_web_page():
    ''' 
    Serves the static web page
    '''
    return send_from_directory('Frontend/', 'index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return send_from_directory('Frontend/', 'about.html')

@app.route('/description.html', methods=['GET'])
def desc():
    return send_from_directory('Frontend/', 'description.html')


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
    elif sensor_name == 'temp':
        data = get_temp()
    elif sensor_name == 'lidar':
        data = get_lidar()
    else:
        data = {"ERROR": "Not supported or not implemented"}
    return jsonify(data)


motion = 'STOP'
@app.route('/command', methods=['POST'])
def command():
    '''
    Function should call the pybinding function to execute motor commands.
    '''
    global motion
    key = request.json['key']
    if key == 'w' and motion != 'w':
        go_straight()
        print("motion is now " + motion)
        motion = 'w'
    elif key == 's' and motion != 's':
        go_backward()
        motion = 's'
        print("motion is now " + motion)
    elif key == 'a' and motion != 'a':
        turn_left()
        motion = 'a'
        print("motion is now " + motion)
    elif key == 'd' and motion != 'd':
        turn_right()
        motion = 'd'
        print("motion is now " + motion)
    elif key == 'STOP' and motion != 'STOP':
        stop()
        motion = 'STOP'
        print("motion is now " + motion)
    return jsonify({
        "payload": "foobar"
    })
    


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(vid_gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')  


if __name__ == "__main__":
    print("Server starting...")
    try:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
            s.connect(("google.com", 80))
            print("Currently running on IP address(public): [\33[94m {}:5000 \33[0m]".format(s.getsockname()[0]))
    except:
        print("DORO doesn't seem to be connected to the internet - It can't figure out the public IP address itself. Try 'ifconfig'.")

    app.run(host='0.0.0.0')