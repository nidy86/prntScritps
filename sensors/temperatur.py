'''
Created on 29.08.2017 ... SENSOR DS18B20
@author: patrik
'''

import os                                                  # import os module
import glob                                                # import glob module
import time                                                # import time module

import sys, getopt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern

sys.path += ['../relays']
from switch import RelaySwitch

os.system('modprobe w1-gpio')                              # load one wire communication device kernel modules
os.system('modprobe w1-therm')                                                 
base_dir = '/sys/bus/w1/devices/'                          # point to the address
device_folder = glob.glob(base_dir + '28*')[0]             # find device with address starting from 28*
device_file = device_folder + '/w1_slave'                  # store the details
def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()                                   # read the device details
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':                   # ignore first line
      time.sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')                        # find temperature in the details
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0                 # convert to Celsius
      return temp_c

while True:
   relay = RelaySwitch(14)
   temp = read_temp()  
   print(temp)                                    # Print temperature  
   if temp<23 :
       relay.on()
   else:
       relay.off()  
   time.sleep(1)