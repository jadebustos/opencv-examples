# Dataset creation

To train the model to recognize faces a dataset will be needed.

For each subject we want to recognise we will need a banch of images.

To help to recollect images we can use a container which will use your webcan to record random images to be used to train the model.

## Create dataset images

Each person which want to be used for face recognition will need to follow:

* Identify the video device for your laptop. [Check this](../face-detection/face-detection-video.md).
* Run the container image:

   ```console
   $ podman run --env VIDEO_INDEX=5 --env MODULUS=7 --env --RANDOM_RANGE=101 --env OUTPUT_DIR=/srv/video/output --privileged -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts -v /home/jadebustos/working/demo-ai/:/srv/video/output:Z -d localhost/face-dataset
   ```

   where:

   * **VIDEO_INDEX** index for your video device. If your video device is **/dev/video5** then **5** should be configured.
   * **MODULUS** modulus. [Check this to understand this value](create-dataset.md).
   * **RANDOM_RANGE** random range. [Check this to understand this value](create-dataset.md).
   * **OUTPUT_DIR** when running the container DO NOT CHANGE this value.
   * **-v /home/jadebustos/working/demo-ai/:/srv/video/output:Z** change **/home/jadebustos/working/demo-ai/** for a local directory where the images will be stored. This directory will be mapped to **/srv/video/output** in the container.