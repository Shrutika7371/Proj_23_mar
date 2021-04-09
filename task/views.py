from django.shortcuts import render
from django.shortcuts import render,redirect
from accounts.models import *
from mainapp.models import *
from task.models import *
from .models import *
from task.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def addproject(request):
    proj_name = request.POST.get('proj_name')
    proj_description = request.POST.get('proj_description')
    team_name = request.POST.get('team_name')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    obj = team.objects.get(team_name=team_name)
    obj1 = Project(proj_name=proj_name, Proj_description=proj_description, assigned_to=obj, start_date=startdate, end_date=enddate) 
    obj2=obj1.save()
    team.objects.filter(team_name=team_name).update(status='busy')
    messages.success(request,'your project registered succussfully!!')
    return redirect('project')
    


def project(request):
    obj=Project.objects.all()
    obj1 = team.objects.filter(status="free")
    dict1 = {'obj':obj, 'obj1':obj1}
    return render(request, "project.html", dict1)


def projectdelete(request,pk):
    print(pk)
    obj = Project.objects.get(proj_name=pk).assigned_to
    print(obj)  
    team.objects.filter(team_name=obj).update(status="free")
    Project.objects.get(proj_name=pk).delete()
    return redirect("project")



def projectupdate(request,pk):
    obj=Project.objects.all()
    obj1 = Project.objects.filter(proj_name=pk).all() 
    obj2 = team.objects.filter(status="free")
    dict1={'obj':obj, 'obj1':obj1, 'obj2':obj2}
    return render(request, "projectupdate.html", dict1)


def updateproj(request):
    proj_name = request.POST.get('proj_name')
    proj_description = request.POST.get('proj_description')
    team_name = request.POST.get('team_name')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    obj = team.objects.get(team_name=team_name)
    Project.objects.filter(proj_name=proj_name).update( Proj_description=proj_description, assigned_to=obj, start_date=startdate, end_date=enddate) 
    return redirect('project')



def task(request):
    email = request.user.email
    print(email)
    teamname = member.objects.get(member_email=email).team_name
    print(teamname)
    obj = member.objects.filter(team_name=teamname , member_status="free")
    obj1 = Taskdata.objects.all()
    print(obj)
    dict1={'obj':obj, 'obj1':obj1}
    return render(request,'task.html',dict1)


def addtask(request):
    taskname = request.POST.get('task')
    print(taskname)
    task_details = request.POST.get('task_details')
    member_name = request.POST.get('member_name')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    obj = member.objects.get(member_name=member_name)
    member.objects.filter(member_name=member_name).update(member_status = "busy")
    print(5)
    obj1 = Taskdata(task_name = taskname, task_details=task_details, assign_member =obj, start_date=startdate, end_date=enddate)
    obj1.save()
    if obj1:
        print('saved')
    return redirect("task")


def taskupdate(request,pk):
    email = request.user.email
    print(email)
    teamname = member.objects.get(member_email=email).team_name
    print(teamname)
    obj = member.objects.filter(team_name=teamname , member_status="free")
    obj1 = Taskdata.objects.all()
    obj2 = Taskdata.objects.filter(task_name=pk)
    for i in obj2:
        print(i)
        print(i.task_details)
    dict1={'obj':obj, 'obj1':obj1,'obj2':obj2}
    return render(request,'taskupdate.html',dict1)

 

def taskdelete(request,pk):
    obj = Taskdata.objects.get(task_name=pk)
    obj1 = obj.assign_member
    member.objects.filter(member_name=obj1).update(member_status="free")
    obj.delete()
    return redirect("task")


def taskassigned(request):
    email = request.user.email
    mem = member.objects.get(member_email=email)
    obj = Taskdata.objects.filter(assign_member=mem)
    print(obj)
    dict1 = {'obj':obj}
    return render(request,'taskassigned.html',dict1)