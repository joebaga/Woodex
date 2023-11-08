from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='user-login') #to secure our app so that anyone who knows the url cant just access it 
def index(request):
    return render(request, 'Home/index.html')

@login_required(login_url='user-login')
def quotes(request):
    return render(request, 'Home/quotes.html')

@login_required(login_url='user-login')
def config(request):
    return render(request, 'Home/conf.html')
