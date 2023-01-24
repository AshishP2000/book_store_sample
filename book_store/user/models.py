# Create your models here.

from django.db import models


class Registration(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.BigIntegerField(default=0)
