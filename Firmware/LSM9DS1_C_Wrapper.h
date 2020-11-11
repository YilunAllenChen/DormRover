#ifndef __SparkFunLSM9DS1_C_WRAPPER_H__
#define __SparkFunLSM9DS1_C_WRAPPER_H__

#include "LSM9DS1.h"

extern "C" {
    LSM9DS1* LSM9DS1_create();
    void LSM9DS1_begin(LSM9DS1* obj);
    void LSM9DS1_calibrate(LSM9DS1* obj);
    // Chack imu
    int LSM9DS1_gyroAvailable(LSM9DS1* obj);
    int LSM9DS1_accelAvailable(LSM9DS1* obj);
    int LSM9DS1_magAvailable(LSM9DS1* obj);
    // Read data
    void LSM9DS1_readGyro(LSM9DS1* obj);
    void LSM9DS1_readAccel(LSM9DS1* obj);
    void LSM9DS1_readMag(LSM9DS1* obj);
    float LSM9DS1_readTemp(LSM9DS1* obj);
    // Get data
    float LSM9DS1_getGyroX(LSM9DS1* obj);
    float LSM9DS1_getGyroY(LSM9DS1* obj);
    float LSM9DS1_getGyroZ(LSM9DS1* obj);
    float LSM9DS1_getAccelX(LSM9DS1* obj);
    float LSM9DS1_getAccelY(LSM9DS1* obj);
    float LSM9DS1_getAccelZ(LSM9DS1* obj);
    float LSM9DS1_getMagX(LSM9DS1* obj);
    float LSM9DS1_getMagY(LSM9DS1* obj);
    float LSM9DS1_getMagZ(LSM9DS1* obj);
    // Compute data
    float LSM9DS1_calcGyro(LSM9DS1* obj, float gyro);
    float LSM9DS1_calcAccel(LSM9DS1* obj, float accel);
    float LSM9DS1_calcMag(LSM9DS1* obj, float mag);
}

#endif /* __SparkFunLSM9DS1_C_WRAPPER_H__ */