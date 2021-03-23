from django.shortcuts import render ,redirect
from accounts.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
from mainapp.models import *

# Create your views here.
@login_required(login_url='loginpage')
def schedule(request):
    obj = Schedule.objects.all()
    dict1={'obj':obj}
    return render(request,'schedule.html',dict1)


@login_required(login_url='loginpage')
def designation(request):
    obj = Designation.objects.all()
    dict1={'obj':obj}
    return render(request,'designation.html',dict1)



@login_required(login_url='loginpage')
def adddesignation(request):
    designation = request.POST.get("designation")
    obj = Designation(designation=designation)
    obj.save()
    return redirect('designation')


@login_required(login_url='loginpage')
def addschedule(request):
    shift = request.POST.get("shift")
    in_time = request.POST.get("in_time")
    out_time = request.POST.get("out_time")
    obj =Schedule(shift=shift,intime=in_time,outtime=out_time)
    obj.save()
    return redirect('schedule')


@login_required(login_url='loginpage')
def desgdelete(request,id):
    Designation.objects.filter(id=id).delete()
    return redirect('designation')


@login_required(login_url='loginpage')
def desgupdate(request,id):
    obj=Designation.objects.get(id=id)
    dict1={'obj':obj}
    return render(request,'updatedesg.html', dict1)

@login_required(login_url='loginpage')
def updatedesg(request):
    id1 = request.POST.get('id')
    print(id)
    designation=request.POST.get('designation')
    print(designation)
    Designation.objects.filter(id=id1).update(designation=designation)
    return redirect('designation')


@login_required(login_url='loginpage')
def scheduledelete(request,id):
    Schedule.objects.filter(id=id).delete()
    return redirect('schedule')


@login_required(login_url='loginpage')
def scheduleupdate(request,id):
    obj=Schedule.objects.get(id=id)
    hr1=obj.intime.hour
    min1=obj.intime.minute
    sec1=obj.intime.second
    hr2=obj.outtime.hour
    min2=obj.outtime.minute
    sec2=obj.outtime.second
    dict1={'obj':obj,'hr1':hr1,'min1':min1, 'sec1':sec1,'hr2':hr2,'min2':min2,'sec2':sec2}
    return render(request,'updateschedule.html', dict1)

@login_required(login_url='loginpage')
def updateschedule(request):
    id1 = request.POST.get('id')
    print(id)
    intime=request.POST.get('intime')
    intime=request.POST.get('intime')
    Designation.objects.filter(id=id1).update(shift=shift,intime=intime,outtime=outtime)
    return redirect('schedule')
   

