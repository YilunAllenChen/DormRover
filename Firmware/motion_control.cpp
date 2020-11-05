#include "motion_control.h"
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
		gpioPWM(AmotorPWM, speed);
	}

	void set_right(int speedIn)
	{
		gpioWrite(BmotorInA, speedIn > 0 ? PI_ON : PI_OFF);
		gpioWrite(BmotorInB, speedIn > 0 ? PI_OFF : PI_ON);
		speed = speedIn > 0 ? speedIn : -speedIn;
		gpioPWM(BmotorPWM, speed);
	}
}