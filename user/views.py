# user/views.py
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import CustomerRegistrationForm
from .models import CustomerProfile
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            if self.request.user.is_staff and self.request.user.is_superuser:
                return redirect('admin-page') 
            else:
                return redirect('index')
        return response

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if User.objects.filter(email=email).exists():
                return render(request, 'User/error_exist.html')

            user, created = User.objects.get_or_create(email=email, defaults=form.cleaned_data)

            if not created:
                return render(request, 'User/error_exist.html')

            if not hasattr(user, 'customerprofile'):
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
            return redirect('user_register')  # Redirect to the user's profile page
    else:
        form = CustomerRegistrationForm()

    return render(request, 'User/register.html', {'form': form})
@login_required
def profile(request):
    user_profile = request.user.customerprofile
    return render(request, 'user/profile.html', {'user_profile': user_profile})


