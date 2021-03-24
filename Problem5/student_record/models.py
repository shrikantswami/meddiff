from django.db import models

# Create your models here.


class Records(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=20)
