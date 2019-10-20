import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 5
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

if len(sys.argv) != 2:
    print("Must supply argument 'on' or 'off")
    sys.exit(1)


if sys.argv[1] == 'off':
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
elif sys.argv[1] == 'on':
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
