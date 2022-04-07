# Face Recognition

This directory contains code to create a container to run an application to recognize people with the aim to authenticate users.

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

## Looking for information about your camera(s)

```console
[jadebustos@archimedes face-detection]$ v4l2-ctl --list-devices
OBS Virtual Camera (platform:v4l2loopback-000):
	/dev/video0

HD Pro Webcam C920 (usb-0000:00:14.0-2.1.3):
	/dev/video5
	/dev/video6
	/dev/media2

Integrated Camera: Integrated C (usb-0000:00:14.0-8):
	/dev/video1
	/dev/video2
	/dev/video3
	/dev/video4
	/dev/media0
	/dev/media1

[jadebustos@archimedes face-detection]$
```

You can get information about the webcam:

```console
[jadebustos@archimedes face-detection]$ v4l2-ctl -d /dev/video5 --list-formats
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'YUYV' (YUYV 4:2:2)
	[1]: 'MJPG' (Motion-JPEG, compressed)
[jadebustos@archimedes face-detection]$
```

Or the extended one:

```console
[jadebustos@archimedes face-detection]$ v4l2-ctl -d /dev/video5 --list-formats-ext
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'YUYV' (YUYV 4:2:2)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.042s (24.000 fps)
			Interval: Discrete 0.050s (20.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
			Interval: Discrete 0.100s (10.000 fps)
			Interval: Discrete 0.133s (7.500 fps)
			Interval: Discrete 0.200s (5.000 fps)
...
[jadebustos@archimedes face-detection]$
```
