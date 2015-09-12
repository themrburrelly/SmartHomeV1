from django.shortcuts import render
from family.models import home_elements
from django.utils import timezone


def index(request):
    context = {"home_elements": home_elements.objects.all()}
    return render(request, 'family/index.html', context)


def new_element(request):
    context = {}
    return render(request, 'family/new_element.html', context)


def add_element(request):
    home_elements.objects.update_or_create(name=request.POST['name'],
                                           defaults={'date': timezone.now(),
                                                     'img': "/static/family/img/"+request.POST['name']+".png"}
                                           )
    return index(request)
