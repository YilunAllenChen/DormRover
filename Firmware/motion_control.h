#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>
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

	//More coming soon (like cyberpunk 2077)
}
