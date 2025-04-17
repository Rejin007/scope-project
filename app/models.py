from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.
GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
MODE_CHOICES=[
    ('online','Online'),
    ('offline','Offline')
]
HOBIES = [
    ('Extracurricular activities', 'Extracurricular activities'),
    ('Reading Books', 'Reading Books'),
    ('Sports', 'Sports'),
    ('Music', 'Music'),
]
LOC_CHOICES=[
    ('technopark','Technopark'),
    ('thampanoor','Thampanoor'),
    ('kochi','Kochi'),
    ('nagarcoil','Nagarcoil'),
    ('online','Online'),
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
        ('Digital Marketing Master Program','Digital Marketing Master Program'),
        ('Software Testing Advanced (Manual / Automation)','Software Testing Advanced (Manual / Automation)'),
        ('Software Testing Manual (ISTQB)','Software Testing Manual (ISTQB)'),
        ('ISTQB CERTIFICATION (EXAM Reg)','ISTQB CERTIFICATION (EXAM Reg)'),
        ('Selenium Testings & Cuccumber / Appium Mobile / QTP / Landrunner / Jmeter / Jira','Selenium Testings & Cuccumber / Appium Mobile / QTP / Landrunner / Jmeter / Jira'),
        ('Computer Networking (CCNA)','Computer Networking (CCNA)'),
        ('Server Admin (MCSE)','Server Admin (MCSE)'),
        ('Server Admin (RHCE)','Server Admin (RHCE)'),
        ('Networking & Server Admin (CCNA / MCSE / Hardware )','Networking & Server Admin (CCNA / MCSE / Hardware )'),
        ('Networking & Server Admin (CCNA / RHCE / Hardware)','Networking & Server Admin (CCNA / RHCE / Hardware)'),
        ('Networking & Server Admin (CCNA / MCSE / RHCE / Hardware)','Networking & Server Admin (CCNA / MCSE / RHCE / Hardware)'),
        ('Security Surveillance & Networking Internship(CCNA / CCTV / Hardware)','Security Surveillance & Networking Internship(CCNA / CCTV / Hardware)'),
        ('Cloud Admin (AWS / MS AZURE)','Cloud Admin (AWS / MS AZURE)'),
        ('Cloud & Networking Admin (CCNA / AWS / Hardware)','Cloud & Networking Admin (CCNA / AWS / Hardware)'),
        ('Cloud & Networking Admin (CCNA / MS ASURE / Hardware)','Cloud & Networking Admin (CCNA / MS ASURE / Hardware)'),
        ('Cloud & Networking Admin (CCNA / AWS)','Cloud & Networking Admin (CCNA / AWS)'),
        ('Cloud & Networking Admin (CCNA / MS AZURE)','Cloud & Networking Admin (CCNA / MS AZURE)'),
        ('Cloud & Server Admin (MCSE / AWS / Hardware)','Cloud & Server Admin (MCSE / AWS / Hardware)'),
        ('Cloud & Server Admin (MCSE / MS AZURE / Hardware)','Cloud & Server Admin (MCSE / MS AZURE / Hardware)'),
        ('Cloud & Server Admin (RHCE / AWS / Hardware)','Cloud & Server Admin (RHCE / AWS / Hardware)'),
        ('Cloud & Server Admin (RHCE / MS AZURE / Hardware)','Cloud & Server Admin (RHCE / MS AZURE / Hardware)'),
        ('Cloud,Networking,Server Admin (CCNA / AWS / AZURE / MCSE / RHCE /Hardware)','Cloud,Networking,Server Admin (CCNA / AWS / AZURE / MCSE / RHCE /Hardware)'),
        ('Devops Mastery (All Together)','Devops Mastery (All Together)'),
        ('Devops-Selective','Devops-Selective'),
        ('Academic Project','Academic Project'),
        ('Ms Office (World / Excel / Power Point / Out Look)','Ms Office (World / Excel / Power Point / Out Look)'),
        ('Data Analytics','Data Analytics'),
        ('Advanced Ms Excel','Advanced Ms Excel'),
        ('Graphic Designing (Photoshop)','Graphic Designing (Photoshop)'),
        ('Graphic Designing  (Photoshop / Illustrator)','Graphic Designing  (Photoshop / Illustrator)'),
        ('None Of The Above , Will Discuss Directly','None Of The Above , Will Discuss Directly'),
    ]


class Courses(models.Model):
    
    course_name = models.CharField(name='course_name',max_length=100)


    def __str__(self):
        return f"{self.course_name} "

class Subject(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=90)

    f_key = models.ForeignKey(Courses,on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name

class Java_Full_Stack(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Python_Full_Stack(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class PHP_Full_Stack(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Net_Core_Full_Stack(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class MERN_Full_Stack(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class MEAN_Full_Stack(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Flutter(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class IONIC(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Website_Designing (models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class UI_UX(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Software_Testing(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Networking_Server(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class AWS(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Ms_Azure(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class RHCSA(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class RHCE(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class DevOps_Engineer(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class CCNA(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Data_Science(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Data_Analytics(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Digital_Marketing(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Microsoft(models.Model):

    sub_name = models.CharField(name="sub_name",max_length=100)

class Contactmodel(models.Model):

    user_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100,unique=False)

    subject = models.CharField(max_length=100)

    content = models.CharField(max_length=500)

    def __str__(self):
        return self.user_name

class Registermodel(models.Model):

    regname = models.CharField(max_length=50)

    dob = models.DateField()

    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    qualification = models.CharField(max_length=100)

    course = models.CharField(max_length=100,choices=COURSE_CHOICES)

    mobile = models.CharField(max_length=15)

    regemail = models.EmailField(max_length=50,unique=True)

    gaurdianmobile = models.CharField(max_length=15)

    mode = models.CharField(max_length=100,choices=MODE_CHOICES)

    places =  models.CharField(max_length=100,choices=LOC_CHOICES)

    gaurdianname = models.CharField(max_length=100)

    occupation = models.CharField(max_length=100)

    time = models.BooleanField(default=False)

    adress = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    pincode = models.CharField(max_length=15)

    hobbies = models.CharField(max_length=50)

    avatar = models.ImageField(upload_to='images/',null=True,blank=True)

class Accountdetail(models.Model):

    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=15)
    dob = models.DateField() 
    email = models.EmailField(max_length=50,unique=True)
    mobile = models.CharField(max_length=15)

   
class OTP(models.Model):
    email = models.EmailField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    def is_expired(self):
        return timezone.now()>self.created_at+datetime.timedelta(minutes=5)