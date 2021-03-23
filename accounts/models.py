from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import datetime ,date
from django.core.validators import MaxValueValidator
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True , primary_key=True )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    birth_date=models.DateTimeField(default=timezone.now)
    contact = models.IntegerField(validators=[MaxValueValidator(9999999999)], unique=False,default=0000000000,null=True, blank=True)
    gender = models.CharField(max_length=20,default='Male',null=True, blank=True)
    designation = models.CharField(max_length=20 , default = 'employee',null=True, blank=True)
    position = models.CharField(max_length=20 , default = 'employee',null=True, blank=True)
    Rate_per_day = models.IntegerField(default=500,null=True, blank=True)
    alloted_leave= models.IntegerField(default=10,null=True, blank=True)
    schedule = models.CharField(max_length=50,default = "10-6",null=True,blank=True)
    
    objects = CustomUserManager()


    def __str__(self):

        return self.email





        
