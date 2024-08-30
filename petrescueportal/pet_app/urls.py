"""
URL configuration for petrescueportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path




urlpatterns = [
   # path('admin/', admin.site.urls),
    path('home/', views.home, name='home'), 
    path('userregister/', views.userregister, name='userregister'),
     path('rescueregister/', views.rescueregister, name='rescueregister'),
     path('login/', views.loginn, name='loginn'),
     path('userlogin/', views.userlogin, name='userlogin'),
      path('rescuerlogin/', views.rescuerlogin, name='rescuerlogin'),
      path('reslogin/', views.reslogin, name='reslogin'),
      path('logout/', views.logout, name='logout'),
      path('addpets/', views.addpets, name='addpets'),
      
    path('petadoption/', views.petadoption, name='petadoption'),
    path('pet_list/', views.pet_list, name='pet_list'),
    path('doc_list/', views.doc_list, name='doc_list'),
     path('doclogin/', views.doclogin, name='doclogin'),
     path('doclist/', views.doclist, name='doclist'),
    path('doc_list/<str:doc>/', views.doc_list, name='doc_list'),
    path('doc_list/<str:doc>/', views.DoctorRegistrationForm, name='doctorreg'),
    path('med_assist/', views.med_assist, name='med_assist'),
    path('adopt/', views.adopt, name='adopt'),
    path('doctorreg/', views.doctorreg, name='doctorreg'),
    path('groomreg/', views.groomreg, name='groomreg'),
    
    
     
  # Add this line for the root URL
    #path('action_save_user/', views.action_save_user, name='action_save_user'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

