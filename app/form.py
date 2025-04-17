from django import forms
from django.contrib.auth.models import User
from .models import *  
from django.contrib.auth.forms import AuthenticationForm



class Contactform(forms.ModelForm):

    user_name = forms.CharField(label="user_name",max_length=100,required=True)

    email = forms.EmailField(label="email",max_length=100,required=True)

    subject = forms.CharField(label="subject",max_length=100,required=False)

    content = forms.CharField(label="content",max_length=500,required=True)

    class Meta:
        model= Contactmodel

        fields = ['user_name','email','subject','content']

class Registerform(forms.ModelForm):



    regname = forms.CharField(label="regname",max_length=50,required=True)

    dob = forms.DateField(label="dob",required=True) 

    gender = forms.ChoiceField(label="gender",choices=GENDER_CHOICES,widget=forms.RadioSelect,required=True)

    qualification = forms.CharField(label="qualification",max_length=100,required=False)

    course = forms.ChoiceField(label="course",choices=COURSE_CHOICES, widget=forms.Select, required=True)

    mobile = forms.CharField(label="mobile",max_length=15,required=True)

    regemail = forms.EmailField(label="regemail",max_length=50,required=True)

    gaurdianmobile = forms.CharField(label="gaurdianmobile",max_length=15,required=False)

    mode = forms.ChoiceField(label="mode",choices=MODE_CHOICES,widget=forms.RadioSelect,required=True)

    places = forms.ChoiceField(label="places",choices=LOC_CHOICES,widget=forms.RadioSelect,required=True)

    gaurdianname = forms.CharField(label="gaurdianname",max_length=100,required=False)

    occupation = forms.CharField(label="occupation",max_length=100,required=False)

    time = forms.BooleanField(label="time",required=True,widget=forms.CheckboxInput)

    adress = forms.CharField(label="adress",max_length=100,required=False)

    country = forms.CharField(label="country",max_length=100,required=False)

    state = forms.CharField(label="state",max_length=100,required=False)

    city = forms.CharField(label="city",max_length=100,required=False)

    pincode = forms.CharField(label="pincode",max_length=15,required=False)

    hobbies = forms.MultipleChoiceField(choices=HOBIES,widget=forms.CheckboxSelectMultiple,label=" hobbies")

    avatar = forms.ImageField(label="avatar",required=False)


    class Meta:
        model = Registermodel
        fields = ['regname','dob','gender','qualification','course','mobile','regemail','gaurdianmobile','mode','places','gaurdianname','occupation','time','adress','country','state','city','pincode','hobbies','avatar']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username",max_length=50,required=True)
    password  = forms.CharField(label="password",max_length=50,required=True,widget=forms.PasswordInput)
    otp = forms.CharField(label="otp",max_length=6,required=False)
    cookie_box = forms.BooleanField(label="cookie_box",required=False,widget=forms.CheckboxInput)

class CreateAccount(forms.ModelForm):
    username = forms.CharField(label="username",max_length=50,required=True)
    first_name = forms.CharField(label="first_name",max_length=50,required=True)
    last_name = forms.CharField(label="last_name",max_length=50,required=True)
    email = forms.EmailField(label="email",max_length=50,required=True)
    password = forms.CharField(label="password",max_length=50,required=True,widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="confirm_password",max_length=50,required=True,widget=forms.PasswordInput)
    otp = forms.CharField(label="otp",max_length=6,required=False)

    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

class CreateAccountdetails(forms.ModelForm):
    username = forms.CharField(label="username",max_length=50,required=True)
    first_name = forms.CharField(label="first_name",max_length=50,required=True)
    last_name = forms.CharField(label="last_name",max_length=50,required=True)
    gender = forms.ChoiceField(label="gender",choices=GENDER_CHOICES,widget=forms.RadioSelect,required=True)
    dob = forms.DateField(label="dob",required=True)
    # mobilenumber = forms.CharField(label="mobilenumber",required=True)
    mobile = forms.CharField(label="mobilenumber",max_length=15,required=True)
    email = forms.EmailField(label="email",max_length=50,required=True)


    class Meta:
        model=Accountdetail
        fields = ['username','first_name','last_name','gender','dob','email','mobile']

class PasswordresetForm(forms.Form):
    username = forms.CharField(label="username",max_length=50,required=True)
    email = forms.CharField(label="email",max_length=50,required=True)
    password  = forms.CharField(label="password",max_length=50,required=True,widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="confirm_password",max_length=50,required=True,widget=forms.PasswordInput)
    otp = forms.CharField(label="otp",max_length=6,required=False)

    class Meta:
        model = User
        fields = ['password']
