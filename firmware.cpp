#include "firmware.h"
#define LED 18
#define AmotorInA 24
#define AmotorInB 23
#define BmotorInA 6
#define BmotorInB 5
#define AmotorPWM 12
#define BmotorPWM 13

extern "C"
{
	int speed = 0;
	void initialize_pins()
	{
		if (gpioInitialise() < 0){
			return;
		};
		gpioSetPWMrange(BmotorPWM, 100);
		gpioSetPWMrange(AmotorPWM, 100);
		gpioSetMode(BmotorInA, PI_OUTPUT);
		gpioSetMode(BmotorInB, PI_OUTPUT);
		gpioSetMode(BmotorPWM, PI_OUTPUT);
		gpioSetMode(AmotorInA, PI_OUTPUT);
		gpioSetMode(AmotorInB, PI_OUTPUT);
		gpioSetMode(AmotorPWM, PI_OUTPUT);
	}

	void set_speed(int new_speed)
	{
		speed = new_speed;
	}

	void go_straight()
	{
		set_left(speed);
		set_right(speed);
	}

	void go_backward()
	{
		set_left(-speed);
		set_right(-speed);
	}
	
	void turn_left()
	{
		set_left(speed);
		set_right(-speed);
	}
	
	void turn_right()
	{
		set_left(-speed);
		set_right(+speed);
	}

	void stop()
	{
		gpioWrite(AmotorInA, PI_ON);
		gpioWrite(AmotorInB, PI_ON);
		gpioWrite(BmotorInA, PI_ON);
		gpioWrite(BmotorInB, PI_ON);
	}
	void set_left(int speedIn)
	{
		gpioWrite(AmotorInA, speedIn > 0 ? PI_ON : PI_OFF); //yes, pick one after ?, no, pick one after :
		gpioWrite(AmotorInB, speedIn > 0 ? PI_OFF : PI_ON);
		speed = speedIn > 0 ? speedIn : -speedIn;
		gpioPWM(AmotorPWM, speedIn);
	}

	void set_right(int speedIn)
	{
		gpioWrite(BmotorInA, speedIn > 0 ? PI_ON : PI_OFF);
		gpioWrite(BmotorInB, speedIn > 0 ? PI_OFF : PI_ON);
		speed = speedIn > 0 ? speedIn : -speedIn;
		gpioPWM(BmotorPWM, speedIn);
	}
	float get_velocity_x()
	{
		return 0;
	}
	float get_velocity_y()
	{
		return 0;
	}
	float get_acceleration_x()
	{
		return 0;
	}
	float get_acceleration_y()
	{
		return 0;
	}

	float get_temperature()
	{
		return 0;
	}


	
}
int main(int argc, char *argv[])
{
	initialize_pins();
	set_speed(100);
	go_straight();
	sleep(1);
	stop();
	printf("Speed is %d\n", speed);
	LSM9DS1 IMU(IMU_MODE_I2C, 0x6B, 0x1E);
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

