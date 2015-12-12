import RPi.GPIO as GPIO
from time
from pymongo import MongoClient
import Adafruit_DHT as dht
import datetime

# SETUP
# ---------------------------------
# Database setup
client = MongoClient()
db = client.db
outputs = db.family_outputs
inputs = db.family_inputs
settings = db.family_settings

# Raspberry Setup
GPIO.setmode(GPIO.BCM)
for pin in range(2, 10):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Initialize Variables
motion_sensor_timer = settings.find_one({"name": "motion_sensor_timer"})['value']
motion_sensor_pin = settings.find_one({"name": "motion_sensor_pin"})['value']
GPIO.setup(motion_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
refresh_time = 0.1
morning = datetime.time(8, 30)
dark = datetime.time(18, 00)
night = datetime.time(23, 30)
sleep = datetime.time(00, 00)

# FUNCTIONS
# Update de la variable desitjada (outputs.update) amb registre de temps.
# Activar o desectivar pin (GPIO.output).

# LOOP
# ---------------------------------
count = 0
while True:
    # Motion Sensor
    try:
        if settings.find_one({"name": "motion_sensor_toggle"})['value']:
            if GPIO.input(motion_sensor_pin):
                # Fer que el temps d'apagat de la llum incrementi en funcio de la cantitat de cops que passes per dabant
                count = 0
                if datetime.time(23, 30) < timestamp < datetime.time(23, 31):
                    outputs.update({'name': 'Left Light'}, {"$set": {'state': 1}}, upsert=False)
                else:
                    outputs.update({'name': 'Right Light'}, {"$set": {'state': 1}}, upsert=False)
            if count == motion_sensor_timer:
                outputs.update({'name': 'Right Light'}, {"$set": {'state': 0}}, upsert=False)
                outputs.update({'name': 'Left Light'}, {"$set": {'state': 0}}, upsert=False)
            if count < motion_sensor_timer:
                count += 1
    except:
        pass

    # Time Trigger
    timestamp = datetime.datetime.now().time()
    if datetime.time(8, 30) < timestamp < datetime.time(8, 31):
        settings.update({'name': 'motion_sensor_toggle'}, {"$set": {'value': 1}}, upsert=False)
        outputs.update({'name': 'Endolls'}, {"$set": {'state': 0}}, upsert=False)
        outputs.update({'name': 'Baixar'}, {"$set": {'state': 0}}, upsert=False)
        outputs.update({'name': 'Pujar'}, {"$set": {'state': 1}}, upsert=False)
    if datetime.time(18, 00) < timestamp < datetime.time(18, 01):
        outputs.update({'name': 'Pujar'}, {"$set": {'state': 0}}, upsert=False)
        outputs.update({'name': 'Baixar'}, {"$set": {'state': 1}}, upsert=False)
    if datetime.time(00, 00) < timestamp < datetime.time(00, 01):
        settings.update({'name': 'motion_sensor_toggle'}, {"$set": {'value': 0}}, upsert=False)
        outputs.update({'name': 'Endolls'}, {"$set": {'state': 1}}, upsert=False)
        time.sleep(30)
        outputs.update({'name': 'Right Light'}, {"$set": {'state': 0}}, upsert=False)
        outputs.update({'name': 'Left Light'}, {"$set": {'state': 0}}, upsert=False)

    # Working
    if outputs.find_one({"name": "Endolls"})['state']:
        settings.update({'name': 'motion_sensor_toggle'}, {"$set": {'value': 0}}, upsert=False)
    else:
        settings.update({'name': 'motion_sensor_toggle'}, {"$set": {'value': 1}}, upsert=False)

    # Update Pin Stauts
    for output in outputs.find():
        if output['state'] == 0:
            GPIO.output(output['pin'], GPIO.HIGH)
        else:
            GPIO.output(output['pin'], GPIO.LOW)
    # Update Sensor Values
    h, t = dht.read_retry(dht.DHT22, inputs.find_one({'name': 'temperature'})['pin'])
    inputs.update({'name': 'temperature'}, {"$set": {'metadata': t}}, upsert=False)
    inputs.update({'name': 'humidity'}, {"$set": {'metadata': h}}, upsert=False)
    time.sleep(refresh_time)
