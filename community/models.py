from django.db import models

# Create your models here.
# from community.models import *

class Building(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    floors = models.IntegerField()

    def __unicode__(self):
        return u"Building: {}".format(self.name)

class Apartment(models.Model):
    number = models.CharField(max_length=120)
    size = models.IntegerField()
    rooms = models.IntegerField()
    rent = models.IntegerField()
    building = models.ForeignKey(Building, related_name='building')

    def __unicode__(self):
        return u"{} - Apartment: {}".format(self.building.name, self.number)


class Renter(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    apartment = models.ForeignKey(Apartment, related_name='apartment')
    complaints = models.ManyToManyField(Building, related_name='building_complaints')

    def __unicode__(self):
        return u"{}".format(self.name)
