from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class RescuerRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
# forms.py
from django import forms
from django.contrib.auth.models import User

class RescuerLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class DoctorRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    speciality = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
# pet_app/forms.py
from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['breed', 'colour', 'age', 'identification', 'location']

from django import forms
from .models import doctor

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = doctor
        fields = ['name', 'speciality', 'email', 'contact', 'password', 'certificate']


