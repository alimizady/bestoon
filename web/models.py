from django.db import models
from django.contrib.auth.models import User
class Expence(models.Model):
    tittle = models.CharField(max_length=20)
    date = models.DateTimeField()
    amount = models.IntegerField()
    def __str__(self):
        return self.tittle
class Income(models.Model):
    tittle = models.CharField(max_length=20)
    date = models.DateTimeField()
    amount = models.IntegerField()
    def __str__(self):
        return self.tittle