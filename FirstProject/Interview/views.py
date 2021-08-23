from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.
def home(request):
    return render(request, 'Home.html')
def welcome(request):
    return render(request,'welcome.html')
def hr_login(request):
    return render(request, 'HR_login.html')
def interviewer(request):
    return render(request, 'Interviewer_Login.html')
