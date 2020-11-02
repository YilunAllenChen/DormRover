# NOTE: Run this with sudo!

# Build the firmware
gcc -shared -fPIC -lpigpio -lrt firmware.cpp -o firmware.so
pip3 install -r requirements./txt

# # Full stack environment
# python3 backend.py

# # Firmware Testing environment
python3 interface.py