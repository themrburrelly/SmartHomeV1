from django.shortcuts import render
from family.models import home_elements, outputs, inputs, settings
from django.utils import timezone
from django.http import HttpResponse


def v_index(request):
    context = {}
    return render(request, 'family/template_home.html', context)


def v_switches(request):
    context = {}
    return render(request, 'family/template_switches.html', context)


def aj_toggle_switch(request):
    if request.POST['switch_id'] == 'Pujar':
        outputs.objects.filter(name='Baixar').update(state=0)
    if request.POST['switch_id'] == 'Baixar':
        outputs.objects.filter(name='Pujar').update(state=0)
    try:
        val = 1 - outputs.objects.get(name=request.POST['switch_id']).state
    except:
        pass
    outputs.objects.filter(name=request.POST['switch_id']).update(state=val)
    return HttpResponse()


def v_sensors(request):
    context = {"temperature": inputs.objects.get(name='temperature').metadata, "humidity": inputs.objects.get(name='humidity').metadata}
    return render(request, 'family/template_sensors.html', context)


def v_settings(request):
    context = {}
    return render(request, 'family/template_settings.html', context)


def v_sports(request):
    context = {}
    return render(request, 'family/template_sports.html', context)


def v_bank(request):
    context = {}
    return render(request, 'family/template_bank.html', context)


def v_food(request):
    context = {}
    return render(request, 'family/template_food.html', context)


# def new_element(request):
#     context = {}
#     return render(request, 'family/new_element.html', context)


# def add_element(request):
#     home_elements.objects.get_or_create(name=request.POST['name'],
#                                         defaults={'date': timezone.now(),
#                                                   'img': "/static/family/img/%s.png" % request.POST['name']}
#                                         )
#     return index(request)


# def output(request):
#     context = {"outputs": outputs.objects.all()}
#     return render(request, 'family/outputs.html', context)


# def new_output(request):
#     context = {}
#     return render(request, 'family/new_output.html', context)


# def add_output(request):
#     outputs.objects.get_or_create(name=request.POST['name'], pin=request.POST['pin'])
#     return output(request)


# def change_output(request):
#     if request.POST['name'] == 'up' and outputs.objects.get(name='up').state == 0:
#         outputs.objects.filter(name='down').update(state=0)
#     if request.POST['name'] == 'down' and outputs.objects.get(name='down').state == 0:
#         outputs.objects.filter(name='up').update(state=0)
#     try:
#         val = 1 - outputs.objects.get(name=request.POST['name']).state
#     except:
#         pass
#     outputs.objects.filter(name=request.POST['name']).update(state=val)
#     return output(request)


# def temperature(request):
#     context = {"inputs": inputs.objects.all()}
#     return render(request, 'family/temperature.html', context)


# def delete(request):
#     home_elements.objects.filter(name=request.POST['name']).delete()
#     inputs.objects.filter(name=request.POST['name']).delete()
#     outputs.objects.filter(name=request.POST['name']).delete()
#     settings.objects.filter(name=request.POST['name']).delete()
#     return index(request)



# def add_settings(request):
#     settings.objects.get_or_create(name=request.POST['name'], value=request.POST['value'])
#     return setting(request)
