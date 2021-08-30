from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.http import  HttpResponse
from django.contrib import admin
from django.contrib.auth.hashers import make_password,check_password
import random
import Interview.models
from .models import Candidate,Interviewer,Human_Resources,slot
from django.core.mail import  send_mail




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

                user = Human_Resources(fname=firstname, lname=lastname,
                                   username=username, email=email, password=password, password2=confirm_password,
                                   gender=gender)
                user.password=make_password(user.password)
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
        #lastname = request.POST['lastname']
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
                user = Interviewer(fname=firstname,
                                                username=username, email=email, password=password,password2=confirm_password,gender=gender)
                user.password = make_password(user.password)
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
        if Human_Resources.objects.all().filter(username=username).exists():
           user = Human_Resources.objects.get(username=username)
           if user:
               flag = check_password(password,user.password)
               if flag:
                     context = {'username': username}
                     return render(request, 'hr_candidateinfo.html', context)
               else:
                 messages.error(request, "Enter correct credentials..")
                 return render(request, 'hr_login.html')

        else:
            messages.error(request, "Enter correct credentials..")
            return render(request, 'hr_login.html')


    return render(request, 'HR_login.html')


#Authentication of Interviewer from DB

def interviewer(request):
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      if Interviewer.objects.all().filter(username=username).exists():
        user1 = Interviewer.objects.get(username=username)
        if user1 :
            flag = check_password(password, user1.password)
            if flag:
                context={'user1':user1}
                return render(request, 'slot.html',context)
            else:
                messages.error(request, "Enter correct credentials..")
                return render(request, 'Interviewer_Login.html')

        else:
            messages.error(request,"Enter correct credentials..")
            return render(request, 'Interviewer_Login.html')

  return render(request, 'Interviewer_Login.html')


#After Login navigate to this  pages








#Page after HR submits candidate information
def submit_candidateinfo(request):
    if request.method == "POST":
        ename = request.POST['empname']
        print(ename)
        can_name = request.POST['canname']
        user = Interviewer.objects.all().filter(fname=ename)
        candidate = Candidate.objects.all().filter(name=can_name)
        for user in user:
            email = user.email
            for candidate in candidate:
                name = candidate.name + str(candidate.time)
                send_mail('Interview Scheduled for the Candidate',
                          name,
                          'schedule.interview2021@gmail.com',
                          [email],
                          fail_silently=False
                          )
                Candidate.objects.all().filter(name=can_name).delete()
            # slot.objects.all().filter(name=ename,from1=candidate.time).delete()
    return render(request, 'submit_candidateinfo.html')


def hr(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        skills = request.POST.get('skills', '')
        experience = request.POST.get('experience', '')
        day = request.POST.get('day', '')
        time = request.POST['time']
        ins = Candidate(name=name, skills=skills, experience=experience, day=day, time=time)
        ins.save()
        employee = slot.objects.all().filter(skills=ins.skills)

        list_interviewers = []
        for emp in employee:
            if ins.day == emp.date:
                if emp.from1 <= float(ins.time) < emp.to:
                    list_interviewers.append(emp.name)
        if len(list_interviewers) == 0:
            context = {'emp': 'No Interviewers are available for this slot. Try another slot.'}
            Candidate.objects.all().filter(name=name).delete()
        else:
            i = random.randint(0, len(list_interviewers)-1)
            selected_interviewers = slot.objects.filter(name=list_interviewers[i], date=ins.day)
            interviewer_select = selected_interviewers[0]
            for selected_interviewer in selected_interviewers:
                if selected_interviewer.from1 == float(ins.time) and selected_interviewer.to == float(ins.time) + 1:
                    rec = slot.objects.filter(name=list_interviewers[i], from1=ins.time, date=ins.day)
                    rec.delete()

                if selected_interviewer.from1 == float(ins.time) and selected_interviewer.to > float(ins.time) + 1:
                    selected_interviewer.from1 = float(ins.time) + 1
                    selected_interviewer.save()
                if selected_interviewer.from1 < float(ins.time) and selected_interviewer.to == float(ins.time) + 1:
                    selected_interviewer.to = float(ins.time)
                    selected_interviewer.save()
                if selected_interviewer.from1 < float(ins.time) and selected_interviewer.to > float(ins.time) + 1:
                    new = slot(name=list_interviewers[i], skills=ins.skills, date=ins.day, day=selected_interviewer.day,
                               from1=float(ins.time) + 1, to=selected_interviewer.to)
                    new.save()
                    selected_interviewer.to = float(ins.time)
                    selected_interviewer.save()
            candidate = Candidate.objects.all().filter(name=name)
            context = {'emp': selected_interviewers[0],
                       'candidate': candidate}

            #context = {'emp': interviewer_select, 'time': str(float(ins.time))+'-'+str(float(ins.time)+1)}
        return render(request, 'submit_candidateinfo.html',context)
    return render(request, 'hr_candidateinfo.html')



def Logout(request):
    auth.logout(request)
    return redirect('/')

def time(request):
    if request.method=='POST':
        name=request.POST['name']
        skills=request.POST['skills']
        date= request.POST['date1']
        day= request.POST['day']
        from1=request.POST['from']
        to=request.POST['to']
        slot=Interview.models.slot(name=name,skills=skills,date=date,day=day,from1=from1,to=to)
        slot.save()
        user1=Interviewer.objects.all().filter(fname=name)
        context = {'username': user1}
        messages.info(request,"Slot Saved")
    return render(request, 'slot.html',context)
