from django.db import models

from django.db import models


class motor(models.Model):
    mid= models.CharField(max_length=1000)
    Temp = models.FloatField()
    voltage = models.FloatField()
    current = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    status = models.CharField(max_length=1000)
