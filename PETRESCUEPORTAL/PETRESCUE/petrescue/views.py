from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import AdminLoginForm
from .forms import CustomUserRegistrationForm
from .forms import RescuerRegistrationForm
from .forms import RescuerLoginForm
from .forms import RescuerAddpetsForm
from .forms import DoctorRegistrationForm
from .forms import ShelterRegistrationForm
from .forms import groomRegistrationForm
from .forms import CustomLoginForm
from .models import Pet
from .models import doctor
from .models import Groomers

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# admin panel

def adminlogin(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username == "admin" and password == "admin@123":
                return redirect('admindashboard') 
    else:
        form = AdminLoginForm()
    return render(request, 'adminlogin.html', {'form': form})

def admindashboard(request):
    return render(request,'admindashboard.html')

# user portal

def userregister(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a different view after registration
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'userregister.html', {'form': form})


def userlogin(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userdashboard')  # Redirect to a home page after successful login
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = CustomLoginForm()
    return render(request, 'userlogin.html', {'form': form})

def userlogout(request):
    logout(request)
    return redirect('home')

def userdashboard(request):
    return render(request,'userdashboard.html')


def user_petadoption(request):
    pets = Pet.objects.all()
    return render(request, 'user_petadoption.html',{'pets': pets})


def user_doclist(request):
    doctors = doctor.objects.all()
    return render(request, 'user_doclist.html', {'doctors': doctors})


def user_groomlist(request):
    groomers = Groomers.objects.all() 
    print(groomers)
    return render(request, 'user_groomlist.html', {'groomers': groomers})


# Rescuer portal

def rescueregister(request):
    if request.method == 'POST':
        form = RescuerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('rescuerlogin')  # Redirect to a different view after registration
    else:
        form = RescuerRegistrationForm()

    return render(request, 'rescuregister.html', {'form': form})




def rescuerlogin(request):
    if request.method == 'POST':
        form = RescuerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('rescuerdashboard.html')  # Redirect to the dashboard or desired page
            else:
                return render(request, 'rescuerlogin.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = RescuerLoginForm()

    return render(request, 'rescuerlogin.html', {'form': form})



def rescuerdashboard(request):
    return render(request,'rescuerdashboard.html')



def rescuer_addpets(request):
    if request.method == 'POST':
        form = RescuerAddpetsForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('rescuerdashboard')  # Redirect to a different view after registration
    else:
        form = RescuerAddpetsForm()

    return render(request, 'rescuer_addpets.html', {'form': form})



def rescuer_petlist(request):
    pets = Pet.objects.all()  # Fetch all pets from the database
    return render(request, 'rescuer_petlist.html', {'pets': pets})



# Register Doctor, Shelter, Groom


def doctorreg(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('home')  # Redirect to a different view after registration
    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctorreg.html', {'form': form})



def shelterreg(request):
    if request.method == 'POST':
        form = ShelterRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('home')  # Redirect to a different view after registration
    else:
        form = ShelterRegistrationForm()

    return render(request, 'shelterreg.html', {'form': form})


def groomreg(request):
    if request.method == 'POST':
        form = groomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('home')  # Redirect to a different view after registration
    else:
        form = groomRegistrationForm()

    return render(request, 'groomreg.html', {'form': form})