from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from django.contrib.auth import authenticate,login 
from django.contrib.auth import logout

from products.models import product



# def home(request):
#     user = request.user
#     return render(request,'index.html', {'user': user})

def addcart(request):
    return render(request,'addcart.html')

def billing(request):
    return render(request,'billing.html')

def index(request):
    products =  product.objects.all()
    
    return render(request,'index.html' , {'products': products})

def placeorder(request):
    return render(request,'placeorder.html')

def details(request):
    return render(request,'productdetail.html')

def step(request):
    return render(request,'step.html')

def print_name(request, name):
    return name


def my_self1(request):
    me = {
        "first_name": "japnoor",
        "middle_name": "kaur",
        "last_name": "choudhary"
    }

    return render(request, "about_me.html",me)


def my_self(request):
    viewed = {
        "comp_language" : [5,61,17,15,198,5261],
        "students_list" : [
            'mahesh',
            'noor',
            'shivam',
            'komal'
        ]
    }
    return render(request, "about_me.html",viewed) 

def login_page(request):
    return render(request,'login.html')  
    
def submit(request):
    username = request.POST['uname']
    password = request.POST['psw']

    user = authenticate( request, username= username, password= password)
    if user is not None:
        login(request, user)

        return redirect('/index')
    else:
        return redirect('/login')
#    print(request.POST['uname'])
 #   print(request.POST['psw'])
  #  return HttpResponse( request.POST['psw'])
    
def logout_view(request):
     logout(request)

     return redirect('/login')

def contact(request):
    return render(request,'contact.html')
