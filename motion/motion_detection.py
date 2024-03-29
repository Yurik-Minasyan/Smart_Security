import smtplib
from email.message import EmailMessage
from gpiozero import MotionSensor, LED
from time import sleep

# Email configuration
from_email_addr = "kaliraspberrypi00@gmail.com"
from_email_password = "atstyvitohlesxyj"
to_email_addr = "edmondseropyan6@gmail.com"
email_subject = "[WARNING] Motion Detected!"
email_body = "Motion was detected by the PIR sensor."

# Initialize the motion sensor on GPIO pin 4 and the LED on GPIO pin 20
pir = MotionSensor(4)
led = LED(20)

# Function to send email
def send_email():
    msg = EmailMessage()
    msg.set_content(email_body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = email_subject

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email_addr, from_email_password)
        server.send_message(msg)
        print('Email sent')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

# Main loop
while True:
    if pir.motion_detected:
        print("Motion detected!")
        led.on()  # Turn on the LED
        send_email()
        sleep(10)  # Avoid multiple emails in a short period
        led.off()  # Turn off the LED
    sleep(0.1)  # Check for motion every 0.1 seconds
