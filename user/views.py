#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#def register(request):
 #   form = UserCreationForm()
  #  return render(request,'User/register.html',{'form':form})
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.contrib.auth.models import User
from .models import CustomerProfile

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if a user with the same email already exists
            if User.objects.filter(email=email).exists():
                # Redirect to an error page or display an error message
                return render(request, 'User/error_exist.html')

            user = form.save(commit=False)
            user.save()

            # Optionally, you can save other user details to the user's profile
            customer_profile = CustomerProfile(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                company_name=form.cleaned_data['company_name'],
                phone_number=form.cleaned_data['phone_number'],
                kakao_talk_login=form.cleaned_data['kakao_talk_login']
            )
            customer_profile.save()

            login(request, user)
            return redirect('User/register.html')  
    else:
        form = CustomerRegistrationForm()
    return render(request, 'User/register.html', {'form': form})
