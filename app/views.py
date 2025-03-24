from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.

def home_page(req):

    title = "home page"

    return render(req,"home.html",{"title":title})

def about_page(req):

    title = "about page"

    return render(req,"about.html",{"title":title})

def contact_page(req):

    title = "contact page"

    return render(req,"contact.html",{"title":title})

def register(req):

    title = "register_form"

    return render(req,"register_form.html",{"title":title})

def login_page(req):

    title = "login"

    return render(req,"login.html",{"title":title})

def dashboard(req):

    title = "dashboard"

    return render(req,"dashboard.html",{"title":title})

def logo(req):

    title = "*"

    return render(req,"tems.html",{"title":title})

def cource(req):

    title = "cources"

    return render(req,"cources.html",{"title":title})