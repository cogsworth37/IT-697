from grovepi import *
from sensors.rotary_angle import *

ra = RotaryAngleSensor(0)
led_port = 5

pinMode(led_port,"OUTPUT")

while True:
    try:
        print(ra.read())
        analogWrite(led_port,ra.read()/4)
    except (IOError, TypeError) as e:
        print(e)

