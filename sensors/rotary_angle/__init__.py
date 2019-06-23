from grovepi import *

class RotaryAngleSensor:
    def __init__(self, port):
        self.digital_port = port

    def read(self):
        return analogRead(self.digital_port)

    
