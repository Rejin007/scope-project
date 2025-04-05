from django import forms
from django.contrib.auth.models import User
from .models import *  


GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'female'),
        ('other', 'other'),
    ]
MODE_CHOICES=[
    ('online','online'),
    ('offline','offline')
]
LOC_CHOICES=[
    ('technopark','technopark'),
    ('thampanoor','thampanoor'),
    ('kochi','kochi'),
    ('nagarcoil','nagarcoil'),
    ('online','online'),
]
COURSE_CHOICES = [
        ('PHP Fullstack', 'PHP Fullstack'),
        ('Python Fullstack', 'Python Fullstack'),
        ('Java Fullstack', 'Java Fullstack'),
        ('C#.NET Core 7 Fullstack', 'C#.NET Core 7 Fullstack'),
        ('MEAN Fullstack', 'MEAN Fullstack'),
        ('MERN Fullstack', 'MERN Fullstack'),
        ('Data Science & AI (Python Guru)', 'Data Science & AI (Python Guru)'),
        ('Python Mastery (Python / Django / MYSQL)', 'Python Mastery (Python / Django / MYSQL)'),
        ('Google Flutter Mobile App Development (iOS / Android)', 'Google Flutter Mobile App Development (iOS / Android)'),
        ('UI/UX Designing', 'UI/UX Designing'),
        # Add more courses as needed...
    ]

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

    hobbies = forms.BooleanField(label="hobbies",required=False,widget=forms.CheckboxInput)

    avatar = forms.ImageField(label="avatar",required=False)

    class Meta:
        model = Registermodel
        fields = ['regname','dob','gender','qualification','course','mobile','regemail','gaurdianmobile','mode','places','gaurdianname','occupation','time','adress','country','state','city','pincode','hobbies','avatar']
