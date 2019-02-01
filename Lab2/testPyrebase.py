#!/usr/bin/python2
import time
from datetime import datetime as dt

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#import gpio libraries
import RPi.GPIO as GPIO

#import temp and humidity libraries
import Adafruit_DHT

from pyrebase import pyrebase

# setup temp and hum sensor
sensor = Adafruit_DHT.DHT22

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# GPIO config
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

config = {
        "apiKey": "AIzaSyA_CDg3tcREhVOj9XIJicQd457X5q4Raq4",
        "authDomain": "ece140a-lab2-aa5e8.firebaseapp.com",
        "databaseURL": "https://ece140a-lab2-aa5e8.firebaseio.com",
        "storageBucket": "ece140a-lab2-aa5e8.appspot.com",
        }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def write_to_pyrebase(temperature, humidity, light, gate, envelope, audio):
    data = {"temperature": temperature, "humidity": humidity, "light": light, \
            "gate": gate, "envelope": envelope, "audio": audio}
    db.push(data)


humidity, temperature = Adafruit_DHT.read_retry(sensor, 4)

write_to_pyrebase(str(int(temperature)),str(int(humidity)),str(mcp.read_adc(2)),\
        str(GPIO.input(21)),str(mcp.read_adc(1)),str(mcp.read_adc(0)))
