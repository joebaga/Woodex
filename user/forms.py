from django.contrib.auth.models import User
from .models import CustomerProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm 


class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()  # Use email as the unique field
    company_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    kakao_talk_login = forms.BooleanField(required=False, initial=False)
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', 'company_name', 'phone_number', 'kakao_talk_login')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['first_name', 'last_name','address','company_name','company_address','country_category','region','phone_number','image']