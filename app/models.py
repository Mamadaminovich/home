from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    optional_car_available = models.BooleanField(default=False)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)