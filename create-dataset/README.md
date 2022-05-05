# Dataset creation

To train the model to recognize faces a dataset will be needed.

For each subject we want to recognise we will need a banch of images.

To help to recollect images we can use a container which will use your webcan to record random images to be used to train the model.

## Create dataset images

Each person which want to be used for face recognition will need to follow:

* Identify the video device for your laptop. [Check this](../face-detection/face-detection-video.md).
* Identify the biggest resolution. Let's say 1920x1080.
* Run the container image:

   ```console
   $ podman run --rm --env VIDEO_INDEX=5 --env MODULUS=11 --env RANDOM_RANGE=101 \
            --env OUTPUT_DIR=/srv/video/output --env IMAGE_SIZE=300 --env WIDTH=1920 \
            --env HEIGHT=1080 --privileged -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
            -v /home/jadebustos/working/demo-ai/:/srv/video/output:Z -d quay.io/rhte_2019/face-dataset:v2
   ```

   where:

   * **VIDEO_INDEX=5** index for your video device. If your video device is **/dev/video5** then **5** should be configured.
   * **MODULUS=11** modulus. [Check this to understand this value](create-dataset.md).
   * **RANDOM_RANGE=101** random range. [Check this to understand this value](create-dataset.md).
   * **SIZE=300** minimum size image in pixels (300x300).
   * **WIDTH=1920** your webcam maximum resolution for width.
   * **HEIGH=1080** your webcam maximum resolution for height.
   * **OUTPUT_DIR=/srv/video/output** when running the container **DO NOT CHANGE** this value.
   * **-v /home/jadebustos/working/demo-ai/:/srv/video/output:Z** change **/home/jadebustos/working/demo-ai/** for the local directory where do you want the images to be stored. This directory will be mapped to **/srv/video/output** in the container.

> ![TIP](../imgs/tip-icon.png) The bigger resolution the bigger images. This will allow that the image for the detectec face will be the biggest possible.

> ![TIP](../imgs/important-icon.png) We would ideally like face images of 500x500 or bigger. The bigger the best. Try to get images of at least 300x300.

> ![TIP](../imgs/tip-icon.png) You can run this container when you are working to store the images. To have as much variability as possible in the dataset try to:
>
> * Use in different days, using a different T-shirt (a clean one, although it is not mandatory).
> * Try to modify your distance to the webcam.
> * Try to smile :-D, move you head, etc.

> ![TIP](../imgs/important-icon.png) You can use the script [start-recording.sh](start-recording.sh).

