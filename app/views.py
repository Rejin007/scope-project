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
    title = "Courses"
    
    # Fetch the course using the course_code passed from the URL
    
    obj = Courses.objects.all()
    print(obj,11111)
    
    
    courses = obj

    return render(req, "cources.html", {"title": title, "courses": courses})


def subject(req,id):

    courses = Courses.objects.get(id=id)

    title = courses.course_name

    subject = Java_Full_Stack.objects.all()

    python = Python_Full_Stack.objects.all()

    php = PHP_Full_Stack.objects.all()

    core = Net_Core_Full_Stack.objects.all()

    mern = MERN_Full_Stack.objects.all()

    mean = MEAN_Full_Stack.objects.all()

    flutter = Flutter.objects.all()

    ionic = IONIC.objects.all()

    Website = Website_Designing.objects.all()
    
    ui_ux = UI_UX.objects.all()
    
    Software = Software_Testing.objects.all()
    
    Networking = Networking_Server.objects.all()
    
    aws = AWS.objects.all()
    
    ms = Ms_Azure.objects.all()
    
    rhcsa = RHCSA.objects.all()
    
    rhce = RHCE.objects.all()
    
    devOps = DevOps_Engineer.objects.all()
    
    ccna = CCNA.objects.all()
    
    data_Science = Data_Science.objects.all()
    
    data_Analytics = Data_Analytics.objects.all()
    
    digital_Marketing = Digital_Marketing.objects.all()
    
    microsoft = Microsoft.objects.all()
    
    






    # key = Subject.objects.all()

    return render(req,"subjects.html",{

            "title":title ,
            'subject':subject , 
            "courses": courses,
            "python":python,
            "php":php,
            "core":core,
            "mern":mern,
            "mean":mean,
            "flutter":flutter,
            "ionic":ionic,

            "Website":Website,
            "ui_ux":ui_ux,
            "Software":Software,
            "Networking":Networking,
            "aws":aws,
            "ms":ms,
            "rhcsa":rhcsa,
            "rhce":rhce,
            "devOps":devOps,
            "ccna":ccna,
            "data_Science":data_Science,
            "data_Analytics":data_Analytics,
            "digital_Marketing":digital_Marketing,
            "microsoft":microsoft,


        })

