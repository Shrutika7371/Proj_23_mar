from django.urls import path,include
from . import views

urlpatterns = [
   # path('accounts', include('accounts.urls')),
   path('newproject', views.newproject, name='newproject'),
   path('addproject', views.addproject, name='addproject')

]