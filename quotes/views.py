import os
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from user.models import CustomerProfile
from .models import Window, Door
import csv
import pandas as pd

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
@login_required(login_url='user-login')
def price(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, 'excel_file/firstExcel.xlsx')

    try:
        # Specify the sheet name you want to read
        sheet_name = '임가공 단가표'
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        data = df.to_dict(orient='records')
    except FileNotFoundError:
        data = []  # Handle the case where the file is not found
    except pd.errors.EmptyDataError:
        data = []  # Handle the case where the specified sheet is empty

    return render(request, 'Home/price.html', {'data': data})

@login_required(login_url='user-login')
def download_csv(request, product_type):
    if product_type == 'windows':
        products = Window.objects.all()
        filename = 'windowPrices.xlsx'
    elif product_type == 'doors':
        products = Door.objects.all()
        filename = 'doorPrices.xlsx'
    else:
        # Handle invalid product type (optional)
        return HttpResponse("Invalid product type specified")

    # Convert queryset to a pandas DataFrame
    df = pd.DataFrame(list(products.values()))

    # Create Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    df.to_excel(response, index=False, sheet_name='Products')

    return response

@login_required(login_url='user-login')
def order(request):
    return render(request,'Home/order.html' )
