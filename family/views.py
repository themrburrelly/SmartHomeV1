from django.shortcuts import render
from pymongo import MongoClient


# Start conection with mongo db server
client = MongoClient()
db = client.db


def index(request):
    home_elements = db.home_elements
    context = home_elements.find_one()
    client.close()
    return render(request, 'family/index.html', context)


