from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import datetime ,date
from django.core.validators import MaxValueValidator


# Create your models here.
class Designation(models.Model):
    designation = models.CharField(max_length=50,unique=True,default="employee",null=True, blank=True)

    def __str__(self):
        return self.designation


class Schedule(models.Model):
    intime = models.TimeField(auto_now=False, auto_now_add=False)
    outtime = models.TimeField(auto_now=False,auto_now_add=False)
    shift=models.CharField(max_length=20, default='dummy object')
    
    def __str__(self):
        return self.shift