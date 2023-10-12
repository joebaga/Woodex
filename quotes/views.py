from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, 'Home/index.html')


def quotes(request):
    return render(request, 'Home/quotes.html')

def config(request):
    return render(request, 'Home/conf.html')