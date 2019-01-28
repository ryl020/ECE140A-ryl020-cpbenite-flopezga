import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI

import Adafruit_MCP3008
from gpiozero import LED
from gpiozero import DigitalInputDevice


GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN);
i = 0
led = LED(26)
led.off()
isOn = 0

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
while i == 0:
    audio = mcp.read_adc(0)
    envelope = mcp.read_adc(1)
    if (audio > 620):
	print("Audio is: +" + str(audio) + " Envelope is: " + str(envelope))
    	if(isOn == 0):
            led.on()
            isOn = 1
        else:
            led.off()
            isOn = 0
