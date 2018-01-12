from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    number = models.IntegerField()

class Weekend(models.Model):
    weekend = models.IntegerField()
    saturday = models.CharField(max_length = 255)
    sunday = models.CharField(max_length = 255)
    employee = models.ForeignKey(Employee, related_name="Weekend")
