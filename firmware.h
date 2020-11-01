extern "C"
{
	void set_speed(int speed);
	// Set speed for both motors

	void go_straight();
	void go_backward();
	void turn_left();
	void turn_right();
	// The functions above should run forever until stop()

	void stop();
	// hard-stop all motors

	float get_velocity_x();
	float get_velocity_y();
	float get_acceleration_x();
	float get_acceleration_y();
	// All functions above are local-frame based raw data

	float get_temperature();


	//More coming soon (like cyberpunk 2077)
}
