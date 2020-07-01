from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from . import models


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def reg_done(request):
    regobj = models.Register()

    name = request.POST.get('name')
    mail = request.POST.get('mail')
    phone = request.POST.get('phone')
    psw = request.POST.get('psw')
    pswr = request.POST.get('pswr')

    # for register
    regobj.name = name   
    regobj.mail = mail
    regobj.phone = phone
    regobj.psw = psw
    regobj.pswr = pswr
    regobj.save()

    return render(request, 'reg_done.html')

def login_done(request):
    regobj = models.Register()

    mail = request.POST.get('lmail')
    psw = request.POST.get('lpsw')

    # for login
    mail = regobj.mail 
    psw = regobj.psw  

    if lmail == mail:
        return render(request, 'login_done.html')
    else:
        return render(request, 'sorry.html')

