#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>

#define light_sensor_read 27
/*
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
			return 1.0f;
		}
		else 
		{
			return 0.0f;
		}
	}
}
*/
int main ()
{
    if(gpioInitialise() < 0)
    {
        return 0;
    }
    gpioSetMode(light_sensor_read, PI_INPUT);
    while (1)
    {
        // printf("light sensor: %f \n", get_light());
        // sleep(1);
        if (gpioRead(light_sensor_read))
        {
            printf("1.0\n");
			sleep(0.01);
        }
        else
        {
            printf("0.0\n");
			sleep(0.01);
        }
    }
}