from django.urls import path,include
from . import views

urlpatterns = [
   path('addproject', views.addproject, name='addproject'),
   path('project', views.project, name='project'),
   path('projectupdate/<str:pk>/', views.projectupdate, name='projectupdate'),
   path('projectdelete/<str:pk>/', views.projectdelete, name='projectdelete'),
   path('updateproj', views.updateproj , name='updateproj'),

]