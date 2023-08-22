from django.db import models

class categories(models.Model):
    name = models. CharField(max_length=100)

class sub_categories(models.Model):
    name = models. CharField(max_length=100)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)

class brand (models.Model):
    name = models.CharField(max_length=100)

class product(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(sub_categories, on_delete=models.CASCADE)
    size = models.CharField( max_length=5,blank=True, null=True)
    color = models.CharField(max_length=15,blank=True, null=True)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    stock_available = models.BooleanField()
    delivery_time = models.IntegerField()
    base_price = models.DecimalField(max_digits=10 , decimal_places=3)
    sale_price = models.DecimalField(max_digits=10 , decimal_places=3)
    discount = models.DecimalField(blank=True, null=True ,max_digits=5 , decimal_places=3)
    product_img =  models.ImageField(upload_to='images/',blank= True,null=True)  








    