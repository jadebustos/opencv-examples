# Face Recognition

This directory contains code to create a container to run an application to recognize people with the aim to authenticate users.

## Creating and running the container image using Podman

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


> ![TIP](../imgs/tip-icon.png) To troubleshoot inside the container and see if the camera can be opened:
>   ```console
>   # python3 -c "import cv2;print(cv2.VideoCapture(5).isOpened())"
>   True
>   #
>   ```
> Where 5 indicates that the camera device is **/dev/video5**. 

## Running the container in kubernetes

Before deploying the container you will need to configure the video device configuration in the YAML file. For the **/dev/video0**:

```yaml
    spec:
      containers:
      - name: face-recognition
        image: quay.io/rhte_2019/face-recognition:v1
        env:
        - name: VIDEO_INDEX
          value: '0' # /dev/video0
        volumeMounts:
        - name: dev-video0
          mountPath: /dev/video0
        securityContext:
          privileged: true
      volumes:
      - name: dev-video0
        hostPath:
          path: /dev/video0  
```

To deploy it:

```console
$ kubectl apply -f face-recognition.x86_64.k8s.yaml
```

> ![INFORMATION](../imgs/information-icon.png) This has been tested on Centos8 Stream, kubernetes 1.23.3 and CRI-0 1.23.1.