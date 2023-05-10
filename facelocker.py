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


def face_recognized(cap, face_cascade) -> bool:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    return len(faces) > 0


def main(time_interval):
    print('Starting Facelocker with interval of {} seconds...'.format(time_interval))

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    time_counter = 0
    platform_name = platform.system()

    print('Looking for faces...'.format(time_interval))

    while True:
        try:
            if face_recognized(cap, face_cascade):
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
    args = parser.parse_args()

    main(args.interval)
