import cv2
import time
import sys

from ctypes import CDLL


def lock_screen_macos():
    login = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
    login.SACLockScreenImmediate()


def face_recognized(cap, face_cascade) -> bool:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    return len(faces) > 0


def main(time_interval):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    time_counter = 0

    print('Facelocker started with lock interval {}. Looking for faces...'.format(time_interval))

    while True:
        if face_recognized(cap, face_cascade):
            time_counter = 0
        else:
            time_counter += 1

        if time_counter == time_interval:
            lock_screen_macos()

        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        time_interval = sys.argv[1]
    else:
        time_interval = 10

    main(time_interval)
