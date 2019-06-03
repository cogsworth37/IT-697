from grovepi import *
from grove_rgb_lcd import *
import time
from functions import *

dht_sensor_port = 7

while True:
  try:
    time.sleep(1)
    [ temp,hum ] = dht(dht_sensor_port,0)		#Get the temperature and Humidity from the DHT sensor
    #print("temp =", temp, "C\thumidity =", hum,"%") 
    temp = cToF(temp)
    output = "Temp:" + str(temp) + "F\nHumidity: " + str(hum) + "%"
    bgColors = setBackgroundColor(temp) 
    setRGB(bgColors['red'], bgColors['green'], bgColors['blue'])
    setText_norefresh(output)
  except KeyboardInterrupt:
    setRGB(100,100,100)
    setText("Goodbye!")
    time.sleep(5)
    setRGB(0,0,0)
    setText("")
    break
  except (IOError, TypeError) as e:
    print e 

