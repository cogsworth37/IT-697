import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, host):
        print("Initializing Client")
        self.host = host
        self.__connect()

    def __connect(self):
        self.local_client = mqtt.Client()
        self.local_client.connect(self.host)
        self.local_client.loop_start()
        print("Connected to MQTT Server")

    def post(self, queue, message):
        self.local_client.publish(queue, message)
        print("Message has been posted")