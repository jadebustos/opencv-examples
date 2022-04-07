# Face Detection Video

**face-detection-video.py** is a python script that detects faces on a webcam. The **haarcascade_frontalface_default.xml** must be present in the same directory.

It has to parameters:

* **--device or -d** which is used to set the video device by its index. If the device for the webcam is **/dev/video0** then **--device 0** needs to be used. This parameter is mandatory.
* **--graphical** if this script is used in a workstation with X-window environment. A window will be opened to show webcam images with a square for faces when this parameter is used. As we are going to run this script inside a container we will not use this parameter. It is only includef for testing purposes. This parameter is optional.

To execute:

```console
$ python face-detection-video.py --device 0
```
At this point when a face is detected the face is stored in a file named **frame.jpg** in the same directory where the script is stored.

You can copy it from the running container using the podman **cp** command.
