import sys, getopt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern

def on(relID):
    RELAIS_1_GPIO = relID
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
    
    return
    
def off(relID):
    RELAIS_1_GPIO = relID
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus

    GPIO.cleanup()
    return

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
   
   if dir=="ON":
       on(port)
   else:
       off(port)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("User stop")
        GPIO.cleanup()