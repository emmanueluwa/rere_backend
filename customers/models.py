from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=100)
  industry = models.CharField(max_length=100)