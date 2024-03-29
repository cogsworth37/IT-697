from grovepi import *
from grove_rgb_lcd import *
import time
import datetime
from temp_sensor.functions import *
from mqtt.mqtt_client import MqttClient
from generateUuid import generateUuid

dht_sensor_port = 7
potentiometer = 0
ultrasonic_ranger = 8

mqtt = MqttClient("test.mosquitto.org")
topic = "SNHU/IT697/sensor/data/" + generateUuid()
print(topic)
while True:
    try:
        # angle = analogRead(potentiometer)
        # print(angle)
        # distance = ultrasonicRead(ultrasonic_ranger)
        time.sleep(1)
        [temp, hum] = dht(
            dht_sensor_port, 0
        )  # Get the temperature and Humidity from the DHT sensor
        # print("temp =", temp, "C\thumidity =", hum,"%")
        tempF = cToF(temp)
        # output = "Temp:" + str(temp) + "F\nHumidity: " + str(hum) + "%"
        bgColors = setBackgroundColor(temp)
        setRGB(bgColors["red"], bgColors["green"], bgColors["blue"])
        setText_norefresh(setOutput(tempF, hum))
        mqtt.post(topic, setOutput(temp, hum))
        mqtt.post(
            topic + "json",
            setOutput(
                temp, hum, "json", str(time.time()), rotary_angle=angle, dist=distance
            ),
        )
    except KeyboardInterrupt:
        setRGB(100, 100, 100)
        setText("Goodbye!")
        time.sleep(5)
        setRGB(0, 0, 0)
        setText("")
        break
    except (IOError, TypeError) as e:
        print(e)

