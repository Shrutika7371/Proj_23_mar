from django.shortcuts import render
from django.shortcuts import render,redirect
from accounts.models import *
from mainapp.models import *
from task.models import *
from .models import *
from task.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def newproject(request):
    obj = team.objects.all()
    dict1={'obj':obj}
    return render(request,'newproject.html',dict1)

def addproject(request):
    proj_name = request.POST.get('proj_name')
    proj_description = request.POST.get('proj_description')
    team_name = request.POST.get('team_name')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')
    obj = team.objects.get(team_name=team_name)
    obj1 = Project(proj_name=proj_name, Proj_description=proj_description, assigned_to=obj, start_date=startdate, end_date=enddate) 
    obj1.save()
    return redirect('teams')