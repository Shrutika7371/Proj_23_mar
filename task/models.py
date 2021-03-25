from django.db import models
from datetime import datetime ,date
from teams.models import *
from mainapp.models import *
from accounts.models import *
from django.utils import timezone

#Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30,default="newassignment", unique=True, primary_key=True)
    task_details =  models.CharField(max_length=30,default="newassignment",null=True, blank=True)
    start_date =models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.assignment_name

class Module(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    module = models.CharField(max_length=100,default='module',null=True, blank=True)

    def __str__(self):
        return self.task


class Project(models.Model):
    proj_name = models.CharField(max_length=200,default='newproj', unique=True , primary_key=True)
    Proj_description =  models.CharField(max_length=500,default="description", null=True, blank=True)
    proj_status = models.CharField(max_length=100,default="pending", null=True, blank=True)
    assigned_to = models.ForeignKey(team, on_delete=models.DO_NOTHING)
    start_date =models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.proj_name
    

    