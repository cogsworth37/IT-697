import paho.mqtt.client as mqtt
from grovepi import *
import json

class MqttClient:
    def __init__(self, host):
        print("Initializing Client")
        self.host = host
        self.local_client = mqtt.Client()
        self.__connect()

    def __connect(self):
        self.local_client.connect(self.host)
        self.local_client.loop_start()
        print("Connected to MQTT Server")
    
    def getClient(self):
        return self.local_client

    def post(self, queue, message):
        self.local_client.publish(queue, message)
        print("Message has been posted")

    def onMessage(self, userdata, msg):
        print(msg.topic, msg.payload)
        payload = json.loads(msg.payload)
        # the legal values for analogWrite are 0-255
        return payload['brightness']

    def sub(self, topic):
        self.local_client.subscribe(topic)