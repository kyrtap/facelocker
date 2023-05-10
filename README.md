# facelocker
Automatically locks your screen when you move away from your machine.

## Setup
Facelocker works on macOS and Windows. The face recognition algorithm relies on the opencv module. 

To install all necessary dependencies, simply use the provided requirements file: 

`pip install -r requirements.txt`


## Usage
The script takes one positional argument `interval`, which describes the time in seconds after which your machine is supposed to lock when no face is recognized. The default value is set to 10.

`python3 facelocker.py [interval]`
