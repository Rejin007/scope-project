from django.db import models
from django.utils.text import *

# Create your models here.

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

#==============================================================================================

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

