from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name='index'),
    path('quotes/',views.quotes, name='quotes-page'),
    path('config/',views.config, name='config'),
    path('price/',views.price, name='price'),
    path('adm/',views.adm, name='adm'),
]