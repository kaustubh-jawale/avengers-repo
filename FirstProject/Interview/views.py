from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def welcome(request):
    return render(request, 'welcome.html')


def hr_login(request):
    return render(request, 'HR_login.html')


def interviewer(request):
    return render(request, 'Interviewer_Login.html')


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
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
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
