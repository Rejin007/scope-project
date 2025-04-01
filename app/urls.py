from django.urls import path
from app import views

app_name = 'app'

urlpatterns=[

    path('',views.home_page,name='homepage'),

    path('gfdresdfgjuy',views.about_page,name="aboutpage"),

    path('kmgjfnmojf',views.contact_page,name="contact"),

    path('sxedzfrxxreds',views.register,name="register"),

    path('srtsrsfcggggggggggggddtgd',views.login_page,name="login"),

    path('dfdhgfhhgfchf',views.dashboard,name="dashboard"),

    path('gsfthagfsdfgs',views.logo,name="logo"),

    path('bhhhdgfdhshjd',views.cource,name="course"),

    path('gdrgsf/<int:id>/gdrtsweaw',views.subject,name="sub"),

    
]