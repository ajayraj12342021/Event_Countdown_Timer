from os import name

from django.db import models

class Event(models.Model):
    Event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.Event_name


