from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=25)
    pupulation = models.IntegerField()
    created = models.DateTimeField()
