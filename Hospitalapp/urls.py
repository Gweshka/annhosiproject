
from django.contrib import admin
from django.urls import path
from Hospitalapp import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appoint, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('delete/<int:id>', views.delete),
    path('deletecontact/<int:id>', views.deletecontact),
    path('edit/<int:id>', views.edit,name='edit'),
    path('', views.register, name='register'),
    path('login/', views.login,name='login')
]
