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

# setup temp and hum sensor
sensor = Adafruit_DHT.DHT22

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# GPIO config
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

humidity, temperature = Adafruit_DHT.read_retry(sensor, 4)
minute = 0
current_minute = 100

#Poll 40 readings
while minute < 40:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, 4)	

	# Read data every minute
	if (current_minute != dt.now().minute):
                current_time = time.asctime()
		print("Minute: " + str(minute))
		print("Time = " + current_time[11:19])
		print("Temp = " + str(int(temperature)))
		print("Hum = " + str(int(humidity)) + "%")
		print("Light = " + str(mcp.read_adc(2)))
		print("Gate = " + str(GPIO.input(21)))
		print("Envelope = " + str(mcp.read_adc(1)))
		print("Audio = " + str(mcp.read_adc(0))) 
		print("\n")
		current_minute = dt.now().minute
		minute += 1

'''
print("Time = " + current_time[11:19])
print("Temp = " + str(temperature)) #TODO: fix this
print("Hum = " + str(humidity) + "%") #TODO: fix this
print("Light = " + str(mcp.read_adc(2)))
print("Gate = " + str(GPIO.input(21)))
print("Envelope = " + str(mcp.read_adc(1)))
print("Audio = " + str(mcp.read_adc(0)))
print("\n")
'''
