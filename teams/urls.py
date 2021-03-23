from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.teams , name='teams'),
    path('addteam', views.addteam, name='addteam'),
    path('addmember', views.addmember, name='addmember'),
    path('deletemember/<int:pk>', views.deletemember, name='deletemember'),
    path('teamdelete/<str:teamname>', views.teamdelete, name='teamdelete'),
    path('teamdetails/<str:teamname>', views.teamdetails, name='teamdetails'),
]