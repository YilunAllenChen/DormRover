#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include "LSM9DS1_Types.h"
#include "LSM9DS1.h"
extern "C"
{
	void initialize_pins();
	void set_speed(int);
	// Set speed for both motors

	void go_straight();
	void go_backward();
	void turn_left();
	void turn_right();
	// The functions above should run forever until stop()

	void stop();
	// hard-stop all motors

	void set_left(int);
	void set_right(int);
	float get_velocity_x();
	float get_velocity_y();
	float get_acceleration_x();
	float get_acceleration_y();
	// All functions above are local-frame based raw data

	float get_temperature();


	//More coming soon (like cyberpunk 2077)
}
