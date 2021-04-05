from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import datetime ,date
from django.core.validators import MaxValueValidator
from django.utils import timezone
from datetime import datetime ,date
from teams.models import *
from mainapp.models import *
from accounts.models import *
# Create your models here.
class Leave(models.Model):
    leave_req_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    leave_reason = models.CharField(max_length=30, default="personal reason",null=True, blank=True)
    start_date =models.DateTimeField(default=timezone.now,null=True, blank=True,auto_now=False)
    end_date = models.DateTimeField(default=timezone.now,null=True, blank=True)
    no_of_days = models.IntegerField(default=0)
    team_name = models.CharField(max_length=30, default="none",null=True,blank=True)
    Leave_Status = models.CharField(max_length=10, default = "pending")

    def __str__(self):
        return self.leave_reason
    
