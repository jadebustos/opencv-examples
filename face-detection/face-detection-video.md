# Face Detection Video

**face-detection-video.py** is a python script that detects faces on webcam. The **haarcascade_frontalface_default.xml** must be present in the same directory.

It has to parameters:

* **--device or -d** which is used to set the video device by its index. If the webcam is **/dev/video** **--device 0** needs to be used. This parameter is mandatory.
* **--graphical** if this script is used in a workstation with X-window environment. A window will be opened to show webcam images with a square for faces. As we are going to run this script inside a container we will not use this parameter. It is only include for testing purposes.

To execute:

```console
$ python face-detection-video.py --device 0
```

