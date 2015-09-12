from django.db import models
from djangotoolbox.fields import ListField


class home_elements(models.Model):
    date = models.DateTimeField()
    name = models.TextField()
    metadata = models.IntegerField(blank=True, null=True, default=None)
    img = models.TextField()
    size = models.TextField(default='col-sm-2 col-xs-4')


class outputs(models.Model):
    name = models.TextField()
    pin = models.IntegerField()
    state = models.IntegerField(blank=True, null=True, default=0)
    time_log = ListField(blank=True, null=True, default=[])
