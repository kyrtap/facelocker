import cv2
import time
import argparse
import ctypes
import platform


def lock_screen(platform_name):
    if platform_name == 'Darwin':
        login = ctypes.CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        login.SACLockScreenImmediate()
    elif platform_name == 'Windows':
        ctypes.windll.user32.LockWorkStation()


def face_recognized(cap, face_cascade, demo_mode) -> bool:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if demo_mode:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Facelocker', frame)
        cv2.waitKey(1)

    return len(faces) > 0


def main(time_interval=10, demo_mode=False):
    print('Starting Facelocker with interval of {} seconds...'.format(time_interval))

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    time_counter = 0
    platform_name = platform.system()

    print('Looking for faces...'.format(time_interval))

    while True:
        try:
            if face_recognized(cap, face_cascade, demo_mode):
                time_counter = 0
            else:
                time_counter += 1
        except cv2.error:
            print('Failed to access camera. Did you grant permissions?')
            break

        if time_counter == time_interval:
            lock_screen(platform_name)
        time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('interval', nargs='?', default=10, type=int, help='Time interval to lock after')
    parser.add_argument('-d', '--demo', action='store_true', default=False,
                        help='Run in demo mode (show camera frames)')
    args = parser.parse_args()

    main(args.interval, args.demo)
