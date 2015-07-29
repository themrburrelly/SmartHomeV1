from django.shortcuts import render
# check if the code is running on the raspberry pi
try:
    import RPi.GPIO as GPIO
    plataform = "rbpi"
except:
    plataform = "mac"

    pin = 6

    def index(request, state=1):
        """Return the responce for the request."""
        if plataform == "rbpi":
            GPIO.setmode(GPIO.BCM), GPIO.setup(pin, GPIO.OUT)
        if int(state) == 0:
            if plataform == "rbpi":
                GPIO.output(pin, GPIO.LOW)
            context = {"msg": "La llum esta obert"}
        else:
            if plataform == "rbpi":
                GPIO.output(pin, GPIO.HIGH)
            context = {"msg": "La llum esta apagada"}
        return render(request, 'family/index.html', context)
