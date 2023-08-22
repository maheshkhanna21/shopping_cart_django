from django.db import models
from django.utils import timezone

# Create your models here.

class cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    created_at = models.TimeField(auto_now= timezone.now() )