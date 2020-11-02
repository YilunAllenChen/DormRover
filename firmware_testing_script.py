'''
Backend of the DormRover project. Powered by Flask and python/C++ binding utilities

Refernces:
'''

import ctypes
import pathlib
from time import sleep

# Import the shared library
try:
    libname = str(pathlib.Path().absolute() / "firmware.so")
except:
    print("ERROR: firmware.so not supplied. \nExiting...")
    exit()

firmware = ctypes.CDLL(libname)
# Function return and parameter types declaration
try:
    firmware.set_speed.argtypes = [ctypes.c_int]
    # firmware.get_velocity_x.restype = ctypes.c_float
    # firmware.get_velocity_y.restype = ctypes.c_float
    # firmware.get_acceleration_x.restype = ctypes.c_float
    # firmware.get_acceleration_y.restype = ctypes.c_float
    # firmware.get_temperature.restype = ctypes.c_float
except Exception as e:
    print("ERROR: Initialization failed for one of the functions: {}\n Exiting...".format(e))
    exit()


# def get_IMU() -> dict:
#     '''
#     Function uses pre-built c++ libraries and obtain all data obtained by the IMU sensor.

#     :return: returns a dictionary of all data.
#         Example format: 
#         {
#             'velocity_x': 1.0,
#             'velocity_y': 1.5,
#             'humidity': 0.63
#         }
#     '''
#     res = {}
#     res['velocity_x'] = firmware.get_velocity_x()
#     res['velocity_y'] = firmware.get_velocity_y()
#     res['acceleration_x'] = firmware.get_acceleration_x()
#     res['acceleration_y'] = firmware.get_acceleration_y()
#     return res

# def get_temperature() -> float:
#     '''
#     Function uses pre-built c++ libraries and obtain data obtained by the temperature sensor.

#     :return: data obtained by the temperature sensor
#     '''
#     return firmware.get_temperature()

def set_speed(speed: float) -> None:
    '''
    Function uses pre-built c++ libraries and set the speed of both motors to parameter speed.

    :param speed: The target speed, from 0 to 100.
    '''
    firmware.set_speed(ctypes.c_int(speed))


def go_straight() -> None:
    '''
    Function uses pre-built c++ libraries and let both motors go forward.
    '''
    firmware.go_straight()

def go_backward() -> None:
    '''
    Function uses pre-built c++ libraries and let both motors go backward.
    '''
    firmware.go_backward()

def turn_left() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot turn left.
    '''
    firmware.turn_left()

def turn_right() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot turn right.
    '''
    firmware.turn_right()

def stop() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot go to a hard stop.
    '''
    firmware.stop()

def initialize_pins():
    firmware.initialize_pins()


if __name__ == '__main__':
    initialize_pins()
    set_speed(100)

    go_straight()
    print("going straight")
    sleep(1)
    print("Done. stopping...")
    stop()
    sleep(1)
    turn_left()
    print("turning left...")
    sleep(1)
    stop()
    print("Done. stopping...")
