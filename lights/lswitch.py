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

class LightSwitch():

    def __init__(self, color=(255,255,255)):
        # Configure the count of pixels:
        self.PIXEL_COUNT = 2*(32+9)
        
        # Alternatively specify a hardware SPI connection on /dev/spidev0.0:
        self.SPI_PORT   = 0
        self.SPI_DEVICE = 0
        self.pixels = Adafruit_WS2801.WS2801Pixels(self.PIXEL_COUNT, spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEVICE), gpio=GPIO)
        self.color = color
    
    def all(self):
        self.pixels.clear()
        for k in range(self.pixels.count()):
            self.pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( self.color[0], self.color[1], self.color[2] ))
        self.pixels.show()  # Make sure to call show() after changing any pixels!
    
    def lite(self):
        self.pixels.clear()
        half = self.pixels.count()/2
        third = half/3
        for k in range(third+1):
            self.pixels.set_pixel(k+third, Adafruit_WS2801.RGB_to_color( self.color[0], self.color[1], self.color[2] ))
            self.pixels.set_pixel(k+third+half, Adafruit_WS2801.RGB_to_color( self.color[0], self.color[1], self.color[2] ))
        self.pixels.show()  # Make sure to call show() after changing any pixels!
    
    def top(self):
        self.pixels.clear()
        half = self.pixels.count()/2
        for k in range(half):
            self.pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( self.color[0], self.color[1], self.color[2] ))
        self.pixels.show()  # Make sure to call show() after changing any pixels!
        
    def bottom(self):
        self.pixels.clear()
        half = self.pixels.count()/2
        for k in range(half):
            self.pixels.set_pixel(k+half, Adafruit_WS2801.RGB_to_color( self.color[0], self.color[1], self.color[2] ))
        self.pixels.show()  # Make sure to call show() after changing any pixels!
        
    def switch_off(self):
        self.pixels.clear()
        color = (0,0,0)
        for k in range(self.pixels.count()):
            self.pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( self.color[0], self.color[1], self.color[2] ))
        self.pixels.show()  # Make sure to call show() after changing any pixels!

def main(argv):
   color = (255,174,250)
   dir = ''
   try:
      opts, args = getopt.getopt(argv,"hc:d:x:",["color=","dir=","rgb="])
   except getopt.GetoptError:
      print 'lswitch.py -c <white/red/blue/yellow/green -d <ON/LITE/TOP/BOTTOM/OFF> --rgb=<R>,<B>,<G>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'lswitch.py -c <white/warm/red/blue/yellow/green/purple/cyan -d <ON/LITE/TOP/BOTTOM/OFF> --rgb=<R>,<B>,<G>'
         sys.exit()
      elif opt in ("-c", "--color"):
         if arg=="white":
             color=(255,255,255)
         elif arg=="warm":
             color=(255,174,250)
         elif arg=="red":
             color=(255,0,0)
         elif arg=="blue":
             color=(0,255,0)
         elif arg=="yellow":
             color=(255,0,255)
         elif arg=="green":
             color=(0,0,255)
         elif arg=="purple":
             color=(255,255,0)
         elif arg=="cyan":
             color=(0,255,255)
         else:
             color=(0,0,0)
      elif opt in ("-d", "--dir"):
         dir = arg
      elif opt in ("-x,","--rgb"):
          clr = arg.split(",")
          color=(int(clr[0]),int(clr[1]),int(clr[2]))
   
   lights = LightSwitch(color)
   
   if dir=="ON":
       lights.all()
   elif dir=="LITE":
       lights.lite()
   elif dir=="TOP":
       lights.top()
   elif dir=="BOTTOM":
       lights.bottom()
   else:
       lights.switch_off()

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("User stop")
        GPIO.cleanup()