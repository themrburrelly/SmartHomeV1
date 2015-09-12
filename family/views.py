from django.shortcuts import render
from family.models import home_elements


def index(request):
    context = {"home_elements": home_elements.objects.all()}
    return render(request, 'family/index.html', context)
