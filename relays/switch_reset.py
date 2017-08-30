import sys, getopt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern

RELAY = [14,15,17,18]

def off(relID):
    RELAY_GPIO_ID = relID
    GPIO.setup(RELAY_GPIO_ID, GPIO.OUT) # GPIO Modus zuweisen
    GPIO.output(RELAY_GPIO_ID, GPIO.LOW) # an
    GPIO.output(RELAY_GPIO_ID, GPIO.HIGH) # aus
    return



if __name__ == "__main__":
    try:
        for i in range(len(RELAY)):
            off(RELAY[i])
        GPIO.cleanup()
    except KeyboardInterrupt:
        print("User stop")
        GPIO.cleanup()