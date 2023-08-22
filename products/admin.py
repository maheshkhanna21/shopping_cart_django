from django.contrib import admin
from .models import *
from django.db import OperationalError

admin.site.register(product)
admin.site.register(brand)
admin.site.register(categories)
admin.site.register(sub_categories)
