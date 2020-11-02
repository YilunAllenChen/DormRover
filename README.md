# DormRover
web-based remote control rover robot.

# Development Notes

## Compile C++ code into a shared library:
`gcc -shared -fPIC -lpigpio -lrt firmware.cpp -o firmware.so`
Note:
- `-shared -fPIC`: specify the firmware to be a shared library
- `-lpigpio -lrt`: include libraries required by the firmware program

## Web development
Rename static html file into `index.html` and put it under `frontend/`.


# Setup
## Installation
pip3 install -r requirements.txt