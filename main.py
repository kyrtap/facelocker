from ctypes import CDLL


def lock_screen_macos():
    login = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
    login.SACLockScreenImmediate()


def main():
    lock_screen_macos()


if __name__ == '__main__':
    main()
