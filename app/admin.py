from django.contrib import admin
from .models import *

# Register your models here.

class Admincontact(admin.ModelAdmin):

    list_display = ['course_name']

class Adminsubject(admin.ModelAdmin):

    list_display = ['sub_name','f_key']

class Adminjava(admin.ModelAdmin):

    list_display=['sub_name']

class Adminpython(admin.ModelAdmin):

    list_display=['sub_name']

class Adminphp(admin.ModelAdmin):

    list_display=['sub_name']

class Admincore(admin.ModelAdmin):

    list_display=['sub_name']

class AdminMERN(admin.ModelAdmin):

    list_display=['sub_name']

class AdminMEAN(admin.ModelAdmin):

    list_display=['sub_name']

class AdminFlutter(admin.ModelAdmin):

    list_display=['sub_name']

class AdminIONIC(admin.ModelAdmin):

    list_display=['sub_name']

class AdminWebsite(admin.ModelAdmin):

    list_display=['sub_name']

class AdminUI_UX(admin.ModelAdmin):

    list_display=['sub_name']

class AdminSoftware_Testing(admin.ModelAdmin):

    list_display=['sub_name']

class AdminNetworking_Server(admin.ModelAdmin):

    list_display=['sub_name']

class AdminAWS(admin.ModelAdmin):

    list_display=['sub_name']

class AdminMs_Azure(admin.ModelAdmin):

    list_display=['sub_name']

class AdminRHCSA(admin.ModelAdmin):

    list_display=['sub_name']

class AdminRHCE(admin.ModelAdmin):

    list_display=['sub_name']

class AdminDevOps_Engineer(admin.ModelAdmin):

    list_display=['sub_name']

class AdminCCNA(admin.ModelAdmin):

    list_display=['sub_name']

class AdminData_Science(admin.ModelAdmin):

    list_display=['sub_name']

class AdminData_Analytics(admin.ModelAdmin):

    list_display=['sub_name']

class AdminDigital_Marketing(admin.ModelAdmin):

    list_display=['sub_name']

class AdminMicrosoft(admin.ModelAdmin):

    list_display=['sub_name']



admin.site.register(Courses,Admincontact)
admin.site.register(Subject,Adminsubject)
admin.site.register(Java_Full_Stack,Adminjava)
admin.site.register(Python_Full_Stack,Adminpython)
admin.site.register(PHP_Full_Stack,Adminphp)
admin.site.register(Net_Core_Full_Stack,Admincore)
admin.site.register(MERN_Full_Stack,AdminMERN)
admin.site.register(MEAN_Full_Stack,AdminMEAN)
admin.site.register(Flutter,AdminFlutter)
admin.site.register(IONIC,AdminIONIC)
admin.site.register(Website_Designing,AdminWebsite)
admin.site.register(UI_UX,AdminUI_UX)
admin.site.register(Software_Testing,AdminSoftware_Testing)
admin.site.register(Networking_Server,AdminNetworking_Server)
admin.site.register(AWS,AdminAWS)
admin.site.register(Ms_Azure,AdminMs_Azure)
admin.site.register(RHCSA,AdminRHCSA)
admin.site.register(RHCE,AdminRHCE)
admin.site.register(DevOps_Engineer,AdminDevOps_Engineer)
admin.site.register(CCNA,AdminCCNA)
admin.site.register(Data_Science,AdminData_Science)
admin.site.register(Data_Analytics,AdminData_Analytics)
admin.site.register(Digital_Marketing,AdminDigital_Marketing)
admin.site.register(Microsoft,AdminMicrosoft)







