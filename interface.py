'''
Backend of the DormRover project. Powered by Flask and python/C++ binding utilities

Refernces:
'''

import ctypes
import pathlib

try:
    libname = pathlib.Path().absolute() / "firmware.so"
    firmware = ctypes.CDLL(libname)
except:
    print("ERROR: firmware.so not supplied.")
    exit()


# Function return and parameter types declaration
firmware.set_speed.argtypes = [ctypes.c_int]
firmware.get_velocity_x.restype = ctypes.c_float
firmware.get_velocity_y.restype = ctypes.c_float
firmware.get_acceleration_x.restype = ctypes.c_float
firmware.get_acceleration_y.restype = ctypes.c_float
firmware.get_temperature.restype = ctypes.c_float


def get_IMU() -> dict:
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

