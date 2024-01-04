from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=100)
  industry = models.CharField(max_length=100)

  #admin display name instead of "object(2)"
  def __str__(self):
    return self.name

class Order(models.Model):
  customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
  description = models.CharField(max_length=500)
  #to avoid using float: use pence and convert to pound(/100), nodecimal type in sqllite3
  totalInPence = models.IntegerField()

  #admin display name instead of "object(2)"
  def __str__(self):
    return self.description