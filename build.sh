#!/bin/bash
# Environment
sudo apt install -y python3
sudo apt install -y python-setuptools python3-setuptools


# pigpio
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
cd ..
rm -rf pigpio_master

# Firmware compilation
cd Firmware
g++ -shared -fPIC -lpigpio -lwiringPi -lrt *.cpp -o firmware.so