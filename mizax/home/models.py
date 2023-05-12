from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    ticket_price = models.IntegerField()
    opentime = models.DateTimeField()
