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
    path('user_chat/<int:user_id>/', views.user_chat, name='user_chat'),
    path('user_chatgroomer/<int:user_id>/', views.user_chatgroomer, name='user_chatgroomer'),
    path('rescueregister/', views.rescueregister, name='rescueregister'),
    path('rescuerlogin/', views.rescuerlogin, name='rescuerlogin'),
    path('rescuerdashboard/', views.rescuerdashboard, name='rescuerdashboard'),
    path('rescuer_addpets/', views.rescuer_addpets, name='rescuer_addpets'),
    path('rescuer_petlist/', views.rescuer_petlist, name='rescuer_petlist'),

    path('doctorreg/', views.doctorreg, name='doctorreg'),
    path('doctorlogin/', views.doctorlogin, name='doctorlogin'),
    path('doc_userchatlist/', views.doc_userchatlist, name='doc_userchatlist'),
    path('doctordashboard/', views.doctordashboard, name='doctordashboard'),
    path('doctor_chat/<int:user_id>/', views.doctor_chat, name='doctor_chat'),

    path('shelterreg/', views.shelterreg, name='shelterreg'),

     path('groomlogin/', views.groomlogin, name='groomlogin'),
    path('groomreg/', views.groomreg, name='groomreg'),
    path('groomdashboard/', views.groomdashboard, name='groomdashboard'),
    path('groom_userchatlist/', views.groom_userchatlist, name='groom_userchatlist'),
    path('groomer_chat/<int:user_id>/', views.groomer_chat, name='groomer_chat'),

    path('proceedtopay/<int:pet_id>/', views.proceedtopay, name='proceedtopay'),
    path('payment/<int:pet_id>/', views.payment, name='payment'),
    path('paymentsuccess', views.paymentsuccess, name='paymentsuccess'),
    path('user_donation', views.user_donation, name='user_donation'),

    path('search_pets', views.search_pets, name='search_pets'),
    path('donation', views.donation, name='donation'),




]