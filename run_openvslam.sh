#!/bin/bash

if [[ -d openvslam-1 ]]
then
  echo "openvslam-1 already cloned"
else
  git clone --recursive https://github.com/Gizzatovamir/openvslam-1.git
fi
xhost +local:
# for debug purposes
docker-compose up --build openvslam
#docker-compose up openvslam