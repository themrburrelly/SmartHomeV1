from django.shortcuts import render
from time import sleep
# check if the code is running on the raspberry pi
try:
    import RPi.GPIO as GPIO
    plataform = "rbpi"
    relay_pin = 3
    sensor_pin = 10
    # set up raspberry pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
except:
    plataform = "mac"

while True:
    sleep(1)
    if GPIO.input(sensor_pin):
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        GPIO.output(relay_pin, GPIO.HIGH)


def index(request, state=1):
    """Return the responce for the request."""
    if int(state) == 0 or GPIO.input(sensor_pin):
        if plataform == "rbpi":
            GPIO.output(relay_pin, GPIO.LOW)
        context = {"msg": "La llum esta oberta"}
    else:
        if plataform == "rbpi":
            GPIO.output(relay_pin, GPIO.HIGH)
        context = {"msg": "La llum esta apagada"}
    return render(request, 'family/index.html', context)
