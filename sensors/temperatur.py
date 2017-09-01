'''
Created on 29.08.2017 ... SENSOR DS18B20
@author: patrik
'''

import os                                                  # import os module
import glob                                                # import glob module
import time                                                # import time module

import sys, getopt
sys.path += ['../relays']
from rswitch import RelaySwitch

class TempSensor():
    def __init__(self):
        os.system('modprobe w1-gpio')                              # load one wire communication device kernel modules
        os.system('modprobe w1-therm')                                                 
        base_dir = '/sys/bus/w1/devices/'                          # point to the address
        self.device_folder = glob.glob(base_dir + '28*')[0]             # find device with address starting from 28*
        self.device_file = self.device_folder + '/w1_slave'                  # store the details
        
    def read_temp_raw(self):
       f = open(self.device_file, 'r')
       lines = f.readlines()                                   # read the device details
       f.close()
       return lines

    def read_temp(self):
       lines = self.read_temp_raw()
       while lines[0].strip()[-3:] != 'YES':                   # ignore first line
          time.sleep(0.2)
          lines = self.read_temp_raw()
       equals_pos = lines[1].find('t=')                        # find temperature in the details
       if equals_pos != -1:
          temp_string = lines[1][equals_pos+2:]
          temp_c = float(temp_string) / 1000.0                 # convert to Celsius
          return temp_c
    
    def show(self):
        print(self.read_temp())
        
    def switchOnOver(self,relay,temp):
        if self.read_temp()<temp :
           relay.on()
        else:
           relay.off()
           
    def switchOnUnder(self,relay,temp):
        if self.read_temp()<temp :
           relay.on()
        else:
           relay.off()
   
   
def main(argv):
   
   port = '14'
   dir = 'OFF'
   temp = 0.0
   sleep = 1
   show = True
   try:
      opts, args = getopt.getopt(argv,"hp:d:t:s:x:",["port=","dir=","temp=","sleep=","x="])
   except getopt.GetoptError:
      print 'temperature.py -p <BMC-ID> -d <OVER/UNDER/OFF> -t <float(TEMP)> -s <sleep> -x <SHOW/HIDE>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'temperature.py -p <BMC-ID> -d <OVER/UNDER/OFF> -t <float(TEMP)> -s <sleep> -x <SHOW/HIDE>'
         sys.exit()
      elif opt in ("-p", "--port"):
         port = int(arg)
      elif opt in ("-d", "--dir"):
         dir = arg
      elif opt in ("-t", "--temp"):
         temp = float(arg)
      elif opt in ("-s", "--sleep"):
         sleep = float(arg)
      elif opt in ("-x", "--x"):
         if(arg=="SHOW"):
             show=True
         else:
             show=False
   
   sensor = TempSensor()
   try:
       if(dir!='OFF'):
           relay = RelaySwitch(port)
       while True:
           if(show==True):
               sensor.show()
           if(dir!='OFF'):
               if(dir=='OVER'):
                   sensor.switchOnOver(relay, temp)
               else:
                   sensor.switchOnUnder(relay, temp)
           time.sleep(sleep)
   except KeyboardInterrupt:
        print("User stop")
        GPIO.cleanup()
           
           

if __name__ == "__main__":
    main(sys.argv[1:])
    