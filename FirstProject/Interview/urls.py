from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import  static
from . import  views

urlpatterns = [

    path('', views.welcome,name="welcome"),
    path('home/',views.home,name="home"),
    path('register',views.register,name="register"),
    path('interviewer', views.interviewer,name="interviewer"),#Interviewer Login
    path('hr_login', views.hr_login,name="hr_login"),
    path('hr_page/', views.hr_page, name="hr_page"),#After Login
    path('interviewer_page/', views.interviewer_page, name="interviewer_page"),#After Login
    path('interview_details/', views.interview_details, name="interview_details"),
    path('hr', views.hr, name="hr"), #saumya's code
    path('submit_candidateinfo/', views.submit_candidateinfo, name="submit"),
    path('', views.Logout, name="Logout")
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
