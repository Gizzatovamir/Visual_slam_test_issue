#!/bin/bash

xhost +local:
docker run -it --rm -e DISPLAY=$DISPLAY \
      --volume /tmp/.X11-unix/:/tmp/.X11-unix:ro \
      --volume ./data/dataset:/dataset:ro \
      --volume ./data/vocab:/vocab:ro \
      --volume ./data/configs:/configs:ro \
      --volume ./data/result:/result \
      --entrypoint ./run_video_slam stella_vslam-desktop \
      --vocab /vocab/orb_vocab.fbow --video /dataset/20240327_161347_448.mp4 --config /configs/equirect.yaml --map-db-out /result/1.msg\
      /

