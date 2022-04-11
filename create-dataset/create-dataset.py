#!/usr/bin/python

# (c) 2022 José Ángel de Bustos Pérez <jadebustos@gmail.com>
# Distributed under GPLv3.0 https://www.gnu.org/licenses/gpl-3.0.txt

import argparse
import random
import string
import cv2
import os

def face_detection(args):
    videoDev = int(args['device'])
    cascPath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)
    output_dir = args['output_dir']
    modulus = int(args['modulus'])
    random_range = int(args['range'])
    image_size = int(args['size'])
    width = int(args['width'])
    height = int(args['height'])

    # print args
    print(args)

    # gauss dev=1 (internal)
    # ramanujan dev=2 (logitech)
    # archimedes dev=5 (logitech)
    try:
        #video_capture = cv2.VideoCapture(videoDev, cv2.CAP_ANY)
        video_capture = cv2.VideoCapture(videoDev, cv2.CAP_V4L)
    except:
        print("Error opening video device")

    # setting camera resolution
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width);
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height);
    if video_capture.isOpened():
        cam_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        cam_height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Camera resolution: %d x %d" % (cam_width, cam_height))

        while True:
            # capture frames from webcam
            ret, frame = video_capture.read()
        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(image_size, image_size),
                    )

            # draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # if image is smaller than image_size x image_size discard image
            if w < image_size or h < image_size:
                print("Image too small (%d x %d)." % (w,h))
                continue

            # display the resulting frame when X11 is used
            if args['graphical'] == True:
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # when no face detected the following crashes
            try:
                # to avoid creating images which are too similar only
                # some random frames will be stored
                # (maquiavelo seal of approval)
                random_int = random.randint(1, random_range)
                if random_int % modulus == 0:
                    # create random name
                    filename = "frame-"+ ''.join(random.choice(string.ascii_lowercase) for i in range(15))+ ".jpg"
                    filepath = os.path.join(output_dir, filename)
                    print("%s -> Camera resolution: %d x %d. Image resolution: %d x %d." % (filename, cam_width, cam_height, w, h))
                    cv2.imwrite(filepath, frame[y:y+h, x:x+w])
            except Exception as e:
                print(e)

        # when everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("Error opening video device")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--device", type=int, required=True, help="video device index")
    parser.add_argument("-g", "--graphical", action="store_true", help="graphical")
    parser.add_argument("-m", "--modulus", type=int, default=23, help="modulus (default 23)")
    parser.add_argument("-o", "--output_dir", required=True, help="output dir where store images")
    parser.add_argument("-r", "--range", type=int, default=101, help="random range (default 101)")
    parser.add_argument("-s", "--size", type=int, default=200, help="minimum image size (default 200)")
    parser.add_argument("-t", "--height", type=int, default=720, help="height resolution for camera (default 720)")
    parser.add_argument("-w", "--width", type=int, default=1280, help="width resolution for camera (default 1280)")
    args = parser.parse_args()

    face_detection(vars(args))
