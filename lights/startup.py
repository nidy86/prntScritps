
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


# Configure the count of pixels: 32=1m
# 82 LEDs
PIXEL_COUNT = 2*(32+9) 

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)

def rainbow_cycle_successive(pixels, wait=0.1):
    end = pixels.count()
    half = end/2
    for i in range(half):
        # tricky math! we use each pixel as a fraction of the full 96-color wheel
        # (thats the i / strip.numPixels() part)
        # Then add in j which makes the colors go around per pixel
        # the % 96 is to make the wheel cycle around
        pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
        pixels.set_pixel((end-1)-i, wheel(((i * 256 // pixels.count())) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)
            
def rainbow_colors(pixels, wait=0.05):
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

def switch_off(pixels):
    pixels.clear()
    color = (0,0,0)
    for k in range(pixels.count()):
        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    pixels.show()  # Make sure to call show() after changing any pixels!

if __name__ == "__main__":
    try:
        # Clear all the pixels to turn them off.
        pixels.clear()
        pixels.show()
        
        #rainbow_colors(pixels, 0.05)
        rainbow_cycle_successive(pixels, 0.1)
        time.sleep(1)
        switch_off(pixels)
    except KeyboardInterrupt:
        print("Licht vom User ausgeschaltet")
        switch_off(pixels)

