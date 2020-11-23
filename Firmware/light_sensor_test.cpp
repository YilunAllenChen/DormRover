#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>
<<<<<<< HEAD
#define light_sensor_read 17

=======

#define light_sensor_read 27
>>>>>>> 558ffb407b4c889aaed168e3affcfa2131056a30
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
<<<<<<< HEAD
			return 1;
		}
		else 
		{
			return 0;
=======
			return 1.0f;
		}
		else 
		{
			return 0.0f;
>>>>>>> 558ffb407b4c889aaed168e3affcfa2131056a30
		}
	}
}
*/
<<<<<<< HEAD
int main()
{	
	if (gpioInitialise() < 0)
		{
			return 0;
		};
	gpioSetMode(light_sensor_read, PI_INPUT);
	while(1){
	if(gpioRead(light_sensor_read))
	{
		printf("What Fuck");
		
	}
	else
	{
		printf("Nothing");
	}
	}
	
}
=======
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
>>>>>>> 558ffb407b4c889aaed168e3affcfa2131056a30
