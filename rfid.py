import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import LED
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()

green_led = LED(16)
red_led = LED(21)

known_tag_id =   # Replace with your known tag ID
write_message = "Hello, RFID!"  # Message to write to the RFID tag

try:
    while True:
        print("Hold a tag near the reader")
        id, _ = reader.read()
        print("Tag ID:", id)
        
        if id == known_tag_id:
            print("Known tag detected, writing message to the tag...")
            green_led.on()
            reader.write(write_message)
            green_led.off()
            print("Message written to the tag")
            break
        else:
            print("Unknown tag detected, try again")
            red_led.on()
            sleep(1)
            red_led.off()

finally:
    GPIO.cleanup()
