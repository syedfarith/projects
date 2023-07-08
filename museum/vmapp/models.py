from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField(max_length=20)


