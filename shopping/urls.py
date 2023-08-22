from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.products_for_index),
    path('productdetail/<int:id>', views.product_detail),
    path('addcart/<int:id>', views.add_to_cart),
    path('view_cart', views.view_cart)
    
    
]