# create-dataset.py

This script will use a webcam to create a dataset of your face.

To use in standalone mode you will need to have installed OpenCV in your laptop. [README.md](A container is provider to use it).

To execute it:

```console
$ python create-dataset.py --device 5 --modulus 7 --range 101 --output_dir /home/jadebustos/working/demo-ai/
```

where there are two mandatory arguments:

* **--device 5** indicates de video device to be used. In this case **/dev/video5**. [Check this](../face-detection/face-detection-video.md) for more information.
* **--output_dir /home/jadebustos/working/demo-ai/** the local directory where to store the images from the webcam.

and there are two optional arguments. These arguments are used to randomly record images:

* **--range 101** a random number in the range 1 to this vale is choosen.
* **--modulus 7** when a random number modulus this value is zero a image is recordered.

## Understanding how often images are recordered (trying to)

To avoid to have images too similar in the dataset random images will be collected.

To collect them a random number will be generated from 1 to **--range** (by default 1 to 101), then if this number is 0 modulus **--modulus** (by default 7) then the image is recordered and stored in **--output_dir** using a random name.

You are allowed to modify and play with **--range** and **--modulus**.