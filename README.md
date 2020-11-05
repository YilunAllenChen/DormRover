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
--TODO--

## Software Setup
1. Ready your Raspberry Pi (3 or above recommended)
2. Pull this repository onto your Pi.
3. Run `./setup` command. This only needs to be run once for installing necessary utilities.
    - After the first `setup` run, later on after you make modifications to the program you could just run `.build` to re-compile the program without reinstalling everything.
5. Run `backend.py` to start the server
6. In your Pi terminal use `ifconfig` to get your IP address
7. Access the web GUI from your computer by going to the IP address with ":5000" appended.
8. Use WASD to control the robot and have fun.

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



# Useful Commands

## Compile C++ code into a shared library:
`gcc -shared -fPIC -lpigpio -lrt firmware.cpp -o firmware.so`
Note:
- `-shared -fPIC`: specify the firmware to be a shared library
- `-lpigpio -lrt`: include libraries required by the firmware program

## Web development
Rename static html file into `index.html` and put it under `frontend/`.

# References
Want to learn more about the tech stack? Here are some useful links:

### [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) Hello World program
### [Video Streaming](https://blog.miguelgrinberg.com/post/video-streaming-with-flask) with Flask
### Using [ctypes](https://realpython.com/python-bindings-overview/#ctypes) to call c++ shared libraries
