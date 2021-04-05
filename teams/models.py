from django.db import models
from accounts.models import *
from mainapp.models import *
from task.models import *
from datetime import datetime ,date
from django.utils import timezone

# Create your models here.
class team(models.Model):
    team_name = models.CharField(max_length=100,primary_key=True,unique=True)
    team_description =  models.CharField(max_length=500,default='desc',null=True,blank=True)
    date_start = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='free')

    def __str__(self):
        return self.team_name



class member(models.Model):
    member_email = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING)
    member_name = models.CharField(max_length=100,default='new member',null=True,blank=True)
    team_name = models.ForeignKey(team , on_delete=models.DO_NOTHING)
    member_position = models.CharField(max_length=100,default="teammember",null=True,blank=True)
    joining_date = models.DateTimeField(default=timezone.now)
    member_status = models.CharField(max_length=50,default="free", null=True, blank=True)

    def __str__(self):
        return self.member_email
        
    


