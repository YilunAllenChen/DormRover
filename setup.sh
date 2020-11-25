#!/bin/bash
# Environment
sudo apt install -y python3
sudo apt install -y python-setuptools python3-setuptools

# Python libraries
sudo pip3 install -r requirements.txt

# pigpio
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
cd ..
rm -rf pigpio_master

cd Frontend
npm install

bash build.sh