from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_element', views.new_element, name='new_element'),
    url(r'^add_element', views.add_element, name='add_element')
]
