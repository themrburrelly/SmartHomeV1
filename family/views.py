from django.shortcuts import render
from family.models import home_elements, outputs, inputs, settings
from django.utils import timezone


def index(request):
    context = {"home_elements": home_elements.objects.all()}
    return render(request, 'family/index.html', context)


def new_element(request):
    context = {}
    return render(request, 'family/new_element.html', context)


def add_element(request):
    home_elements.objects.get_or_create(name=request.POST['name'],
                                        defaults={'date': timezone.now(),
                                                  'img': "/static/family/img/%s.png" % request.POST['name']}
                                        )
    return index(request)


def output(request):
    context = {"outputs": outputs.objects.all()}
    return render(request, 'family/outputs.html', context)


def new_output(request):
    context = {}
    return render(request, 'family/new_output.html', context)


def add_output(request):
    outputs.objects.get_or_create(name=request.POST['name'], pin=request.POST['pin'])
    return output(request)


def change_output(request):
    if request.POST['name'] == 'up' and outputs.objects.get(name='up').state == 0:
        outputs.objects.filter(name='down').update(state=0)
    if request.POST['name'] == 'down' and outputs.objects.get(name='down').state == 0:
        outputs.objects.filter(name='up').update(state=0)
    try:
        val = 1 - outputs.objects.get(name=request.POST['name']).state
    except:
        pass
    outputs.objects.filter(name=request.POST['name']).update(state=val)
    return output(request)


def temperature(request):
    context = {"inputs": inputs.objects.all()}
    return render(request, 'family/temperature.html', context)


def delete(request):
    home_elements.objects.filter(name=request.POST['name']).delete()
    inputs.objects.filter(name=request.POST['name']).delete()
    outputs.objects.filter(name=request.POST['name']).delete()
    settings.objects.filter(name=request.POST['name']).delete()
    return index(request)


def setting(request):
    context = {"settings": settings.objects.all()}
    return render(request, 'family/settings.html', context)


def add_settings(request):
    settings.objects.get_or_create(name=request.POST['name'], pin=request.POST['value'])
    return setting(request)
