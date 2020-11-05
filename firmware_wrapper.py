'''
Backend of the DormRover project. Interaction with C library powered by ctypes
'''

from ctypes import *
import ctypes
import pathlib

# Load all libraries

on = '[\33[31m  ON  \33[0m]'
off = '[\33[31m OFF  \33[0m]'

system_status = {
    'Motion Control': off,
    'IMU': off,
    'Light Sensor': off
}

def load_lib(libname: str):
    '''
    Helper function to load a shared C library
    '''
    try:
        libname = str(pathlib.Path().absolute() / "Firmware" / libname)
        return ctypes.CDLL(libname)
    except Exception as e:
        print("ERROR: Library {} could not be loaded: {}".format(
            libname, e))

try:
    motion_control_lib = load_lib('motion_control.so')
    motion_control_lib.set_speed.argtypes = [ctypes.c_int]
except:
    print("Unable to load motion control libraries. Doro will proceed without it.")

try:
    IMU_lib = load_lib('IMU.so')
    IMU_lib.LSM9DS1_create.argtypes = []
    IMU_lib.LSM9DS1_create.restype = c_void_p
    IMU_lib.LSM9DS1_begin.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_begin.restype = None
    IMU_lib.LSM9DS1_calibrate.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_calibrate.restype = None
    IMU_lib.LSM9DS1_gyroAvailable.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_gyroAvailable.restype = c_int
    IMU_lib.LSM9DS1_accelAvailable.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_accelAvailable.restype = c_int
    IMU_lib.LSM9DS1_magAvailable.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_magAvailable.restype = c_int
    IMU_lib.LSM9DS1_readGyro.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_readGyro.restype = c_int
    IMU_lib.LSM9DS1_readAccel.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_readAccel.restype = c_int
    IMU_lib.LSM9DS1_readMag.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_readMag.restype = c_int
    IMU_lib.LSM9DS1_getGyroX.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getGyroX.restype = c_float
    IMU_lib.LSM9DS1_getGyroY.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getGyroY.restype = c_float
    IMU_lib.LSM9DS1_getGyroZ.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getGyroZ.restype = c_float
    IMU_lib.LSM9DS1_getAccelX.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getAccelX.restype = c_float
    IMU_lib.LSM9DS1_getAccelY.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getAccelY.restype = c_float
    IMU_lib.LSM9DS1_getAccelZ.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getAccelZ.restype = c_float
    IMU_lib.LSM9DS1_getMagX.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getMagX.restype = c_float
    IMU_lib.LSM9DS1_getMagY.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getMagY.restype = c_float
    IMU_lib.LSM9DS1_getMagZ.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_getMagZ.restype = c_float
    IMU_lib.LSM9DS1_calcGyro.argtypes = [c_void_p, c_float]
    IMU_lib.LSM9DS1_calcGyro.restype = c_float
    IMU_lib.LSM9DS1_calcAccel.argtypes = [c_void_p, c_float]
    IMU_lib.LSM9DS1_calcAccel.restype = c_float
    IMU_lib.LSM9DS1_calcMag.argtypes = [c_void_p, c_float]
    IMU_lib.LSM9DS1_calcMag.restype = c_float
except:
    print("Unable to load IMU library. Doro will proceed without it.")

try:
    light_sensor_lib = load_lib('light_sensor.so')
    light_sensor_lib.get_light.restype = c_float
except:
    print("Unable to load light sensor library. Doro will proceed without it.")



# System initialization
try:
    motion_control_lib.initialize_pins()
    motion_control_lib.set_speed(20)
    system_status['Motion Control'] = on
except Exception as e:
    print("Failed to initialize motion control utilities: {} \nDORO will not be able to react to your command.".format(e))

try:
    imu = IMU_lib.LSM9DS1_create()
    IMU_lib.LSM9DS1_begin(imu)
    if IMU_lib.LSM9DS1_begin(imu) == 0:
        print("Failed to communicate with LSM9DS1.")
        exit()
    IMU_lib.LSM9DS1_calibrate(imu)
    system_status['IMU'] = on
except Exception as e:
    print("Failed to initialize IMU unit: {}. \nDORO will proceed without IMU functionalities".format(e))

try:
    light_sensor_lib.initialize_light_sensor()
    system_status['Light Sensor'] = on
except Exception as e:
    print("Failed to initialize light sensor: {}. \nDORO will proceed without light sensor functionalities")


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
    try:
        # if IMU_lib.LSM9DS1_accelAvailable(imu) == 0:
        IMU_lib.LSM9DS1_readAccel(imu)
        ax = IMU_lib.LSM9DS1_getAccelX(imu)
        ay = IMU_lib.LSM9DS1_getAccelY(imu)
        az = IMU_lib.LSM9DS1_getAccelZ(imu)
        ax = IMU_lib.LSM9DS1_calcAccel(imu, ax)
        ay = IMU_lib.LSM9DS1_calcAccel(imu, ay)
        az = IMU_lib.LSM9DS1_calcAccel(imu, ay)
        res = {
            'ax': ax,
            'ay': ay,
            'az': az
        }
        return res
    except Exception as e:
        return {
            "ERROR": e
        }

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


def get_light() -> float:
    res = light_sensor_lib.get_light()
    print("Light sensor: {}".format(res))

for (item, status) in system_status.items():
    print(" "*(15-len(item)) + item , ":", status)


# motion_control_lib testing script. Run this file to test functionality.
if __name__ == '__main__':
    from time import sleep
    set_speed(100)

    # go_straight()
    # print("going straight")
    # sleep(1)
    # print("Done. stopping...")
    # stop()
    # sleep(1)
    # turn_left()
    # print("turning left...")
    # sleep(1)
    # stop()
    # print("Done. stopping...")

    while True:
        print(get_light())
