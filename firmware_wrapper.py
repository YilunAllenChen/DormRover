'''
Backend of the DormRover project. Interaction with C library powered by ctypes
'''

import ctypes
import pathlib


# Load all libraries
def load_lib(libname: str):
    '''
    Helper function to load a shared C library
    '''
    try:
        libname = str(pathlib.Path().absolute() + libname)
    except:
        print(f"ERROR: {libname} not supplied. \nExiting...")
        exit()
    try:
        return ctypes.CDLL(libname)
    except Exception as e:
        print(f"ERROR: Can't load the {libname} dll: {e}\nExiting...")
        exit()

motion_control = load_lib('motion_control.so')
IMU = load_lib('IMU.so')



# Function return and parameter types declaration
try:
    motion_control.set_speed.argtypes = [ctypes.c_int]
    '''
    IMU.get_velocity_x.restype = ctypes.c_float
    IMU.get_velocity_y.restype = ctypes.c_float
    IMU.get_acceleration_x.restype = ctypes.c_float
    IMU.get_acceleration_y.restype = ctypes.c_float
    IMU.get_temperature.restype = ctypes.c_float
    '''
except Exception as e:
    print(f"ERROR: Library function return and argument types declaration failed for one of the functions: {e}\n Exiting...")
    exit()


# System initialization
motion_control.initialize_pins()
## TODO: IMU Initialization here




def get_IMU() -> dict:
    '''
    Function uses pre-built c++ libraries and obtain all data obtained by the IMU sensor.

    :return: returns a dictionary of all data.
        Example format: 
        {
            'velocity_x': 1.0,
            'velocity_y': 1.5,
            'humidity': 0.63
        }
    '''
    res = {}
    res['velocity_x'] = IMU.get_velocity_x()
    res['velocity_y'] = IMU.get_velocity_y()
    res['acceleration_x'] = IMU.get_acceleration_x()
    res['acceleration_y'] = IMU.get_acceleration_y()
    return res

def get_temperature() -> float:
    '''
    Function uses pre-built c++ libraries and obtain data obtained by the temperature sensor.

    :return: data obtained by the temperature sensor
    '''
    return motion_control.get_temperature()

def set_speed(speed: int) -> None:
    '''
    Function uses pre-built c++ libraries and set the speed of both motors to parameter speed.

    :param speed: The target speed, from 0 to 100.
    '''
    motion_control.set_speed(speed)

def go_straight() -> None:
    '''
    Function uses pre-built c++ libraries and let both motors go forward.
    '''
    motion_control.go_straight()

def go_backward() -> None:
    '''
    Function uses pre-built c++ libraries and let both motors go backward.
    '''
    motion_control.go_backward()

def turn_left() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot turn left.
    '''
    motion_control.turn_left()

def turn_right() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot turn right.
    '''
    motion_control.turn_right()

def stop() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot go to a hard stop.
    '''
    motion_control.stop()


# motion_control testing script. Run this file to test functionality.
if __name__ == '__main__':
    from time import sleep
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
