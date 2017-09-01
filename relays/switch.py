import sys, getopt
import RPi.GPIO as GPIO

class RelaySwitch():
 
    def __init__(self,bcmPort):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
        self.RELAY_ID_GPIO = bcmPort

    def on(self):
        GPIO.setup(self.RELAY_ID_GPIO, GPIO.OUT) # GPIO Modus zuweisen
        GPIO.output(self.RELAY_ID_GPIO, GPIO.LOW) # an
    
    def off(self,relID):
        GPIO.setup(self.RELAY_ID_GPIO, GPIO.OUT) # GPIO Modus zuweisen
        GPIO.output(self.RELAY_ID_GPIO, GPIO.LOW) # an
        GPIO.output(self.RELAY_ID_GPIO, GPIO.HIGH) # aus

        GPIO.cleanup()
        
    def close(self):
        GPIO.cleanup()

def main(argv):
   
   port = ''
   dir = ''
   try:
      opts, args = getopt.getopt(argv,"hp:d:",["port=","dir="])
   except getopt.GetoptError:
      print 'switch.py -p <BMC-ID> -d <ON/OFF>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'switch.py -p <BMC-ID> -d <ON/OFF>'
         sys.exit()
      elif opt in ("-p", "--port"):
         port = int(arg)
      elif opt in ("-d", "--dir"):
         dir = arg
   
   relay = RelaySwitch(port)
   
   if dir=="ON":
       relay.on()
   else:
       relay.off()

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("User stop")
        GPIO.cleanup()