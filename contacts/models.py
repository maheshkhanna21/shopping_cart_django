from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    # user_id = models.IntegerField(default=None, blank=True, null=True)

