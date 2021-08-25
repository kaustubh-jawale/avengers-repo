from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import  HttpResponse
from django.contrib import admin
from django.contrib.auth import  authenticate
from .models import Candidate,Employee

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def welcome(request):
    return render(request, 'welcome.html')

#Registration Code here
def register(request):
    # if request from registration.html is POST, get all details in variables
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        # check if password and confirm password both are same
        if password == confirm_password:
            # check whether same username is there any database
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            else:
                # if not same username, register the user
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                                                username=username, password=password)

                user.save()
                return redirect('/')
        else:
            # printing message if password doesnt match
            messages.info(request, 'Password not matched')
            return redirect('register')
        return redirect('register')

    # if the request from registration.html is GET, then transfer it to registration.html
    else:
        return render(request, 'registration.html')

#Aunthentication of HR from DB
def hr_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'hr_candidateinfo.html')
        else:
            messages.error(request, "Enter correct credentials..")
            return render(request, 'hr_login.html')
          
    return render(request, 'HR_login.html')


#Authentication of Interviewer from DB

def interviewer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'interview_details.html')
        else:
            messages.error(request,"Enter correct credentials..")
            return render(request, 'Interviewer_Login.html')

    return render(request, 'Interviewer_Login.html')


#After Login navigate to this  pages




#Interviewer reg- Mayuri's Code added
def interview_details(request):
        if request.method == "POST":
            emp_first_name = request.POST.get('first_name', '')
            emp_last_name = request.POST.get('last_name', '')
            emp_ID = request.POST.get('Emp_ID', '')
            emp_Email = request.POST.get('Email_ID', '')
            emp_Phone = request.POST.get('phone', '')
            emp_Gender = request.POST.get('gender', '')
            emp_Experience = request.POST.get('experience', '')
            emp_Skill = request.POST.get('skill', '')
            time_Week = request.POST.get('week', '')
            time_Day = request.POST.get('day', '')
            time_Slot = request.POST.get('time', '')
            ins = Employee(emp_first_name=emp_first_name, emp_last_name=emp_last_name, emp_ID=emp_ID,
                           emp_Email=emp_Email, emp_Phone=emp_Phone, emp_Gender=emp_Gender,
                           emp_Experience=emp_Experience, emp_Skill=emp_Skill, time_Week=time_Week, time_Day=time_Day,
                           time_Slot=time_Slot)
            ins.save()
            return render(request, 'interviewer_page.html')


#Page after HR submits candidate information
def submit_candidateinfo(request):
    return render(request, 'submit_candidateinfo.html')


def hr(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        skills = request.POST.get('skills', '')
        experience = request.POST.get('experience', '')
        day = request.POST.get('day', '')
        time = request.POST.get('time', '')
        ins = Candidate(name=name, skills=skills, experience=experience, day=day, time=time)
        ins.save()
        context={'time':time}
        return render(request, 'submit_candidateinfo.html',)
    return render(request, 'hr_candidateinfo.html')

def Logout(request):
    def logout(request):
        auth.logout(request)
        return redirect('/')
