from django.db import models


class Timer(models.Model):
    title = models.CharField(max_length=100)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=25)
    seconds = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    uuid = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
