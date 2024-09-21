from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('userregister/', views.userregister, name='userregister'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('user_petadoption/', views.user_petadoption, name='user_petadoption'),
    path('user_doclist/', views.user_doclist, name='user_doclist'),
    path('user_groomlist/', views.user_groomlist, name='user_groomlist'),

    path('rescueregister/', views.rescueregister, name='rescueregister'),
    path('rescuerlogin/', views.rescuerlogin, name='rescuerlogin'),
    path('rescuerdashboard/', views.rescuerdashboard, name='rescuerdashboard'),
    path('rescuer_addpets/', views.rescuer_addpets, name='rescuer_addpets'),
    path('rescuer_petlist/', views.rescuer_petlist, name='rescuer_petlist'),

    path('doctorreg/', views.doctorreg, name='doctorreg'),
    path('shelterreg/', views.shelterreg, name='shelterreg'),
    path('groomreg/', views.groomreg, name='groomreg'),
]