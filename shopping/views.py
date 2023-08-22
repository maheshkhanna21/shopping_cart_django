from django.shortcuts import render, redirect
from products.models import *
from .models import cart

# Create your views here.

def products_for_index(request):
    items = product.objects.all() #to fetch all products from database
    
    data = {
        'products' : items
    }
    return render(request, 'index.html', data)

def product_detail(request, id):
    item = product.objects.get(id = id)    # to fetch only one product by using id
    data = {
        'product' : item
    }
    return render(request, 'productdetail.html', data)

def add_to_cart(request, id):
    product_id = id
    user_id = request.user.id
    temp_cart = cart()
    temp_cart.user_id = user_id
    temp_cart.product_id = product_id
    temp_cart.save()
    
    
    return redirect('/view_cart')
    # return render(request, 'addcart.html', data)
    # return HttpResponse()
    
def view_cart(request):
    user_id = request.user.id
    cart_items = cart.objects.filter(user_id = user_id) # to fetch multiple objects from django ORM
    data = {
        'cart_items' : cart_items
    }
    return render(request, 'addcart.html', data)