from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .form import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.conf.urls.static import static
import os
from django.contrib.staticfiles import finders
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import authenticate,login,logout as djangologout
import secrets
from django.contrib.auth import get_user_model


from django.http import JsonResponse
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
        form = Registerform(req.POST , req.FILES)
        if form.is_valid():
            print("registerform is valid")
            form.save()
            return redirect('app:homepage')
        
        return render(req,"register_form.html",{"form":form})
    else:
        form = Registerform()

    return render(req,"register_form.html",{"title":title})

# def mail(req):

#     subject = "RJR image"
#     from_email = settings.EMAIL_HOST_USER
#     to = ['raeevndranraeevndran144@gmail.com']
#     msg = EmailMultiAlternatives(subject,from_email,"message",to)

#     html = f"""
#         <html>
#             <body>
#                 <h1>vanakkam</h1>
#                 <img src="cid:image1" alt="">
#                 <h5>click here to activate</h5>
#             </body>
#         </html>
#     """
#     msg.attach_alternative(html,"text/html")
#     image_path = "./5star.png"

#     with open(image_path,'rb')as img:
#         image = MIMEImage(img.read())
#         image.add_header('content-ID','<image1>')
#         msg.attach(image)
#     msg.send()

#     print(req.errors)
#     return HttpResponse("mail sended")

def mail(req,user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.id))
    site = get_current_site(req)
    domain = site.domain
    print(user.id,"*******",uid,"*******",token)
    message = render_to_string(
        "mail.html",
        {'uid':uid,
        'token':token,
        'user':user,
        'domain':domain
        }
    )
    print("email = ",user.email)
    subject = 'verification mail from RJR'
    recipient_list=[user.email]
    email = EmailMessage(subject,message,'rejinrjr144@gmail.com',to=recipient_list)
    email.content_subtype='html'
    email.send()

def activate(req,uidb64,token):

    pk = urlsafe_base64_decode(uidb64).decode()
    user = get_object_or_404(User,pk = pk)

    if default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('app:login')
    
def cookie_page(req):
    return render(req,"cookie.html")

def refresh(req):

    if OTP.objects.exists():
        OTP.objects.all().delete()  # delete otp when any store in db
    return redirect("app:login")
    
def login_page(req):
    title = "login"
    
    if req.method == 'POST':


        form = LoginForm(req,data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            cookie_box = form.cleaned_data.get('cookie_box')
            input_code = form.cleaned_data.get('otp')
            user = authenticate(username = username,password = password)
            # OTP.objects.filter(created_at__lt=timezone.now()).delete()  # delete otp when any store in db
                
            if user is not None:
                try:
                    latest_otp = OTP.objects.filter(user = user).latest('created_at')
                    if latest_otp.is_expired(): # if otp is expired
                        latest_otp.delete()
                        raise OTP.DoesNotExist
                except OTP.DoesNotExist:
                    otp_code = generate_otp()       # to generate otp
                    OTP.objects.create(user = user,code = otp_code)  # create in db otp
                    user_email = user.email     
                    otp = otp_code
                    send_otp(user_email,otp)
                    return render(req,"login.html",{
                        "title":title,
                        "form":form,
                        "otp_send":True,
                        "username":username,
                        "password":password
                        })
                if input_code and input_code == latest_otp.code and not latest_otp.is_expired(): # login if all contition is true
                    login(req,user)                             # for login
                    latest_otp.delete()                         # after login delete otp from db;

                    if cookie_box is True:                      # for save cookies
                        set_cookies(req,username)
                        get_cookies(req)
                        return redirect("app:homepage")
                    else:                                       # for save session
                        return render(req,"login.html")

                else:
                    return HttpResponse(print(form.errors))
            else:
                print(form.errors)
        else:
            print(form.errors)
            return render(req,"login.html",{"title":title,"form":form})

    return render(req,"login.html",{"title":title})

def set_cookies(req,name):
    response = HttpResponse("cookies set")
    response.set_cookie(key='username',value = name,max_age=3600*24*15)
    return response

def get_cookies(req):
    username = req.COOKIES.get('username')
    print(username)
    return HttpResponse(username)

def delete_cook(req):
    response = HttpResponse("delete cookie")
    response.delete_cookie('username')
    return response

def generate_otp(length=6):
    otp = ''.join([str(secrets.randbelow(10))for _ in range(length)])
    return otp

def send_otp(user_email,otp):
    subject = "your otp code"
    message = f"Your otp code is {otp}.it will expire in 5-minutes"
    
    from_  = settings.EMAIL_HOST_USER
    send_mail(subject,message,from_,[user_email])

def dashboard(req):

    title = "dashboard"

    return render(req,"dashboard.html",{"title":title})

def logout(req):
    djangologout(req)
    response = redirect("app:homepage")
    response.delete_cookie("username")

    return response 

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

def forgotpassword(req):
    if req.method == 'POST':
        form = PasswordresetForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            input_code = form.cleaned_data.get('otp')
            user = get_user_model().objects.get( email=email) 
            try:
                latest_otp = OTP.objects.filter(user = user).latest('created_at')
                if latest_otp.is_expired(): # if otp is expired
                    latest_otp.delete()
                    raise OTP.DoesNotExist
            except OTP.DoesNotExist:
                otp_code = generate_otp()       # to generate otp
                OTP.objects.create(user = user,code = otp_code)  # create in db otp
                user_email = user.email     
                otp = otp_code
                send_otp(user_email,otp)
                return render(req,"forgotpassword.html",{
                    # "title":title,
                    "form":form,
                    "otp_sends":True,
                    "username":username,
                    "password":password,
                    "email":email,
                    "password":password
                    })
            
            if input_code and input_code == latest_otp.code and not latest_otp.is_expired() and password == confirm_password: # login if all contition is true
                User = get_user_model()
                user = User.objects.get(email = email)  # Or use email/id
                user.set_password(password)
                user.username
                user.save()
                latest_otp.delete()
                print(user.save())

            else:
                return render(req,"forgotpassword.html")
            
            return HttpResponse("data saved")

        # else:
        #     print(form.errors)

        else:
            print(form.errors)
            return render(req,"forgotpassword.html")

    return render(req,"forgotpassword.html")

def createaccount(req):
    title = "create account"
    if req.method == 'POST':
        form = CreateAccount(req.POST)
        copyform = CreateAccountdetails(req.POST)
        if form.is_valid():
            inpassword = form.cleaned_data.get('password')
            confirm_password  = form.cleaned_data.get('confirm_password')
            
            if inpassword == confirm_password :
                copyform.save()
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.is_active = False
                try:
                    user.save()
                    user = User.objects.get(email=user.email)
                    mail(req,user)
                    return HttpResponseRedirect('https://mail.google.com/')
                except Exception as e:
                    print(form.errors)
        return render(req,"createaccount.html",{"form":form})
    else:
        pass
    return render(req,"createaccount.html",{"title":title})

# def otp(req):
