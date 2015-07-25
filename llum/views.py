from django.shortcuts import render
import RPi.GPIO as GPIO


def index(request, state=1):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    if int(state) == 0:
        GPIO.output(2, GPIO.LOW)
        context = {"msg": "La llum esta oberta"}
    else:
        GPIO.output(2, GPIO.HIGH)
        context = {"msg": "La llum esta apagada"}
    return render(request, 'llum/index.html', context)
