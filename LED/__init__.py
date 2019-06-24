from grovepi import *

class LED:
    def __init__(self, port):
        self.port = port
        pinMode(port,"OUTPUT")
    
    def adjust(self, brightness):
        analogWrite(self.port,brightness)
