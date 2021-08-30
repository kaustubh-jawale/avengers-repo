from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import  static
from . import  views

urlpatterns = [

    path('', views.welcome,name="welcome"),
    path('home/',views.home,name="home"),
    path('register_both/', views.register_both, name="register_both"),

    #Registration for both
    path('hr_register', views.hr_register, name="hr_register"),
    path('interviewer_register',views.interviewer_register,name="interviewer_register"),

    #Login For for both
    path('interviewer', views.interviewer,name="interviewer"),
    path('hr_login', views.hr_login,name="hr_login"),

    path('<int:id>',views.detail,name="detail"),
    #After Login
    path('slot', views.slots, name="slot"),

    path('hr', views.hr, name="hr"),
    path('submit_candidateinfo', views.submit_candidateinfo, name="submit_candidateinfo"),


    #Logout
    path('', views.Logout, name="Logout"),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
