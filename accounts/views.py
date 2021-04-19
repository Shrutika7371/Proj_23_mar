from django.shortcuts import render ,redirect
from accounts.models import *
from mainapp.models import *
from task.models import *
from teams.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
from mainapp.models import *


def loginpage(request):
    return render(request, "login.html")

def dologin(request):
    email=request.POST.get('email')
    passw=request.POST.get('password')
    print(email)
    print(passw)
    user = authenticate(request, email=email, password=passw)
    print(user is not None)
    if user is not None:
        login(request, user)
        flag = redirect('index')

    else:
        flag=redirect('loginpage')
    return flag

    
@login_required(login_url='loginpage')
def logout_view(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def change_password(request):
    return render(request,'changepassword.html')


@login_required(login_url='loginpage')
def pass_change(request):
    newpass = request. POST.get('newpass')
    confpass = request.POST.get('confpass')
    email= request.user.email
    obj = CustomUser.objects.get(email=email)
    print( request.user.password)
    print(newpass)
    if(newpass == confpass):
        obj.set_password(newpass)
        obj.save()
    return redirect('index')




@login_required(login_url='loginpage')
def index(request):
    email = request.user.email
    obj = team.objects.all()
    if request.user.position!='admin':
        a=CustomUser.objects.get(email=email)
        b=member.objects.get(member_email=a).team_name
        obj1=Project.objects.filter(assigned_to=b)
        print(obj1)
        obj2=Project.objects.filter(assigned_to=b)
        dict1 = {'obj':obj,'obj1':obj1,'obj2':obj2}
    else:
        obj3 = Project.objects.all()
        a = Project.objects.filter(proj_status=100).count()
        b = Project.objects.filter(proj_status=0).count()
        c = obj3.count()-a-b
        dict1 = {'obj':obj,'obj3':obj3,'a':a,'b':b,'c':c}
    return render(request , "index.html",dict1)
    
@login_required(login_url='loginpage')
def profile(request):
    email=request.user.email
    obj=CustomUser.objects.get(email=email)
    dict1={'obj':obj}
    return render(request,"profile.html",dict1)

@login_required(login_url='loginpage')
def employeetrans(request):
    obj1 =  Designation.objects.all()
    obj2 = Schedule.objects.all()
    dict1={'obj1':obj1,'obj2':obj2}
    return render(request, 'employee-trans.html',dict1)

@login_required(login_url='loginpage')
def adduser(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    contact = request.POST.get('contact')
    designation = request.POST.get('designation')
    contact = request.POST.get('contact')
    rateperday = request.POST.get('rateperday')
    alloted_leave = request.POST.get('alloted_leave')
    schedule = request.POST.get('schedule')
    
    new_user = CustomUser.objects.create(first_name=fname,last_name=lname,email=email,birth_date=dob,gender=gender,designation=designation,contact=contact,Rate_per_day=rateperday,alloted_leave=alloted_leave,schedule=schedule)
    new_user.set_password(password)
    new_user.save()
    return render(request, 'index.html' , {'alert':'registered succesfully'})

@login_required(login_url='loginpage')
def employees(request):
    obj = CustomUser.objects.all()
    dict1={'obj':obj }
    return render(request,'employees.html',dict1) 



@login_required(login_url='loginpage')
def empdelete(request,email):
    CustomUser.objects.filter(email=email).delete()
    return redirect('employees')
    

@login_required(login_url='loginpage')
def empupdate(request,email):
    obj = CustomUser.objects.get(email=email)
    print(obj.gender)
    obj1 = Designation.objects.all()
    obj2 = Schedule.objects.all()
    dict1 = {'i':obj,'obj1':obj1,'obj2':obj2 } 
    return render(request,'empupdate.html',dict1)

def updateemp(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    contact = request.POST.get('contact')
    designation = request.POST.get('designation')
    contact = request.POST.get('contact')
    rateperday = request.POST.get('rateperday')
    alloted_leave = request.POST.get('alloted_leave')
    schedule = request.POST.get('schedule')
    upd_user = CustomUser.objects.filter(email=email).update(first_name=fname,last_name=lname,birth_date=dob,gender=gender,designation=designation,contact=contact,Rate_per_day=rateperday,alloted_leave=alloted_leave,schedule=schedule) 
    return redirect('index')