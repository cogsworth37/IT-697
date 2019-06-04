import json

def cToF(temp):
    """
    Convert from Celcius to Farenheit
    """
    return (temp * 1.8) + 32

def setBackgroundColor(temp):
    """
    Change the background color based on the temperature
    """
    if temp < 65:
        colors = { "red": 0, "green": 128, "blue": 64 }
    elif temp > 65 and temp < 85:
        colors = { "red": 0, "green": 255, "blue": 0 }
    elif temp > 85:
        colors = { "red": 255, "green": 0, "blue": 0 }
    else:
        colors = { "red": 255, "green": 255, "blue": 0}

    return colors

def setOutput(temp, hum):
    """
    Check to see if the Temp and Hum are valid and then return the text
    Else return Error
    """
    if temp and hum:
        return "Temp:" + str(temp) + "F\nHumidity: " + str(hum) + "%"
    else:
        return "ERROR"
