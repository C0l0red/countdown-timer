from django.db import models


class Event(models.Model):
    name = models.CharField()
    date = models.DateTimeField()