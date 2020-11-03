# NOTE: Run this with sudo!

# Build the firmware
# compile to run (no share flag)
# g++ -lpigpio -lrt -lwiringPi firmware.cpp LSM9DS1.cpp -o firmware.so
# g++ -Wall -O2 -shared -fPIC -c -lrt -lwiringPi LSM9DS1.cpp -o IMU.so
g++ -shared -fPIC -lpigpio -lrt -lwiringPi firmware.cpp LSM9DS1.cpp -o firmware.so
# gcc -shared -fPIC -lpigpio -lrt firmware.cpp -o firmware.so
pip3 install -r requirements./txt

# # Full stack environment
# python3 backend.py

# # Firmware Testing environment
python3 interface.py