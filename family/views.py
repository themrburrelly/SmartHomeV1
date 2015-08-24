from django.shortcuts import render
from pymongo import MongoClient
import datetime
from time import sleep

# Start conection with mongo db server
client = MongoClient()
db = client.db
# check if the code is running on the raspberry pi
try:
    import RPi.GPIO as GPIO
    plataform = "rbpi"
    relay_pin = 4
    sensor_pin = 10
    # set up raspberry pins
    GPIO.setmode(GPIO.BCM)
    for pin in range(2, 10):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
except:
    plataform = "mac"


def index(request, state=1):
    home_elements = db.home_elements
    context = home_elements.find()
    return render(request, 'family/index.html', context)
