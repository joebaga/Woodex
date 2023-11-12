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


#Jun Price 추가
@login_required(login_url='user-login')
def price(request):
    return render(request, 'Home/price.html')


#Jun Order 추가
@login_required(login_url='user-login')
def order(request):
    return render(request, 'Home/order.html')


# Jun #Info 추가
# @login_required(login_url='user-login')
# def Info(request):
#     return render(request, 'Home/info.html')

@login_required(login_url='user-login')
def config(request):
    return render(request, 'Home/conf.html')

#Jun customer 추가
@login_required(login_url='user-login')
def customer(request):
    return render(request, 'Home/customer.html')
