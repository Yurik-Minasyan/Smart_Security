import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()

try:
    print("Hold a tag near the reader")
    id, text = reader.read()
    print("Tag ID: ", id)
    print("Tag Text: ", text)
finally:
    GPIO.cleanup()

