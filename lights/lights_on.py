
'''
Created on 29.08.2017
@author: patrik
'''
# SRC from Source: https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/
# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


# Configure the count of pixels:
PIXEL_COUNT = 2*(32+9)

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

if __name__ == "__main__":
    try:
        # Clear all the pixels to turn them off.
        pixels.clear()
        color = (255,255,255)
        for k in range(pixels.count()):
            pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
        pixels.show()  # Make sure to call show() after changing any pixels!
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Licht vom User gestoppt")
        pixels.clear()
        color = (0,0,0)
        for k in range(pixels.count()):
            pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
        pixels.show()  # Make sure to call show() after changing any pixels!

