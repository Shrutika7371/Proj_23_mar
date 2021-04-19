from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.loginpage , name='loginpage'),
    path('logout_view', views.logout_view , name='logout_view'),
    path('change_password', views.change_password, name='change_password'),
    path('pass_change', views.pass_change, name='pass_change'),
    path('profile', views.profile , name='profile'),
    path('dologin', views.dologin , name='dologin'),
    path('index', views.index , name='index'),
    path('employee-trans', views.employeetrans, name='employee-trans'),
    path('adduser', views.adduser, name='adduser'),
    path('employees', views.employees, name='employees'),
    path('empupdate/<str:email>', views.empupdate, name='empupdate'),
    path('empdelete/<str:email>', views.employees, name='empdelete'),
    path('updateemp', views.updateemp, name='updateemp'),

]