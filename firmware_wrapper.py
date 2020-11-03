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

motion_control_lib = load_lib('motion_control.so')
IMU_lib = load_lib('IMU.so')



# Function return and parameter types declaration
try:
    motion_control_lib.set_speed.argtypes = [ctypes.c_int]
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
motion_control_lib.initialize_pins()
imu = IMU_lib.LSM9DS1_create()
IMU_lib.LSM9DS1_begin(imu)
if IMU_lib.LSM9DS1_begin(imu) == 0:
    print("Failed to communicate with LSM9DS1.")
    exit()
IMU_lib.LSM9DS1_calibrate(imu)




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
    res = None
    # if IMU_lib.LSM9DS1_accelAvailable(imu) == 0:
    IMU_lib.LSM9DS1_readAccel(imu)
    ax = IMU_lib.LSM9DS1_getAccelX(imu)
    ay = IMU_lib.LSM9DS1_getAccelY(imu)
    az = IMU_lib.LSM9DS1_getAccelZ(imu)
    res = {
        'ax': ax,
        'ay': ay,
        'az': az
    }
    return res

def get_temperature() -> float:
    '''
    Function uses pre-built c++ libraries and obtain data obtained by the temperature sensor.

    :return: data obtained by the temperature sensor
    '''
    return motion_control_lib.get_temperature()

def set_speed(speed: int) -> None:
    '''
    Function uses pre-built c++ libraries and set the speed of both motors to parameter speed.

    :param speed: The target speed, from 0 to 100.
    '''
    motion_control_lib.set_speed(speed)

def go_straight() -> None:
    '''
    Function uses pre-built c++ libraries and let both motors go forward.
    '''
    motion_control_lib.go_straight()

def go_backward() -> None:
    '''
    Function uses pre-built c++ libraries and let both motors go backward.
    '''
    motion_control_lib.go_backward()

def turn_left() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot turn left.
    '''
    motion_control_lib.turn_left()

def turn_right() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot turn right.
    '''
    motion_control_lib.turn_right()

def stop() -> None:
    '''
    Function uses pre-built c++ libraries and let the robot go to a hard stop.
    '''
    motion_control_lib.stop()


# motion_control_lib testing script. Run this file to test functionality.
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

    while True:
        print(get_IMU())