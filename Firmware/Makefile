CC = g++
CFLAGS = -O2 -g

.PHONY: all
all: IMU.so motion_control.so light_sensor.so lidar.so firmware.so servo.so

LSM9DS1.o: LSM9DS1.cpp
	$(CC) -Wall -O2 -fPIC -c -lwiringPi LSM9DS1.cpp -o LSM9DS1.o

firmware.so: firmware_test.cpp
	$(CC) -Wall -O2 -fPIC -lwiringPi -lpigpio -lrt LSM9DS1.cpp motion_control.cpp VL53L0X.cpp firmware_test.cpp -o firmware.so

VL53L0X.o: VL53L0X.cpp
	$(CC) -Wall -O2 -fPIC -c VL53L0X.cpp -o VL53L0X.o
	
# dynamic library

motion_control.so: motion_control.cpp
	$(CC) -Wall -O2 -shared -lpigpio -lrt motion_control.cpp -o motion_control.so

LSM9DS1_C_Wrapper.o: LSM9DS1_C_Wrapper.cpp
	$(CC) -Wall -O2 -fPIC -c -lwiringPi LSM9DS1_C_Wrapper.cpp -o LSM9DS1_C_Wrapper.o

IMU.so: LSM9DS1_C_Wrapper.o LSM9DS1.o
	$(CC) -Wall -O2 -shared -lwiringPi LSM9DS1.o LSM9DS1_C_Wrapper.o -o IMU.so

light_sensor.so: light_sensor.cpp
	$(CC) -Wall -O2 -shared -lpigpio -lrt light_sensor.cpp -o light_sensor.so

VL53L0X_C_Wrapper.o: VL53L0X_C_Wrapper.cpp
	$(CC) -Wall -O2 -fPIC -c VL53L0X_C_Wrapper.cpp -o VL53L0X_C_Wrapper.o

lidar.so: VL53L0X_C_Wrapper.o VL53L0X.o
	$(CC) -Wall -O2 -shared VL53L0X.o VL53L0X_C_Wrapper.o -o lidar.so

servo.so: servo.cpp
	$(CC) -Wall -O2 -shared -lpigpio -lrt servo.cpp -o servo.so

clean:
	rm -f *.o *.so
