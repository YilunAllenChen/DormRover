# "DORO" Dorm Rover

DORO is a web-based RC rover robot. It allows users to access the data acqured by the rover's camera and any other onboard sensors as well as motion control systems via a web GUI.

Ever aspired to have your own Mars Rover? Using your own raspberry Pi you sure can!


Project Contributers:  
Firmware: 
[Yida Wang](https://github.com/savage12138),
[Xi Li](https://github.com/tianran-xi)  
Backend:
[Yilun Chen](https://github.com/YilunAllenChen)  
Frontend:
[Charlie Chu](https://github.com/czjcha)


# Project Architecture
The project consists three major parts:
- Firmware (C/C++): Low-level module that takes care of the interaction with GPIOs. Firmware encapsulates numerous functions (go forward, read sensor data, etc.) and expose them to the Backend module to use.
- Backend (Python): Web server that reacts to RESTful API calls from the Frontend module and handles them by calling corresponding Firmware utilities. The server uses the `Flask` framework and uses `ctypes` for data marshalling when calling C++ shared libraries
- Frontend (JavaScript): Static web page that takes care of different keyboard and mouse events and call corresponding RESTful APIs to notify the Backend Module.

# Project Setup

## Hardware Setup

![Image of Yaktocat](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Header-with-Photo-702x336.png)   
Figure 1. Raspberry Pi pinout   
The pin number discussed in the following section will be referred to the pinout picture above. Please read the number labelled as GPIOxx rather than number circled in the middle   

### Motion Control
#### Components
2 motors and Dual H-bridge (TB6612)
![Image of Yaktocat](https://i2.wp.com/dronebotworkshop.com/wp-content/uploads/2019/12/TB6612FNG-pinout.jpeg?w=768&ssl=1)   
Figure 2. Dual H-briage   
![Image of Yaktocat](https://opencircuit.shop/resources/content/4d31362984068/crop/1900-950/DC-Geared-Motor.webp)   
Figure 3. Motors used in Motion Control   
![Image of Yaktocat](https://www.cytron.io/image/catalog/products/HD-BSC-2WD/HD-BSC-2WD.jpg)   
Figure 4 Chassis and motor position   
#### Connection
Motion Control take 6 pins. Among them, 5,6,24 and 23 are digital output pins, and 12 and 13 are PWM output pins.   
The PWMA pin on the TB6612 in Figure 3 is connected to the raspberry pi 12   
The PWMB pin on the TB6612 in Figure 3 is connected to the raspberry pi 13   
The BI1 pin on the TB6612 in Figure 3 is connected to the raspberry pi 6   
The BI2 pin on the TB6612 in Figure 3 is connected to the raspberry pi 5  
The AI1 pin on the TB6612 in Figure 3 is connected to the raspberry pi 24   
The AI2 pin on the TB6612 in Figure 3 is connected to the raspberry pi 23
The A01 pin and A02 pin on the TB6612 in Figure 3 are connected to the motor on the left as shown in Figure 4   
The B01 pin and B02 pin on the TB6612 in Figure 3 are connected to the motor on the right as shown in Figure 4
The GROUND pin on the TB6612 in Figure 3 is connected to the common ground   
The VM and VCC are ahd STBY pins on the TB6612 are connected to the 5v power line   



### Servo   
#### Components   
![Image of Yaktocat](https://os.mbed.com/media/uploads/4180_1/htservo.jpg)   
Figure 5 Servo appearance   

![Image of Yaktocat](https://os.mbed.com/media/uploads/4180_1/servocable.png)   
Figure 6 Servo Wire Connection   
#### Connection
As shown in Figure 5, the servo has three wires. Black wire is connected to the common ground, and the red wire is connected to the 5v power line. The yellow signal wire is connected to the GPIO 18 of raspberry pi.
### IMU
![Image of Yaktocat](https://cdn.sparkfun.com//assets/parts/1/1/6/3/3/13944-01.jpg)
Figure 7 The SparkFun 9DoF Sensor Stick (IMU)
**Table 1**
| Raspberry Pi 4  |   IMU  | 
|-----------------|--------|
|     **3.3V**    | **VDD**| 
|     **GND**     | **GND**|
|     **GPIO2**   | **SDA**|
|     **GPIO3**   | **SCL**|
### lidar sensor
--TODO-- [Xi Li, Yida Wang]

## Software Setup
1. Ready your Raspberry Pi (3 or above recommended)
2. Pull this repository onto your Pi.
3. Run `./setup` command. This only needs to be run once for installing necessary utilities.
    - After the first `setup` run, later on after you make modifications to the program you could just run `.build` to re-compile the program without reinstalling everything.
5. Run `sudo python3 backend.py` to start the server.
6. You should be able to see DORO's sensor system status as well as where DORO is serving its website. Access that url using your favorite browser.

# Development Notes
### 2020.10.27
- Prototyped the physical rover 
    - External battery
    - Two DC motors
    - Dual-H-brdge
- Developed generic motion control functions using pigpio
- Tested motion control capabilities using vnc

### 2020.11.1
- Team meeting. Decided on the software architecture of the project.
- Prototyped another rover
- Created Backend module and enabled bindings
- Encapsulated motion control functions
- Tested motion control functions

### 2020.11.3
- Created IMU libraries 
- Reorganized repos
- Improved Readme

### 2020.11.1
- Created generic frontend for testing
- Improved backend functionality and exception handling with malfunctioning libraries

### 2020.11.10
- Created firmware for lidar sensors
- Integrated lidar firmware and created corresponding wrapper functions and backend APIs

### 2020.11.15
- Frontend v1.0 done. 
- Added static files serving functionalities to backend.

### 2020.11.23
- Created firmware for servos   
- Integrated servos firmware and created corresponding wrapper functions and backend APIs
# References
Want to learn more about the tech stack? Here are some useful links:

### [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) Hello World program
### [Video Streaming](https://blog.miguelgrinberg.com/post/video-streaming-with-flask) with Flask
### Using [ctypes](https://realpython.com/python-bindings-overview/#ctypes) to call c++ shared libraries
