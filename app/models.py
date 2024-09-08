from django.contrib.auth.models import User
from django.db import models


class Timer(models.Model):
    title = models.CharField(max_length=100)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=25)
    seconds = models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
