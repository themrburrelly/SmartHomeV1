import RPi.GPIO as GPIO
from time import sleep
from pymongo import MongoClient

# SETUP
# ---------------------------------
# Database setup
client = MongoClient()
db = client.db
outputs = db.family_outputs

# Raspberry Setup
GPIO.setmode(GPIO.BCM)
for pin in range(2, 10):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# LOOP
# ---------------------------------
while True:
    for output in outputs.find():
        if output['state'] == 0:
            GPIO.output(output['pin'], GPIO.LOW)
        else:
            GPIO.output(output['pin'], GPIO.HIGH)
    sleep(1)
