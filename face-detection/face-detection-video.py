#!/usr/bin/python

# https://realpython.com/face-detection-in-python-using-a-webcam/

# https://realpython.com/traditional-face-detection-python/
# https://realpython.com/face-recognition-with-python/
# https://github.com/shantnu/PyEng

import argparse
import cv2
import sys

def face_detection(args):
    videoDev = int(args['device'])
    cascPath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)

    # toshiba dev=1
    try:
        video_capture = cv2.VideoCapture(videoDev)
    except:
        print("Error opening video device")

    if video_capture.isOpened():
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            if args['graphical'] == True:
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # in case some variable is not defined, no face detected
            try:
                cv2.imwrite("frame.jpg", frame[y:y+h, x:x+w])
            except:
                pass

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("Error opening video device")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--device", type=int, required=True, help="video device index")
    parser.add_argument("-g", "--graphical", action="store_true", help="graphical")
    args = parser.parse_args()

    face_detection(vars(args))
