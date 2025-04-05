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

    path('srtsrsfcggggggggggggddtgd',views.login_page,name="login"),

    path('dfdhgfhhgfchf',views.dashboard,name="dashboard"),

    path('gsfthagfsdfgs',views.logo,name="logo"),

    path('bhhhdgfdhshjd',views.cource,name="course"),

    path('gdrgsf/<int:id>/gdrtsweaw',views.subject,name="sub"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_roor=settings.MEDIA_ROOT)
