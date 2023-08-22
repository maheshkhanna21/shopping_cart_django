from django.shortcuts import render

from django.http import HttpResponse
from .models import contact
# Create your views here.
def submit_contact(request):
    name = request.POST['name']
    mobile = request.POST['mobile']
    email = request.POST['email']
    description = request.POST['description']

    contact_form = contact()
    contact_form.name = name
    contact_form.mobile = mobile
    contact_form.email = email
    contact_form.description = description
    contact_form.save()
    return HttpResponse('hello')