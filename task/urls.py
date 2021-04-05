from django.urls import path,include
from . import views

urlpatterns = [
   path('addproject', views.addproject, name='addproject'),
   path('project', views.project, name='project'),
   path('projectupdate/<str:pk>/', views.projectupdate, name='projectupdate'),
   path('projectdelete/<str:pk>/', views.projectdelete, name='projectdelete'),
   path('updateproj', views.updateproj , name='updateproj'),
   path('task', views.task , name='task'),
   path('addtask', views.addtask , name='addtask'),
   path('taskupdate/<str:pk>/', views.taskupdate, name='taskupdate'),
   path('taskdelete/<str:pk>/', views.taskdelete, name='taskdelete'),
   path('taskassigned', views.taskassigned,  name = 'taskassigned'),

]