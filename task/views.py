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
