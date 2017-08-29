import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 15
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an

#GPIO.cleanup()