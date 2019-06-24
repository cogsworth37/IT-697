from grovepi import *
from sensors.rotary_angle import *
from mqtt.mqtt_client import MqttClient

ra = RotaryAngleSensor(0)
led_port = 5

pinMode(led_port,"OUTPUT")

mqtt = MqttClient("localhost")
mqtt.sub("SNHU/IT697/leds")
mqtt.on_message()


# while True:
#     try:
#         print(ra.read())
#         analogWrite(led_port,ra.read()/4)
#     except (IOError, TypeError) as e:
#         print(e)

