CC = g++
CFLAGS = -O2 -g

.PHONY: all
all: IMU.so motion_control.so firmware.so light_sensor.so

motion_control.so: motion_control.cpp
	$(CC) -Wall -O2 -shared -lpigpio -lrt motion_control.cpp -o motion_control.so

LSM9DS1.o: LSM9DS1.cpp
	$(CC) -Wall -O2 -fPIC -c -lwiringPi LSM9DS1.cpp -o LSM9DS1.o

# dynamic library

LSM9DS1_C_Wrapper.o: LSM9DS1_C_Wrapper.cpp
	$(CC) -Wall -O2 -fPIC -c -lwiringPi LSM9DS1_C_Wrapper.cpp -o LSM9DS1_C_Wrapper.o


IMU.so: LSM9DS1_C_Wrapper.o LSM9DS1.o
	$(CC) -Wall -O2 -shared -lwiringPi LSM9DS1.o LSM9DS1_C_Wrapper.o -o IMU.so

firmware.so: firmware_test.cpp
	$(CC) -Wall -O2 -fPIC -lwiringPi -lpigpio -lrt *.cpp -o firmware.so

light_sensor.so: light_sensor.cpp
	$(CC) -Wall -O2 -shared -lpigpio -lrt light_sensor.cpp -o light_sensor.so

clean:
	rm -f *.o *.so