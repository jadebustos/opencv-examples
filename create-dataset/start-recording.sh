#!/bin/bash

# configure according to your environment
MY_VIDEO_INDEX=5
MY_MODULUS=17
MY_RANDOM_RANGE=101
MY_IMAGE_SIZE=400
MY_WIDTH=1920
MY_HEIGHT=1080

podman run --rm --env VIDEO_INDEX=$MY_VIDEO_INDEX --env MODULUS=$MY_MODULUS \
           --env RANDOM_RANGE=$MY_RANDOM_RANGE --env OUTPUT_DIR=/srv/video/output \
           --env IMAGE_SIZE=$MY_IMAGE_SIZE --env WIDTH=$MY_WIDTH --env HEIGHT=$MY_HEIGHT \
           --privileged -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
           -v /home/jadebustos/working/demo-ai/:/srv/video/output:Z -d quay.io/rhte_2019/face-dataset:v1