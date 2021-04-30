from django.shortcuts import render,redirect
from accounts.models import *
from mainapp.models import *
from task.models import *
from .models import *
from task.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    obj1= team.objects.get(team_name=teamname).status
    if obj1=='busy':
        return redirect('teams')
    else: 
        obj = member.objects.filter(team_name=teamname)
        print(obj)
        for i in obj:
            CustomUser.objects.filter(email=i.member_email).update(position="employee")
        member.objects.filter(team_name=teamname).delete()
        team.objects.get(team_name=teamname).delete()
        return redirect("teams")

    
def teamdetails(request,teamname):      
    obj=team.objects.get(team_name = teamname)
    obj1=Project.objects.filter(assigned_to = obj.team_name)
    print(obj1)
    obj2=member.objects.filter(team_name = teamname)
    obj3=CustomUser.objects.filter(position = "employee")
    if obj1 is not None:
        dict1={'obj':obj, 'obj1':obj1, 'obj2':obj2,'obj3':obj3}
    else:
        dict1={'obj':obj, 'obj1':obj1, 'obj2':obj2,'obj3':obj3}
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
    if obj.member_status=="busy":
        messages.error(request,'your project registered succussfully!!')
    else:
        CustomUser.objects.filter(email=obj.member_email).update(position="employee")
        member.objects.get(id=pk).delete()
    return redirect('teamdetails',obj.team_name)



def updatemember(request,pk):
    obj4 = member.objects.get(id=pk)
    teamname = obj4.team_name
    print(teamname)
    obj=team.objects.get(team_name = teamname)
    obj1=Project.objects.filter(assigned_to = obj.team_name)
    obj2=member.objects.filter(team_name = teamname)
    obj3=CustomUser.objects.filter(position = "employee")
    if obj1 is not None:
        dict1={'obj':obj, 'obj1':obj1, 'obj2':obj2,'obj3':obj3}
    else:
        dict1={'obj':obj, 'obj1':obj1, 'obj2':obj2,'obj3':obj3}
    dict1['obj4'] = obj4
    return render(request,"updatemember.html",dict1)

def leaderteam(request):
    email = request.user.email
    obj = member.objects.get(member_email=email).team_name
    return redirect("teamdetails",obj)


def memberupdate(request):
    id1 = request.POST.get('id')
    position = request.POST.get('position')
    member.objects.filter(id=id1).update(member_position=position)
    email = member.objects.get(id=id1).member_email
    CustomUser.objects.filter(email=email).update(position=position)
    obj = member.objects.get(id=id1).team_name
    return redirect('teamdetails',obj)



def teammember(request):
    email = request.user.email
    teamname = member.objects.get(member_email=email).team_name
    obj =  member.objects.filter(team_name=teamname)
    obj1 = Project.objects.filter(assigned_to = teamname)
    obj2 = team.objects.get(team_name=teamname)
    dict1={'obj':obj, 'obj1':obj1,'obj2':obj2}
    return render(request,'teammember.html',dict1)