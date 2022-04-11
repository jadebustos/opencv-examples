#!/usr/bin/python

# (c) 2022 José Ángel de Bustos Pérez <jadebustos@gmail.com>
# Distributed under GPLv3.0 https://www.gnu.org/licenses/gpl-3.0.txt

import argparse
import cv2

def face_detection(args):
    videoDev = int(args['device'])
    cascPath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)
    if args['size'] == None:
        image_size = 500
    else:
        image_size = int(args['size'])

    # gauss dev=1 (internal)
    # ramanujan dev=2 (logitech)
    # archimedes dev=5 (logitech)
    try:
        video_capture = cv2.VideoCapture(videoDev)
    except:
        print("Error opening video device")

    if video_capture.isOpened():
        while True:
            # capture frames from webcam
            ret, frame = video_capture.read()
        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    )

            # draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # if image is fewer than image_size x image_size discard image
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
                cv2.imwrite("frame.jpg", frame[y:y+h, x:x+w])
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
    parser.add_argument("-s", "--size", type=int, help="minimum image size")
    args = parser.parse_args()

    face_detection(vars(args))
