#!/bin/bash

python3 create-dataset.py --device $VIDEO_INDEX --modulus $MODULUS --range $RANDOM_RANGE \
                          --width $WIDTH --height $HEIGHT \ 
                          --size $IMAGE_SIZE --output_dir $OUTPUT_DIR
