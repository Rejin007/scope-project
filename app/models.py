from django.db import models
# Create your models here.
GENDER_CHOICES = [
        ('male', 'male'),
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

    hobbies = models.BooleanField(default=False)

    avatar = models.ImageField(upload_to='images/',null=True,blank=True)