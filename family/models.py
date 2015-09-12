from django.db import models
from djangotoolbox.fields import ListField


class home_elements(models.Model):
    date = models.DateTimeField()
    name = models.TextField()
    metadata = models.IntegerField()
    img = models.TextField()
    size = models.TextField()
