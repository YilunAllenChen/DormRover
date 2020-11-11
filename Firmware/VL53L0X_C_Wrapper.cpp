#include "VL53L0X_C_Wrapper.h"
#include "VL53L0X.h"

// Create the sensor with default values
VL53L0X sensor;

VL53L0X* lidar_create()
{
    // Initialize the sensor
    sensor.initialize();
    // Set measurement timeout value
    sensor.setTimeout(200);
    // Lower the return signal rate limit (default is 0.25 MCPS)
    sensor.setSignalRateLimit(0.1);
    // Increase laser pulse periods (defaults are 14 and 10 PCLKs)
    sensor.setVcselPulsePeriod(VcselPeriodPreRange, 18);
    sensor.setVcselPulsePeriod(VcselPeriodFinalRange, 14);
    sensor.setMeasurementTimingBudget(200000);
    return &sensor;
    // return new VL53L0X;
}

// void lidar_initialize(VL53L0X* obj)
// {
//     obj->initialize();
// }

uint16_t lidar_get_distance(VL53L0X* obj)
{
    return obj->readRangeSingleMillimeters();
}

