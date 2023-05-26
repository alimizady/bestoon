from django.db import models
from django.contrib.auth.models import User
class Expence(models.Model):
    tittle = models.CharField(max_length=20)
    date = models.DateTimeField()
    amount = models.IntegerField()

# Create your models here.
