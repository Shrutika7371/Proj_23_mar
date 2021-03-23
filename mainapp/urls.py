from django.urls import path,include
from . import views
urlpatterns = [
    path('schedule', views.schedule , name='schedule'),
    path('designation', views.designation , name='designation'),
    path('adddesignation', views.adddesignation , name='adddesignation'),
    path('addschedule', views.addschedule , name='addschedule'),
    path('desgupdate/<int:id>', views.desgupdate, name='desgupdate'),
    path('desgdelete/<int:id>', views.desgdelete, name='desgdelete'),
    path('updatedesg', views.updatedesg, name='updatedesg'),
    path('scheduleupdate/<int:id>', views.scheduleupdate, name='scheduleupdate'),
    path('scheduledelete/<int:id>', views.scheduledelete, name='scheduledelete'),
    path('updateschedule', views.updateschedule, name='updateschedule'),

]