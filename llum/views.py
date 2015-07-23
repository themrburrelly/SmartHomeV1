from django.shortcuts import render


def index(request, state):
    if int(state) == 0:
        context = {"msg": "La llum esta oberta"}
    else:
        context = {"msg": "La llum esta apagada"}
    return render(request, 'llum/index.html', context)
