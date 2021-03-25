from django.shortcuts import render,redirect
from accounts.models import *
from mainapp.models import *
from task.models import *
from .models import *
from task.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url='loginpage')
def teams(request):
    obj = team.objects.all()
    dict1={'obj':obj}
    return render(request,'teams.html',dict1)


def addteam(request):
    team_name=request.POST.get('teamname')
    team_description=request.POST.get('desc')
    obj = team(team_name=team_name, team_description=team_description)
    obj.save()
    return redirect('teams')

def teamdelete(request,teamname):
    team.objects.filter(team_name=teamname).delete()
    return redirect('teams')

def teamdetails(request,teamname):
    obj=team.objects.get(team_name = teamname)
    obj2=member.objects.filter(team_name = teamname)
    obj3=CustomUser.objects.filter(position="employee")

    dict1={'obj':obj, 'obj1':obj1, 'obj2':obj2,'obj3':obj3}
    # dict1={'obj':obj}
    return render(request,'teamdetails.html',dict1)


def addmember(request):
    teamname=request.POST.get('teamname')
    email = request.POST.get('email')
    position = request.POST.get('position')
    CustomUser.objects.filter(email=email).update(position=position)
    obj1 = CustomUser.objects.get(email=email)
    name = obj1.first_name+obj1.last_name
    print(obj1.position)
    obj2 = team.objects.get(team_name=teamname)
    obj=member(member_email=obj1 , team_name=obj2, member_name=name, member_position=position)
    obj.save()
    return redirect('teamdetails',teamname)


def deletemember(request,pk):
    obj = member.objects.get(id=pk)
    print(obj.member_email)
    email=obj.member_email
    teamname=obj.team_name
    CustomUser.objects.filter(email=email).update(position="employee")
    obj.delete()
    return redirect('teamdetails',teamname)