from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import  HttpResponse
from django.contrib import admin
from django.contrib.auth import  authenticate

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def welcome(request):
    return render(request,'welcome.html')

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
            return render(request, 'hr_page.html')
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
            return render(request, 'interviewer_page.html')
        else:
            messages.error(request,"Enter correct credentials..")
            return render(request, 'Interviewer_Login.html')

    return render(request, 'Interviewer_Login.html')


#After Login navigate to this  pages
def hr_page(request):
    return render(request,'hr_page.html')
def interviewer_page(request):
    return render(request,'interviewer_page.html')



#Interviewer reg- Mayuri's Code added
def interview_details(request):
    return render(request, 'interview_details.html')