#include "motion_control.h"
#include "LSM9DS1.h"
#include "math.h"
#include "VL53L0X.h"
#include "light_sensor.cpp"
extern int speed;

int main(int argc, char *argv[])
{
	initialize_pins();
    // LSM9DS1 IMU(IMU_MODE_I2C, 0x6b, 0x1e);
	// set_speed(100);
	// go_straight();
	// sleep(1);
	// stop();
	// printf("Speed is %d\n", speed);

    // IMU.begin();
	// if (!IMU.begin()) {
    //     printf("Failed to communicate with LSM9DS1.\n");
	// 	exit(EXIT_FAILURE);
    // }
    // IMU.calibrate(1);

     // Create the sensor with default values
    VL53L0X sensor;
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

    // double a = 0.0;
    uint16_t distance;
	while(1) {
        // while(!IMU.tempAvailable());
        // IMU.readTemp();
        // while(!IMU.accelAvailable());
        // IMU.readAccel();
        // // a = sqrt(IMU.calcAccel(IMU.ax) * IMU.calcAccel(IMU.ax) + IMU.calcAccel(IMU.ay) * IMU.calcAccel(IMU.ay) + IMU.calcAccel(IMU.az) * IMU.calcAccel(IMU.az));
        // printf("\nIMU Temperature = %f C\n\r",25.0 + IMU.temperature/16.0);
        // printf("        X axis    Y axis    Z axis\n\r");
        // printf("accel: %9f %9f %9f in Gs\n\r", IMU.calcAccel(IMU.ax), IMU.calcAccel(IMU.ay), IMU.calcAccel(IMU.az));
		// printf("accel: %9f in Gs\n\r", a);
        distance = sensor.readRangeSingleMillimeters();
        printf("\rReading: %d \n", distance);
        sleep(1.0);
        printf("light sensor: %f \n", get_light());
	}
	exit(EXIT_SUCCESS);
	return 0;
}

