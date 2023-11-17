from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            if self.request.user.is_staff and self.request.user.is_superuser:
                return redirect('admin-page')  # Replace 'admin-page' with the actual URL name of your admin page
            else:
                return redirect('index')
        return response
def is_admin(user):
    return user.is_authenticated and user.is_staff and user.is_superuser

@user_passes_test(is_admin, login_url='/user-login/')
def adm(request):
    print(request.user.is_authenticated)  # Check if the user is authenticated
    print(request.user.is_staff)         # Check if the user is staff
    print(request.user.is_superuser)     # Check if the user is a superuser
    return render(request, 'Home/adm.html')

@login_required(login_url='user-login') #to secure our app so that anyone who knows the url cant just access it 
def index(request):
    return render(request, 'Home/index.html')

@login_required(login_url='user-login')
def quotes(request):
    return render(request, 'Home/quotes.html')

@login_required(login_url='user-login')
def config(request):
    return render(request, 'Home/conf.html')

def price(request):
    return render(request,'Home/price.html' )

