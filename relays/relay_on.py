import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 14
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an

GPIO.cleanup()