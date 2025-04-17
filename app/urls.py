from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns=[

    path('',views.home_page,name='homepage'),

    path('gfdresdfgjuy',views.about_page,name="aboutpage"),

    path('kmgjfnmojf',views.contact_page,name="contact"),

    path('sxedzfrxxreds',views.register,name="register"),

    path('login',views.login_page,name="login"),

    path('dfdhgfhhgfchf',views.dashboard,name="dashboard"),

    path('gsfthagfsdfgs',views.logout,name="logout"),

    path('bhhhdgfdhshjd',views.cource,name="course"),

    path('gdrgsf/<int:id>/gdrtsweaw',views.subject,name="sub"),

    path('mail',views.mail,name="mail"),

    path('forgot',views.forgotpassword,name="forgotpassword"),

    path('create',views.createaccount,name="createaccount"),

    path('verify/<uidb64>/<token>',views.activate,name="activate"),

    path('cookie',views.cookie_page,name="cookie"),

    path('refresh',views.refresh,name="refresh")
    

    
]
urlpatterns += static(settings.MEDIA_URL, document_roor=settings.MEDIA_ROOT)
