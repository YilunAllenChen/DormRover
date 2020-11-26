#ifndef _VL53L0X_C_WRAPPER_H
#define _VL53L0X_C_WRAPPER_H

#include "VL53L0X.h"

extern "C" {
    VL53L0X* lidar_create();
    uint16_t lidar_get_distance(VL53L0X* obj);
}

#endif