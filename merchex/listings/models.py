from django.db import models

# Create your models here.

class Players(models.Model):
    name = models.fields.CharField(max_length=100)

class Teams(models.Model):
    name = models.fields.CharField(max_length=100)
