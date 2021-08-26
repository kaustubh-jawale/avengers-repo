from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.http import  HttpResponse
from django.contrib import admin
from django.contrib.auth import  authenticate
from .models import Candidate,Employee,Interviewer,Human_Resources
from cryptography.fernet import Fernet

def encrypt(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    ecrypt_password = fernet.encrypt(password.encode())
    return ecrypt_password


def decrypt(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    decrypt_password = fernet.decrypt(password).decode()
    return decrypt_password

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def welcome(request):
    return render(request, 'welcome.html')

def register_both(request):
    return render(request, 'register_both.html')
#HR Register
def hr_register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        gender = request.POST['gender']
        # check if password and confirm password both are same
        if password == confirm_password:
            # check whether same username is there any database
            if Human_Resources.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return render(request, 'registration.html')
            else:
                # if not same username, register the user
                password = encrypt(password)
                user = Human_Resources(fname=firstname, lname=lastname,
                                   username=username, email=email, password=password,
                                   gender=gender)

                user.save()
                return redirect('/')
        else:
            # printing message if password doesnt match
            messages.info(request, 'Password not matched')
            return render(request, 'registration.html')
        return render(request, 'registration.html')

        # if the request from registration.html is GET, then transfer it to registration.html
    else:
        return render(request, 'registration.html')






#Registration Code here
def interviewer_register(request):
    # if request from registration.html is POST, get all details in variables
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        gender=request.POST['gender']
        # check if password and confirm password both are same
        if password == confirm_password:
            # check whether same username is there any database
            if Interviewer.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('interviewer_register')
            else:
                # if not same username, register the user
                user = Interviewer(fname=firstname, lname=lastname,
                                                username=username, email=email, password=password,password2=confirm_password,gender=gender)

                user.save()
                return redirect('/')
        else:
            # printing message if password doesnt match
            messages.info(request, 'Password not matched')
            return redirect('interviewer_register')
        return redirect('interviewer_register')

    # if the request from registration.html is GET, then transfer it to registration.html
    else:
        return render(request, 'interviewer_register.html')





#Aunthentication of HR from DB
def hr_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = Human_Resources.objects.all().filter(username=username)
        password_dec = decrypt(user.password)
        if password == password_dec:
            #if Human_Resources.objects.all().filter(username=username,password=password).exists():
                context = {'username': username}
                return render(request, 'hr_candidateinfo.html',context)
        else:
            messages.error(request, "Enter correct credentials..")
            return render(request, 'hr_login.html')
          
    return render(request, 'HR_login.html')







#Authentication of Interviewer from DB

def interviewer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Interviewer.objects.all().filter(username=username,password=password).exists():
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
    if request.method == "POST":
        name = request.POST.get('name', '')
        skills = request.POST.get('skills', '')

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
        employee = Employee.objects.all().filter(emp_Skill=skills)
        context = {'emp': employee}
        return render(request, 'submit_candidateinfo.html',context)
    return render(request, 'hr_candidateinfo.html')



def Logout(request):
    def logout(request):
        auth.logout(request)
        return redirect('/')
