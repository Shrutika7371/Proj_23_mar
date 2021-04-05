from django.urls import path,include
from . import views
urlpatterns = [
    path('leavemember', views.leavemember , name='leavemember'),
    path('applyleave', views.applyleave , name='applyleave'),
    path('leaveleader', views.leaveleader , name='leaveleader'),
    path('leaveadmin', views.leaveadmin, name='leaveadmin'),
    path('approveleave/<int:pk>', views.approveleave,  name ='approveleave'),
    path('rejectleave/<int:pk>', views.rejectleave,  name ='rejectleave'),

]