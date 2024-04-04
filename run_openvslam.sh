#!/bin/bash

if [[ -d openvslam-1 ]]
then
  echo "openvslam-1 already cloned"
else
  git clone --recursive https://github.com/Gizzatovamir/openvslam-1.git
fi
xhost +local:
docker-compose up --build openvslam