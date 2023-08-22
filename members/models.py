from django.db import models
# from django.contrib import admin
class human(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    pancard = models.CharField( max_length=50)
    address = models.TextField(),

class category(models.Model):
    # id = models.IntegerField(("5"))
    name = models.CharField(max_length=100)

