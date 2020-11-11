'''
Firmware wrapper to bundle all c++ libraries together for backend to use.
'''

from ctypes import *
import ctypes
import pathlib
# Initialize sensor status reports

on = '[\33[92m  ON  \33[0m]'
off = '[\33[91m OFF  \33[0m]'
unavailable = '[\33[93m N/A  \33[0m]'
system_status = {
    'Motion Control': off,
    'IMU': off,
    'Light Sensor': off,
    'Camera': off,
    'Lidar': off
}


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Load all libraries and define their argument types and return types
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

try:
    from camera_utils import vid_gen
    system_status['Camera'] = on
except:
    pass


def load_lib(libname: str):
    '''
    Helper function to load a shared C library
    '''
    try:
        libname = str(pathlib.Path().absolute() / "Firmware" / libname)
        return ctypes.CDLL(libname)
    except Exception as e:
        print("[\33[91m ERROR \33[0m]: Library {} could not be loaded: {}".format(
            libname, e))


# motion control library
try:
    motion_control_lib = load_lib('motion_control.so')
    motion_control_lib.set_speed.argtypes = [ctypes.c_int]
except:
    print("Unable to load motion control libraries. Doro will proceed without it.")

# IMU library
try:
    IMU_lib = load_lib('IMU.so')
    IMU_lib.LSM9DS1_create.argtypes = []
    IMU_lib.LSM9DS1_create.restype = c_void_p
    IMU_lib.LSM9DS1_begin.argtypes = [c_void_p]
    IMU_lib.LSM9DS1_begin.restype = None
    IMU_lib.LSM9DS1_readTemp.restype = c_float
    IMU_lib.LSM9DS1_readTemp.argtypes = [c_void_p]
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

# light sensor library
try:
    light_sensor_lib = load_lib('light_sensor.so')
    light_sensor_lib.get_light.restype = c_float
except:
    print("Unable to load light sensor library. Doro will proceed without it.")

# lidar library
try:
    lidar_lib = load_lib('lidar.so')
    lidar_lib.lidar_create.restype = c_void_p
    lidar_lib.lidar_get_distance.argtypes = [c_void_p]
    lidar_lib.lidar_get_distance.restype = c_uint16
except:
    print("Unable to load lidar library. Doro will proceed without it.")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                Library utilities initialization and setup
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# motion control library
try:
    motion_control_lib.initialize_pins()
    motion_control_lib.set_speed(20)
    system_status['Motion Control'] = on
except Exception as e:
    print("Failed to initialize motion control utilities: {} \nDORO will not be able to react to your command.".format(e))

# IMU library
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

# Light sensor library
try:
    light_sensor_lib.initialize_light_sensor()
    system_status['Light Sensor'] = on
except Exception as e:
    print("Failed to initialize light sensor: {}. \nDORO will proceed without light sensor functionalities".format(e))


try:
    lidar = lidar_lib.lidar_create()
    system_status['Lidar'] = on
except Exception as e:
    print("Failed to initialize lidar: {}. \nDORO will proceed without light sensor functionalities".format(e))


# print out sensor system status
print("\n", "*"*14, "Sensor System Status", "*"*14)
for (item, status) in system_status.items():
    print(" "*(15-len(item)) + item, ":", status)
print("*"*50, '\n')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                        Wrapper function definitions
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def get_IMU() -> dict:
    '''
    Function uses pre-built c++ libraries and obtain all data obtained by the IMU sensor.

    :return: returns a dictionary of all data.
        Example format: 
        {
            'gx': 1.2,
            'ay': 3.2,
            'mz': 1.1
        }
    '''
    try:
        IMU_lib.LSM9DS1_readAccel(imu)
        IMU_lib.LSM9DS1_readMag(imu)
        IMU_lib.LSM9DS1_readGyro(imu)
        ax = IMU_lib.LSM9DS1_calcAccel(imu, IMU_lib.LSM9DS1_getAccelX(imu))
        ay = IMU_lib.LSM9DS1_calcAccel(imu, IMU_lib.LSM9DS1_getAccelY(imu))
        az = IMU_lib.LSM9DS1_calcAccel(imu, IMU_lib.LSM9DS1_getAccelZ(imu))
        mx = IMU_lib.LSM9DS1_calcMag(imu, IMU_lib.LSM9DS1_getMagX(imu))
        my = IMU_lib.LSM9DS1_calcMag(imu, IMU_lib.LSM9DS1_getMagY(imu))
        mz = IMU_lib.LSM9DS1_calcMag(imu, IMU_lib.LSM9DS1_getMagZ(imu))
        gx = IMU_lib.LSM9DS1_calcGyro(imu, IMU_lib.LSM9DS1_getGyroX(imu))
        gy = IMU_lib.LSM9DS1_calcGyro(imu, IMU_lib.LSM9DS1_getGyroY(imu))
        gz = IMU_lib.LSM9DS1_calcGyro(imu, IMU_lib.LSM9DS1_getGyroZ(imu))
        return {
            'ax': ax,
            'ay': ay,
            'az': az,
            'mx': mx,
            'my': my,
            'mz': mz,
            'gx': gx,
            'gy': gy,
            'gz': gz
        }
    except Exception as e:
        return {
            "ERROR": str(e)
        }


def get_temp() -> float:
    '''
    Function uses pre-built c++ libraries and obtain temperature
    '''
    try:
        return (IMU_lib.LSM9DS1_readTemp(imu) / 16 + 25)
    except Exception as e:
        return -9999

def get_lidar() -> int:
    '''
    Function uses pre-built c++ libraries to obtain distance to nearby objects with its lidar sensor.
    '''
    return lidar_lib.lidar_get_distance(lidar)

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
    try:
        res = light_sensor_lib.get_light()
        print("Light sensor: {}".format(res))
        return res
    except:
        return -9999

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
        # print(get_light())
        print('imu', get_IMU())
        print('temp', get_temp())
