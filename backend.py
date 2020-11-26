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
import sys


DEBUG_MODE = False

for i in range(0,len(sys.argv)): #reads input whether we are running the robot version or not
    if (sys.argv[i] == "-debug"):
        DEBUG_MODE = True
print("Using [ {} ] build".format("\33[92mDEBUG\33[0m" if DEBUG_MODE else "\33[94mPRODUCTION\33[0m"))

if DEBUG_MODE:
    app = Flask(__name__, 
        template_folder=os.path.abspath("./Frontend/"),
        static_folder=os.path.abspath("./Frontend/static"))
else:
    app = Flask(__name__,
        template_folder=os.path.abspath("./Frontend/build/"),
        static_folder=os.path.abspath("./Frontend/build/static"))

CORS(app)



# Front page
@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['GET'])
@app.route('/app/dashboard', methods=['GET'])
def static_web_page():
    ''' 
    Serves the static web page
    '''
    if DEBUG_MODE: 
        return send_from_directory('Frontend/', 'index.html')
    else:
        return send_from_directory('Frontend/build/','index.html')

@app.route('/sensor_data/<sensor_name>', methods=['GET'])
def get_sensor_data(sensor_name):
    '''
    Function should call the pybinding function to obtain sensor data, jsonify it and return it.
    TODO: Implement this.
    '''
    data = {
        "placeholder": "foobar"
    }
    try:
        if sensor_name == "imu":
            data = get_IMU()
        elif sensor_name == 'temp':
            data = get_temp()
        elif sensor_name == 'lidar':
            data = get_lidar()
        else:
            data = {"ERROR": "Not supported or not implemented"}
    except Exception as e:
        data = {"ERROR": "Error occurred obtaining data." + str(e)}
    return jsonify(data)


@app.route('/command', methods=['POST'])
def command():
    '''
    Function should call the pybinding function to execute motor commands.
    '''
    key = request.json['key']
    if key == 'w':
        set_speed(100)
        go_straight()
        sleep(0.7)
    elif key == 's':
        set_speed(100)
        go_backward()
        sleep(0.7)
    elif key == 'a':
        set_speed(40)
        turn_left()
        sleep(0.3)
    elif key == 'd':
        set_speed(40)
        turn_right()
        sleep(0.3)
    elif key == 'servo_left':
        move_servo('left')
        sleep(0.5)
    elif key == 'servo_right':
        move_servo('right')
        sleep(0.5)
    elif key == 'servo_reset':
        move_servo('reset')
        sleep(0.5)
    stop()
    return jsonify({
        "payload": "foobar"
    })
    


@app.route('/app/video_feed')
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
