from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from Interview import views
=======
>>>>>>> 247da9ca82931d96dba4455f5b77502d592b4b39
from django.conf import  settings
from django.conf.urls.static import  static
from . import  views

urlpatterns = [

<<<<<<< HEAD
    path('welcome/',views.welcome,name="welcome"),
=======
    path('', views.welcome,name="welcome"),
>>>>>>> 247da9ca82931d96dba4455f5b77502d592b4b39
    path('home/',views.home,name="home"),
    path('register',views.register,name="register"),
    path('interviewer', views.interviewer,name="interviewer"),#Interviewer Login
    path('hr_login', views.hr_login,name="hr_login"),
<<<<<<< HEAD
    path('hr_page/', views.hr_page, name="hr_page"),#After Login
    path('interviewer_page/', views.interviewer_page, name="interviewer_page"),#After Login
    path('interview_details/', views.interview_details, name="interview_details"),#Mayuri's code
    path('hr/', views.hr, name="Info"), #saumya's code
    path('submit_candidateinfo/', views.submit_candidateinfo, name="submit") #saumya's code
=======
   path('interview_details', views.interview_details, name="interview_details"),
    path('hr', views.hr, name="hr"), #saumya's code
    path('submit_candidateinfo/', views.submit_candidateinfo, name="submit"),
    path('', views.Logout, name="Logout")
>>>>>>> 247da9ca82931d96dba4455f5b77502d592b4b39
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
