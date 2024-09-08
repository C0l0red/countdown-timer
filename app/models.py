from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Timer(models.Model):
    title = models.CharField(max_length=100)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=25, validators=[MaxValueValidator(59), MinValueValidator(0)])
    seconds = models.IntegerField(default=0, validators=[MaxValueValidator(59), MinValueValidator(0)])
    priority = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
