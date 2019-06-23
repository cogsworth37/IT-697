from grovepi import *
from sensors.rotary_angle import *

ra = RotaryAngleSensor(0)

while True:
    try:
        print(ra.read())
    except (IOError, TypeError) as e:
        print(e)

