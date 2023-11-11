from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name='index'),
    path('quotes/',views.quotes, name='quotes-page'),
    path('price/',views.price, name='price-page'),
    path('order/',views.order, name='order-page'),
    #path('info/',views.price, name='info-page'),
    path('config/',views.config, name='config')
]