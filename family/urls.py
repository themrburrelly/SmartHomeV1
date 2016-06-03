from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.v_index, name='index'),
    url(r'^switches', views.v_switches, name='switches'),
    url(r'^aj_toggle_switch', views.aj_toggle_switch, name='toggle_switch'),
    url(r'^sensors', views.v_sensors, name='sensors'),
    url(r'^settings', views.v_settings, name='settings'),
    url(r'^sports', views.v_sports, name='sports'),
    url(r'^bank', views.v_bank, name='bank'),
    url(r'^food', views.v_food, name='food'),
]
