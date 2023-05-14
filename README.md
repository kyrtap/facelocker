# Facelocker
Automatically locks your screen when you move away from your machine.

## Setup
Facelocker works on macOS and Windows. The face recognition algorithm relies on the opencv module. 

To install all necessary dependencies, simply use the provided requirements file: 

`pip install -r requirements.txt`


## Usage

```
facelocker.py [-h] [-r RATE] [-d] [interval]

positional arguments:
  interval              Time interval to lock after (Default: 10s)

options:
  -h, --help            show this help message and exit
  -r RATE, --refresh RATE
                        Camera refresh rate in seconds (Default: 1s)
  -d, --demo            Run in demo mode (show camera frames)
```
To set up the time after which the screen is locked, use the positional argument `interval` in seconds. The default value is set to 10 seconds.

Additionally, there are two optional arguments:
- Using `-r`, you can set the camera refresh rate in seconds, i.e. the rate at which a camera capture is made. The default value is set to 1 second.
- To view the current camera image together with the recognized faces, you can run Facelocker in demo mode using the `-d` argument.