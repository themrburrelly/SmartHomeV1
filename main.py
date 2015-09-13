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
    GPIO.output(pin, GPIO.HIGH)

# LOOP
# ---------------------------------
count = 0
motion_sensor_pin = 10
while True:
    if GPIO.input(motion_sensor_pin):
        count = 0
        outputs.update({'name': 'right_light'}, {"$set": {'state': 1}}, upsert=False)
    if count == 600:
        outputs.update({'name': 'right_light'}, {"$set": {'state': 0}}, upsert=False)
    for output in outputs.find():
        if output['state'] == 0:
            GPIO.output(output['pin'], GPIO.HIGH)
        else:
            GPIO.output(output['pin'], GPIO.LOW)
    if count < 650:
        count += 1
    sleep(1)
