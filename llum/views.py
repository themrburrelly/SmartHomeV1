from django.shortcuts import render
import RPi.GPIO as GPIO

pin = 6


def index(request, state=1):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    if int(state) == 0:
        GPIO.output(pin, GPIO.LOW)
        context = {"msg": "La llum esta obert"}
    else:
        GPIO.output(pin, GPIO.HIGH)
        context = {"msg": "La llum esta apagada"}
    return render(request, 'llum/index.html', context)
