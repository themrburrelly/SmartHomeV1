from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<state>.*?)/$', views.index, name='index'),
]
