from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('taxes', views.viewTaxes, name='taxes'),
    path('users', views.viewUsers, name='users'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('request',views.request, name='form')
    
]