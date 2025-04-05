from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home_page(req):

    title = "home page"

    return render(req,"home.html",{"title":title})

def about_page(req):

    title = "about page"

    return render(req,"about.html",{"title":title})

def contact_page(req):
    title = "contact page"
    form = Contactform(req.POST)

    if req.method=='POST':

        if form.is_valid():

            user = form.save(commit=False)

            mail=  req.POST.get('email')
            subject = req.POST.get('subject')
            text = req.POST.get('content')
            name = req.POST.get('user_name')
            # message = f"Name : {name}\nEmail : {mail}\nContent : {text}"
            message = ""
            html =f""" 
                <html>
                    <body>
                        <h1 style="text-align: center;color: rgb(0, 255, 68);">YOUR EMAIL</h1>
                        <h3 >Name : <span style="color: red;">{name}</span></h3>
                        <h3>Email : <span style="color: red;">{mail}</span></h3>
                        <h3>Content : <span style="color: red;"><br> &emsp; &emsp;&emsp;{text}</span></h3>
                    </body>
                </html>
            """

            try:
                send_mail(
                    subject = subject,
                    message = message,
                    from_email = mail,
                    html_message= html,
                    recipient_list = ['rejinrjr144@gmail.com'],
                )
                # user.save()
                return redirect('app:homepage')
            except Exception as e:
                return HttpResponse(f"An error occurred while sending the email {e}")

    return render(req,"contact.html",{"title":title,"form":form})

    

def register(req):

    title = "register_form"
    if req.method == 'POST':
        print(req.POST,'files**** ',req.FILES)
        form = Registerform(req.POST , req.FILES)
        print("registerform done")
        if form.is_valid():
            print("registerform is valid")

            form.save()

            return redirect('app:homepage')

        else:
            print("form not valid","*/*/*/*/",form.errors)

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
    
    courses = Courses.objects.all()

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
