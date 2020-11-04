#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>
#define sensorRead 17
#define lightControl 27
int result = 0;

extern "C"
{
	void initialize_pins()
	{
		if (gpioInitialise() < 0)
		{
			return;
		};
		gpioSetMode(sensorRead, PI_INPUT);
	}

	float lightSensor()
	{
		// set readIn pin as input
		if (gpioRead(sensorRead))
		{
			return 1;
		}
		else if (!gpioRead(sensorRead))
		{
			return 0;
		}
		return 0;
	}
}
/*
int main()
{
	if (gpioInitialise() < 0)
{
   // pigpio initialisation failed.
    printf("Fail");
   return 0;
  
}
gpioSetMode(sensorRead, PI_INPUT); // set readIn pin as input
gpioSetMode(lightControl, PI_OUTPUT); // set control out pin as output
gpioSetPWMrange(lightControl, 100);
gpioWrite(lightControl,PI_OFF);
while(1){
	
	if(gpioRead(sensorRead))
	{result = 1;
		printf("Fuck YOU! I can see nothing!!!! \n");
		gpioWrite(lightControl,result);
		sleep(0.01);
		}
	else if(!gpioRead(sensorRead)){result = 0;}
	gpioWrite(lightControl,result);
	}
}
*/
