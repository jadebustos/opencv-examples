# Face Recognition

This directory contains code to create a container to run an application to recognize people with the aim to authenticate users.

## Running the container image using Podman

To create the container:

```console
$ buildah bud --build-arg OPENCV_VERSION=4.5.5 -t opencv .
```

This will create the container image using a CentOS Stream 8 image and **OpenCV 4.5.5** will be used.

To run the container:

```console
$ podman run --rm --env VIDEO_INDEX=5 --privileged -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts -d localhost/opencv
```

* **VIDEO_INDEX** is the video index device for the webcam you want to use. In this case the **/dev/video5** was used.

To troubleshoot inside the container you can execute:

```console
# python3 -c "import cv2;print(cv2.VideoCapture(5).isOpened())"
True
```

Which will inform you if the webcan can be used.

