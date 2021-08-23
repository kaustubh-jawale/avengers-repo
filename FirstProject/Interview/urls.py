from django.contrib import admin
from django.urls import path
from Interview import views
from django.conf import  settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('home/', views.home, name="home"),
    path('interviewer/', views.interviewer, name="interviewer"),
    path('hr_login/', views.hr_login, name="hr_login"),
    path('register', views.register, name="register"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
