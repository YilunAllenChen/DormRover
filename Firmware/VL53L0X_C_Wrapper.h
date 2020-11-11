#ifndef _VL53L0X_C_WRAPPER_H
#define _VL53L0X_C_WRAPPER_H

#include "VL53L0X.h"

extern "C" {
    VL53L0X* lidar_create();
    void lidar_get_distance(VL53L0X* obj);
    // void lidar_initialize(VL53L0X* obj);
    // void lidar_powerOn(VL53L0X* obj);
    // void lidar_powerOff(VL53L0X* obj);
    // void lidar_setAddress(VL53L0X* obj);
    // inline uint8_t lidar_getAddress(VL53L0X* obj);
    // bool lidar_setSignalRateLimit(VL53L0X* obj);
    // float lidar_getSignalRateLimit(VL53L0X* obj);
    // bool lidar_setMeasurementTimingBudget(VL53L0X* obj);
    // uint32_t lidar_getMeasurementTimingBudget(VL53L0X* obj);
    // bool lidar_setVcselPulsePeriod(VL53L0X* obj);
    // uint8_t lidar_getVcselPulsePeriod(VL53L0X* obj);
    // void lidar_startContinuous(VL53L0X* obj);
    // void lidar_stopContinuous(VL53L0X* obj);
    // uint16_t lidar_readRangeContinuousMillimeters(VL53L0X* obj);
    // uint16_t lidar_readRangeSingleMillimeters(VL53L0X* obj);
    // inline void lidar_setTimeout(VL53L0X* obj);
    // inline uint16_t lidar_getTimeout(VL53L0X* obj);
    // bool lidar_timeoutOccurred(VL53L0X* obj);
}

#endif