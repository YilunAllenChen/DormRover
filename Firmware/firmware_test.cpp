#include "motion_control.h"
#include "LSM9DS1.h"
#include "math.h"

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
    double a = 0.0;
	while(1) {
        while(!IMU.tempAvailable());
        IMU.readTemp();
        while(!IMU.accelAvailable());
        IMU.readAccel();
        a = sqrt(IMU.calcAccel(IMU.ax) * IMU.calcAccel(IMU.ax) + IMU.calcAccel(IMU.ay) * IMU.calcAccel(IMU.ay) + IMU.calcAccel(IMU.az) * IMU.calcAccel(IMU.az));
        printf("\nIMU Temperature = %f C\n\r",25.0 + IMU.temperature/16.0);
        printf("        X axis    Y axis    Z axis\n\r");
        printf("accel: %9f %9f %9f in Gs\n\r", IMU.calcAccel(IMU.ax), IMU.calcAccel(IMU.ay), IMU.calcAccel(IMU.az));
		printf("accel: %9f in Gs\n\r", a);
        
        sleep(1.0);
	}
	exit(EXIT_SUCCESS);
	return 0;
}

