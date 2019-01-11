from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=8)
    email = models.CharField(max_length=30)


