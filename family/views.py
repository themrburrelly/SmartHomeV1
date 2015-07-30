from django.shortcuts import render
# check if the code is running on the raspberry pi
try:
    import RPi.GPIO as GPIO
    plataform = "rbpi"
    relay_pin = 9
    sensor_pin = 10
except:
    plataform = "mac"


def index(request, state=1):
    """Return the responce for the request."""
    if plataform == "rbpi":
        # set up raspberry pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay_pin, GPIO.OUT)
        GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUT_DOWN)
    if int(state) == 0 or GPIO.input():
        if plataform == "rbpi":
            GPIO.output(relay_pin, GPIO.LOW)
        context = {"msg": "La llum esta obert"}
    else:
        if plataform == "rbpi":
            GPIO.output(relay_pin, GPIO.HIGH)
        context = {"msg": "La llum esta apagada"}
    return render(request, 'family/index.html', context)
