#include "LSM9DS1_C_Wrapper.h"
#include "LSM9DS1.h"

LSM9DS1* LSM9DS1_create() {
    return new LSM9DS1(IMU_MODE_I2C, 0x6b, 0x1e);
}

void LSM9DS1_begin(LSM9DS1* obj) {
    obj->begin();
}

void LSM9DS1_calibrate(LSM9DS1* obj) {
    obj->calibrate();
}

int LSM9DS1_gyroAvailable(LSM9DS1* obj) {
    return obj->gyroAvailable();
}

int LSM9DS1_accelAvailable(LSM9DS1* obj) {
    return obj->accelAvailable();
}

int LSM9DS1_magAvailable(LSM9DS1* obj) {
    return obj->magAvailable();
}

void LSM9DS1_readGyro(LSM9DS1* obj) {
    obj->readGyro();
}

void LSM9DS1_readAccel(LSM9DS1* obj) {
    obj->readAccel();
}

void LSM9DS1_readMag(LSM9DS1* obj) {
    obj->readMag();
}

void LSM9DS1_readTemp(LSM9DS1* obj) {
    obj->readTemp();
}

float LSM9DS1_getGyroX(LSM9DS1* obj) {
    return obj->gx;
}
float LSM9DS1_getGyroY(LSM9DS1* obj) {
    return obj->gy;
}
float LSM9DS1_getGyroZ(LSM9DS1* obj) {
    return obj->gz;
}

float LSM9DS1_getAccelX(LSM9DS1* obj) {
    return obj->ax;
}
float LSM9DS1_getAccelY(LSM9DS1* obj) {
    return obj->ay;
}
float LSM9DS1_getAccelZ(LSM9DS1* obj) {
    return obj->az;
}

float LSM9DS1_getMagX(LSM9DS1* obj) {
    return obj->mx;
}
float LSM9DS1_getMagY(LSM9DS1* obj) {
    return obj->my;
}
float LSM9DS1_getMagZ(LSM9DS1* obj) {
    return obj->mz;
}

float LSM9DS1_calcGyro(LSM9DS1* obj, float gyro) {
    return obj->calcGyro(gyro);
}
float LSM9DS1_calcAccel(LSM9DS1* obj, float accel) {
    return obj->calcAccel(accel);
}
float LSM9DS1_calcMag(LSM9DS1* obj, float mag) {
    return obj->calcMag(mag);
}
