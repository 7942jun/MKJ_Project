from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=8)
    email = models.CharField(max_length=30)

class Memory(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

