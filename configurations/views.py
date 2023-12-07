# config/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from Woodex.WoodexWeb.configurations.forms import ConfigurationForm
from xhtml2pdf import pisa
from .models import Configuration
from user.models import CustomerProfile

def configure(request):
    user_profile = CustomerProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        conf_form = ConfigurationForm(request.POST)
        if conf_form.is_valid():
            configuration = conf_form.save(commit=False)
            configuration.user_profile = user_profile
            configuration.save()
            
            return redirect('generate_pdf')  # Redirect to PDF generation view
    else:
        conf_form = ConfigurationForm(initial={'user_profile': user_profile})

    return render(request, 'conf.html', {'form': conf_form, 'user_profile': user_profile})

def generate_pdf(request):
    user_profile = CustomerProfile.objects.get(user=request.user)
    configuration = Configuration.objects.get(user_profile=user_profile)

    template_path = 'pdf_template.html'
    context = {'user_profile': user_profile, 'configuration': configuration}
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="configuration.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response
