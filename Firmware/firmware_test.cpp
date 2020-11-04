#include "motion_control.h"
#include "LSM9DS1.h"

extern int speed;

int main(int argc, char *argv[])
{
	initialize_pins();
	set_speed(100);
	go_straight();
	sleep(1);
	stop();
	printf("Speed is %d\n", speed);
	LSM9DS1 IMU(IMU_MODE_I2C, 0x6b, 0x1e);
    IMU.begin();
	if (!IMU.begin()) {
        printf("Failed to communicate with LSM9DS1.\n");
		exit(EXIT_FAILURE);
    }
    IMU.calibrate(1);
	while(1) {
        while(!IMU.tempAvailable());
        IMU.readTemp();
        while(!IMU.magAvailable(X_AXIS));
        IMU.readMag();
        while(!IMU.accelAvailable());
        IMU.readAccel();
        while(!IMU.gyroAvailable());
        IMU.readGyro();
        printf("\nIMU Temperature = %f C\n\r",25.0 + IMU.temperature/16.0);
        printf("        X axis    Y axis    Z axis\n\r");
        printf("gyro:  %9f %9f %9f in deg/s\n\r", IMU.calcGyro(IMU.gx), IMU.calcGyro(IMU.gy), IMU.calcGyro(IMU.gz));
        printf("accel: %9f %9f %9f in Gs\n\r", IMU.calcAccel(IMU.ax), IMU.calcAccel(IMU.ay), IMU.calcAccel(IMU.az));
        printf("mag:   %9f %9f %9f in gauss\n\r", IMU.calcMag(IMU.mx), IMU.calcMag(IMU.my), IMU.calcMag(IMU.mz));
		sleep(1.0);
	}
	exit(EXIT_SUCCESS);
	return 0;
}

