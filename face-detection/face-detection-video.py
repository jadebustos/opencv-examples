#!/usr/bin/python

# https://realpython.com/face-detection-in-python-using-a-webcam/

# https://realpython.com/traditional-face-detection-python/
# https://realpython.com/face-recognition-with-python/
# https://github.com/shantnu/PyEng

import cv2
import sys

def face_detection(video):
    videoDev = int(video)
    cascPath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)

    # toshiba dev=1
    video_capture = cv2.VideoCapture(videoDev)

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
        cv2.imshow('Video', frame)
        cv2.imwrite("frame.jpg", frame[y:y+h, x:x+w])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detection(sys.argv[1])
