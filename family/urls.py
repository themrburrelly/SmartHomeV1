from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_element', views.new_element, name='new_element'),
    url(r'^add_element', views.add_element, name='add_element'),
    url(r'^outputs', views.output, name='outputs'),
    url(r'^temperature', views.temperature, name='temperature'),
    url(r'^new_output', views.new_output, name='new_output'),
    url(r'^add_output', views.add_output, name='add_output'),
    url(r'^change_output/(?P<output_name>.*)', views.change_output, name='change_output'),
]
