#include "VL53L0X_C_Wrapper.h"
#include "VL53L0X.h"

// Create the sensor with default values
VL53L0X sensor;

VL53L0X* lidar_create()
{
    // Initialize the sensor
    sensor.initialize();
    // Set measurement timeout value
    sensor.setTimeout(0);
    // Lower the return signal rate limit (default is 0.25 MCPS)
    sensor.setSignalRateLimit(0.1);
    // Increase laser pulse periods (defaults are 14 and 10 PCLKs)
    sensor.setVcselPulsePeriod(VcselPeriodPreRange, 18);
    sensor.setVcselPulsePeriod(VcselPeriodFinalRange, 14);
    sensor.setMeasurementTimingBudget(200000);
    return &sensor;
}

uint16_t lidar_get_distance(VL53L0X* obj)
{
    return obj->readRangeSingleMillimeters();
}

