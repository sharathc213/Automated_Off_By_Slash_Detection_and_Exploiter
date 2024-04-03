from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.signin,name='signin'),
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('Dashboard/<str:page>/',views.Dashboard,name='Dashboard'),
    path('scan',views.scan,name='scan'),
    path('CheckScanStatus',views.CheckScanStatus,name='CheckScanStatus'),
    path('get_file_list', views.get_file_list, name='get_file_list'),
    path('signout', views.signout, name='signout'),
]