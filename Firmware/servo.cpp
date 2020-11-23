
#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>
#include "LSM9DS1.h"
#define servoPWM 18
float turn = 7;
int c;

extern "C"
{
	void servo_initialize_pins()
	{
		if (gpioInitialise() < 0){
			return;
		};
		gpioSetPWMrange(servoPWM, 100);
		gpioSetMode(servoPWM, PI_OUTPUT);
		gpioSetPWMfrequency(servoPWM, 50);
		gpioPWM(servoPWM,turn);
		sleep(0.1);
	}
	
	void servo_return_to_middle()
	{
		turn = 7;
		gpioPWM(servoPWM,turn);
		sleep(0.1);
	}
	void servo_turn_left()
	{
		if (turn > 2)
		{
			turn -= 1;
		}
		gpioPWM(servoPWM,turn);
		sleep(0.1);
	}
	void servo_turn_right()
	{
		if(turn < 13)
		{
			turn +=1;
		}
		gpioPWM(servoPWM,turn);
		sleep(0.1);
	}
		
	
}
/*
void middle()
{
	turn = 7;
}
void left()
{
	if (turn > 2)
	{
		turn -= 1;
	}
}
void right()
{
	if(turn < 13)
	{
		turn +=1;
	}
}
int main()
{	gpioTerminate();
	if (gpioInitialise() < 0){
		printf("Not initialise");
		return 0;
	}
	else
	{
		gpioSetPWMrange(servoPWM, 100);
		gpioSetMode(servoPWM, PI_OUTPUT);
		gpioSetPWMfrequency(servoPWM, 50);
	}
while(1){
		printf("enter here: ");
		c = getchar();
		switch(c)
		{
			case '1' : 	left() ; break;
			case '2' : 	middle() ; break;
			case '3' : 	right() ; break;
		}
			
	gpioPWM(servoPWM,turn);
	sleep(0.1);
	//gpioPWM(servoPWM,);

}

	//gpioPWM(servoPWM,5);
	
	
	printf("C");
	sleep(1);
	printf("C");
	return 0;
}		
*/
