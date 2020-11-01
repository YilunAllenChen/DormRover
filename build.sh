# Run this with sudo

apt install python3-dev -y
pip3 install -r requirements.txt
g++ -shared *.cpp -o lib.so