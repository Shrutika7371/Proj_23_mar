from django.shortcuts import render ,redirect
from accounts.models import *
from mainapp.models import *
from task.models import *
from teams.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
from mainapp.models import *
from .models import *
from django.contrib import messages
# Create your views here.


def leavemember(request):
    obj = member.objects.get(member_email=request.user.email)
    a = CustomUser.objects.get(email=request.user.email)
    obj1 = Leave.objects.filter(user=a)
    dict1= {'obj':obj,'obj1':obj1} 
    return render(request,"leavemember.html", dict1)



def applyleave(request):
    if request.user.alloted_leave !=0 :
        leave= request.POST.get('leave_reason')
        team_name = request.POST.get('teamname')
        email = request.POST.get('email')
        start_date = request.POST.get('from')
        end_date = request.POST.get('to')
        no_of_days = request.POST.get('no_of_days')
        obj = CustomUser.objects.get(email=email)
        position = obj.position
        obj1 =Leave(leave_reason = leave,user=obj, start_date=start_date, team_name=team_name , end_date=end_date,no_of_days=no_of_days)
        obj1.save()
        messages.success(request,'your project registered succussfully!!')


    else:
        messages.error(request,'your alloted leaves are completed')
    
    return redirect('leavemember')
        


def leaveleader(request):
    obj = member.objects.get(member_email=request.user.email)
    a = CustomUser.objects.get(email=request.user.email)
    obj1 = Leave.objects.filter(user=a)
    dict1= {'obj':obj,'obj1':obj1}
    return render(request,"leaveleader.html",dict1)




def leaveadmin(request):
    obj = Leave.objects.filter(Leave_Status="pending")
    dict1={'obj':obj}
    return render(request,"leaveadmin.html",dict1)



def approveleave(request,pk):
    obj = Leave.objects.get(leave_req_id=pk).user
    x=obj.alloted_leave
    obj1 = Leave.objects.get(leave_req_id=pk)
    y=obj1.no_of_days
    CustomUser.objects.filter(email=obj.email).update(alloted_leave=x-y)
    Leave.objects.filter(leave_req_id=pk).update(Leave_Status= "approved")
    return redirect(leaveadmin)


def rejectleave(request,pk):
    Leave.objects.filter(leave_req_id=pk).update(Leave_Status= "rejected")
    return redirect(leaveadmin)