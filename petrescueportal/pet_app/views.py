from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def rescueregister(request):
    return render(request,'rescueregister.html')
def loginn(request):
    return render(request,'login.html')
def userlogin(request):
    return render(request,'userlogin.html')
def userlogin(request):
    return render(request, 'userlogin.html')
def rescuerlogin(request):
    return render(request, 'rescuerlogin.html')
def reslogin(request):
    return render(request, 'reslogin.html')
def logout(request):
    return render(request, 'home.html')
def addpets(request):
    return render(request, 'addpets.html')

def pet_list(request):
    return render(request, 'pet_list.html')
def doctorreg(request):
    return render(request, 'doctorreg.html')
def groomreg(request):
    return render(request, 'groomreg.html')
def doclogin(request):
    return render(request, 'doclogin.html')
def petadoption(request):
    return render(request, 'petadoption.html')
def doclist(request):
    return render(request, 'doclist.html')
def adopt(request):
    return render(request, 'adopt.html')
def med_assist(request):
    return render(request, 'med_assist.html')
from django.shortcuts import render
from .models import Pet



from django.shortcuts import render, redirect




# pet_app/views.py
from django.shortcuts import render
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html')
def doclist(request):
    doctors = doctor.objects.all()
    return render(request, 'doclist.html', {'doctors': doctors})

def petadoption(request):
    pets = Pet.objects.all()
    return render(request, 'petadoption.html',{'pets': pets})




def userregister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save(commit=False)
            # Hash the password before saving it (optional)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Redirect to a success page or the login page
            return redirect('/login')
        else:
            # Show the form with errors
            return render(request, 'userregister.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'userregister.html', {'form': form})
from django.contrib.auth import authenticate, login

def user_portal(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('userportal')  # Redirect to userlogin.html
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')
    
    # views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RescuerLoginForm
# views.py
from .forms import RescuerLoginForm


def rescuerlogin(request):
    if request.method == 'POST':
        form = RescuerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('rescuer_dashboard')  # Redirect to the dashboard or desired page
            else:
                return render(request, 'rescuerlogin.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = RescuerLoginForm()

    return render(request, 'rescuerlogin.html', {'form': form})

# pet_app/views.py
from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet


# pet_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PetForm
from .models import Pet



# pet_app/views.py
from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet

#def addpets(request):
   # if request.method == 'POST':
       # breed=request.POST['breed']
       ## colour=request.POST['colour']
       # age=request.POST['age']
        #identification=request.POST['identification']
        #location=request.POST['location']
        #print(breed)
        #form = PetForm(request.POST)
        #if form.is_valid():
         #   form.save()  # Save the new pet details to the database
          #  return redirect('pet_list')  # Redirect to the pet list page or another page
    #else:
     #   form = PetForm()

    #return render(request, 'addpets.html', {'form': form})
from django.shortcuts import render
from .models import Pet

def addpets(request):
    if request.method == 'POST':
        breed = request.POST['breed']
        colour = request.POST['colour']
        age = request.POST['age']
        identification = request.POST['identification']
        location = request.POST['location']

        # Save to the database
        pet = Pet(breed=breed, colour=colour, age=age, identification=identification, location=location)
        pet.save()

        # Optionally, you can add a success message or redirect to another page
        # For now, the user will stay on the same page after submitting

    return render(request, 'addpets.html')

from django.shortcuts import render
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()  # Fetch all pets from the database
    return render(request, 'pet_list.html', {'pets': pets})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import PetForm  # Assuming you have a form class for handling pet details



# views.py


from django.shortcuts import render
from .models import doctor

def doc_list(request):
    doctors = doctor.objects.all()  # Fetch all doctor records
    return render(request, 'doc_list.html', {'doctors': doctors})

from django.shortcuts import render, redirect
from .models import doctor
from .forms import DoctorRegistrationForm

def doc_list(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            doctor = form.save()
            # Redirect to the details page after successful registration
            return redirect('doc_list', name=doctor.name)
    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctorreg.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm

def doc_list(request, name):
    doctors = get_object_or_404(doctor, name=name)
    return render(request, 'doc_list.html', {'doctor': doctor})
def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()  # Save the doctor details to the database
            print("Doctor saved successfully")
            return redirect('doc_list')  # Redirect to doctor list page after successful registration
        else:
            print("Form is not valid")
            print(form.errors)  # Print the form errors for debugging
    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctorreg.html', {'form': form})
from django.shortcuts import render, redirect
from .models import doctor
from .forms import DoctorRegistrationForm

def doc_list(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle password confirmation
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                form.save()
                return redirect('doc_list.html')
            else:
                form.add_error('confirm_password', 'Passwords do not match')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctorreg.html', {'form': form})
