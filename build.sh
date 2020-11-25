#!/bin/bash

# Firmware compilation
cd Firmware
make
cd ..

cd Frontend
npm run-script build
cd ..
