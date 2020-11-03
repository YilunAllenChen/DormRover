#include <stdio.h>
#include <stdlib.h>
#include <pigpio.h> // include GPIO library
#include <signal.h> // needed to clean up CTL C abort
#include <sys/types.h>
#include <unistd.h>

#define LED 18 
#define AmotorInA 24
#define AmotorInB 23
#define BmotorInA 6
#define BmotorInB 5
#define AmotorPWM 12 
#define BmotorPWM 13

void initialize_pins(){
	gpioSetPWMrange(BmotorPWM,100);
	gpioSetPWMrange(AmotorPWM,100);
	gpioSetMode(BmotorInA, PI_OUTPUT);
	gpioSetMode(BmotorInB, PI_OUTPUT);
	gpioSetMode(BmotorPWM, PI_OUTPUT);
	gpioSetMode(AmotorInA, PI_OUTPUT);
	gpioSetMode(AmotorInB, PI_OUTPUT);
	gpioSetMode(AmotorPWM, PI_OUTPUT);
}

void reset(){
	gpioWrite(AmotorInA, PI_ON);
	gpioWrite(AmotorInB, PI_ON);
	gpioWrite(BmotorInA, PI_ON);
	gpioWrite(BmotorInB, PI_ON);
}

void set_left(int speed) {
	gpioWrite(AmotorInA, speed > 0 ? PI_ON : PI_OFF);
	gpioWrite(AmotorInB, speed > 0 ? PI_OFF : PI_ON);
	speed = speed > 0 ? speed : -speed;
	gpioPWM(AmotorPWM, speed);
}

void set_right(int speed) {
	gpioWrite(BmotorInA, speed > 0 ? PI_ON : PI_OFF);
	gpioWrite(BmotorInB, speed > 0 ? PI_OFF : PI_ON);
	speed = speed > 0 ? speed : -speed;
	gpioPWM(BmotorPWM, speed);
}

void straight(int dura, int speed){
	set_left(speed);
	set_right(speed);
	sleep(dura);
	reset();
}

void turn (int dura, int speed){
	set_left(-speed);
	set_right(speed);
	sleep(dura);
	reset();
}

int dim = 0;
int main(int argc, char *argv[])
{
   if (gpioInitialise()<0) return 1; // init I/O library

	initialize_pins();
   
    while(1){
	char c = getchar();
	
	if( c == 43 && dim < 100){
	   dim += 10; 
	}	
	else if (c == 45 && dim > -100){
	   dim -= 10;
	}
	
	if (c == 'w') straight(1, 100);
	if (c == 's') straight(1, -100);
	if (c == 'a') turn(1, 25);
	if (c == 'd') turn(1, -25);
	
	//printf("char: %d -> dim: %d\n",c, dim);
	set_left(dim);
   }  
   gpioTerminate();
   return 0;
}
