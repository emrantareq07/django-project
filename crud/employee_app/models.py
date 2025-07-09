from django.db import models

class member(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
