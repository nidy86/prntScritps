'''
Created on 29.08.2017
@author: patrik
'''
# SRC from Source: https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/
# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import sys, getopt
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

def all(pixels, color=(255,255,255)):
    pixels.clear()
    for k in range(pixels.count()):
        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    pixels.show()  # Make sure to call show() after changing any pixels!

def lite(pixels, color=(255,255,255)):
    pixels.clear()
    half = pixels.count()/2
    third = half/3
    for k in range(third+1):
        pixels.set_pixel(k+third, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
        pixels.set_pixel(k+third+half, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    pixels.show()  # Make sure to call show() after changing any pixels!

def top(pixels, color=(255,255,255)):
    pixels.clear()
    half = pixels.count()/2
    for k in range(half):
        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    pixels.show()  # Make sure to call show() after changing any pixels!
    
def bottom(pixels, color=(255,255,255)):
    pixels.clear()
    half = pixels.count()/2
    for k in range(half):
        pixels.set_pixel(k+half, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    pixels.show()  # Make sure to call show() after changing any pixels!
    
def switch_off(pixels):
    pixels.clear()
    color = (0,0,0)
    for k in range(pixels.count()):
        pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    pixels.show()  # Make sure to call show() after changing any pixels!

def main(pixels,argv):
   color = (255,255,255)
   dir = ''
   try:
      opts, args = getopt.getopt(argv,"hc:d:",["color=","dir="])
   except getopt.GetoptError:
      print 'switch.py -c <white/red/blue/yellow/green -d <ON/LITE/TOP/BOTTOM/OFF>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'switch.py -c <white/red/blue/yellow/green -d <ON/LITE/TOP/BOTTOM/OFF>'
         sys.exit()
      elif opt in ("-c", "--color"):
         if arg=="white":
             color=(255,255,255)
         elif arg=="red":
             color=(255,0,0)
         elif arg=="blue":
             color=(0,0,255)
         elif arg=="yellow":
             color=(0,255,0)
         elif arg=="green":
             color=(0,255,0)
         else:
             color=(0,0,0)
      elif opt in ("-d", "--dir"):
         dir = arg
   
   if dir=="ON":
       all(pixels, color)
   elif dir=="LITE":
       lite(pixels, color)
   elif dir=="TOP":
       top(pixels, color)
   elif dir=="BOTTOM":
       bottom(pixels, color)
   else:
       switch_off(pixels)

if __name__ == "__main__":
    try:
        main(pixels,sys.argv[1:])
    except KeyboardInterrupt:
        print("User stop")
        GPIO.cleanup()