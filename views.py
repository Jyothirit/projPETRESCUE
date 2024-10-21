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
from .forms import DoctorLoginForm
from .forms import GroomerLoginForm
from .forms import CustomLoginForm
from .models import Pet
from .models import doctor
from .models import Groomers
from .models import Message
from .models import CustomUser
from .models import Rescuer
import razorpay
from django.views.decorators.csrf import csrf_exempt

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
            return redirect('userlogin')  # Redirect to a different view after registration
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
    request.session.clear()
    request.session.flush()
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

            users = Rescuer.objects.filter(username=username, password = password).first()
            if users is not None:
                request.session['user_id'] = users.id
                request.session['username'] = users.username
                return redirect('rescuerdashboard')
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



# Register Doctor


def doctorreg(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('doctorlogin')  # Redirect to a different view after registration
    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctorreg.html', {'form': form})


def doctorlogin(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            users = doctor.objects.filter(username=username, password = password).first()
            if users is not None:
                request.session['user_id'] = users.id
                request.session['username'] = users.name
                return redirect('doctordashboard')
            else:
                return render(request, 'doctorlogin.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = DoctorLoginForm()

    return render(request, 'doctorlogin.html', {'form': form})


def doctordashboard(request):
    return render(request,'doctordashboard.html')


def doc_userchatlist(request):
    users = CustomUser.objects.all()
    return render(request, 'doc_userchatlist.html', {'users': users})



# Register Shelter, Groom



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

def groomlogin(request):
    if request.method == 'POST':
        form = GroomerLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            groomers = Groomers.objects.filter(name = name, email = email).first()
            if groomers is not None:
                request.session['user_id'] = groomers.id
                request.session['name'] = groomers.name
                return redirect('groomdashboard')
            else:
                return render(request, 'groomlogin.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = GroomerLoginForm()

    return render(request, 'groomlogin.html', {'form': form})

def groomdashboard(request):
    return render(request,'groomdashboard.html')


def groom_userchatlist(request):
    users = CustomUser.objects.all()
    return render(request, 'groom_userchatlist.html', {'users': users})

def user_chat(request, user_id):
    if request.method == 'POST':
        sender = request.user.id
        sender_cat = 1
        recever = user_id
        recever_cat = 2
        content = request.POST['content']

        sentmsg = Message(sender=sender,sender_cat=sender_cat,recever=recever,recever_cat=recever_cat,content=content)
        sentmsg.save()

        return redirect('user_chat',user_id)


    messages = Message.objects.filter(sender=request.user.id,sender_cat= 1, recever = user_id, recever_cat = 2) | Message.objects.filter(sender=user_id,sender_cat= 2, recever = request.user.id, recever_cat = 1)
    recever_name = doctor.objects.filter(id=user_id).values_list('name', flat=True).first()
    senter_name = CustomUser.objects.filter(id=request.user.id).first()
    return render(request, 'user_chat.html', {'messages': messages, 'recever_id': user_id, 'recever_name': recever_name, 'senter_name': senter_name})



def doctor_chat(request, user_id):
    if request.method == 'POST':
        sender = request.session.get('user_id')
        sender_cat = 2
        recever = user_id
        recever_cat = 1
        content = request.POST['content']

        sentmsg = Message(sender=sender,sender_cat=sender_cat,recever=recever,recever_cat=recever_cat,content=content)
        sentmsg.save()

        return redirect('doctor_chat',user_id)

        

    messages = Message.objects.filter(sender=user_id,sender_cat= 1, recever = request.session.get('user_id'), recever_cat = 2) | Message.objects.filter(sender=request.session.get('user_id'),sender_cat= 2, recever = user_id, recever_cat = 1)
    recever_name = CustomUser.objects.filter(id=user_id).first()
    senter_name = doctor.objects.filter(id=request.session.get('user_id')).values_list('name', flat=True).first()
    
    return render(request, 'doctor_chat.html', {'messages': messages, 'recever_id': user_id, 'recever_name': recever_name, 'senter_name': senter_name})


def groomer_chat(request, user_id):
    if request.method == 'POST':
        sender = request.session.get('user_id')
        sender_cat = 3
        recever = user_id
        recever_cat = 1
        content = request.POST['content']

        sentmsg = Message(sender=sender,sender_cat=sender_cat,recever=recever,recever_cat=recever_cat,content=content)
        sentmsg.save()

        return redirect('groomer_chat',user_id)

        

    messages = Message.objects.filter(sender=user_id,sender_cat= 1, recever = request.session.get('user_id'), recever_cat = 3) | Message.objects.filter(sender=request.session.get('user_id'),sender_cat= 3, recever = user_id, recever_cat = 1)
    recever_name = CustomUser.objects.filter(id=user_id).first()
    senter_name = Groomers.objects.filter(id=request.session.get('user_id')).values_list('name', flat=True).first()
    
    return render(request, 'groomer_chat.html', {'messages': messages, 'recever_id': user_id, 'recever_name': recever_name, 'senter_name': senter_name})

def user_chatgroomer(request, user_id):
    if request.method == 'POST':
        sender = request.user.id
        sender_cat = 1
        recever = user_id
        recever_cat = 3
        content = request.POST['content']

        sentmsg = Message(sender=sender,sender_cat=sender_cat,recever=recever,recever_cat=recever_cat,content=content)
        sentmsg.save()

        return redirect('user_chatgroomer',user_id)


    messages = Message.objects.filter(sender=request.user.id,sender_cat= 1, recever = user_id, recever_cat = 3) | Message.objects.filter(sender=user_id,sender_cat= 3, recever = request.user.id, recever_cat = 1)
    recever_name = Groomers.objects.filter(id=user_id).values_list('name', flat=True).first()
    senter_name = CustomUser.objects.filter(id=request.user.id).first()
    return render(request, 'user_chatgroomer.html', {'messages': messages, 'recever_id': user_id, 'recever_name': recever_name, 'senter_name': senter_name})


def proceedtopay(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'proceedtopay.html', {'pet': pet})
def payment(request,pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method =='POST':
        amount=50000
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_edrzdb8Gbx5U5M','XgwjnFvJQNG6cS7Q13aHKDJj'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request, 'payment.html',{'pet': pet})

def paymentsuccess(request):
    
    return render(request, 'paymentsuccess.html')

def user_donation(request):
    return render(request, 'user_donation.html')

def search_pets(request):
    query = request.GET.get('q')  # 'q' is the name of the input field in the form
    if query:
        pets = Pet.objects.filter(breed__icontains=query) | Pet.objects.filter(location__icontains=query) | Pet.objects.filter(breed__icontains=query)
    else:
        pets = Pet.objects.all()
    return render(request, 'search_pets.html', {'pets': pets})

def donation(request):
    if request.method =='POST':
        amount=50000
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_edrzdb8Gbx5U5M','XgwjnFvJQNG6cS7Q13aHKDJj'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request, 'donation.html')