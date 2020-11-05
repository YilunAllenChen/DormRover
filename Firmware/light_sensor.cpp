#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>
#define light_sensor_read 17

extern "C"
{
	void initialize_light_sensor()
	{
		if (gpioInitialise() < 0)
		{
			return;
		};
		gpioSetMode(light_sensor_read, PI_INPUT);
	}

	float get_light()
	{
		// set readIn pin as input
		if (gpioRead(light_sensor_read))
		{
			return 1;
		}
		else 
		{
			return 0;
		}
	}
}