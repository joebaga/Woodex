from django.urls import path
from . import views

#Jun 페이지 추가
urlpatterns = [
    path('home/',views.index, name='index'),
    path('quotes/',views.quotes, name='quotes-page'),
    path('price/',views.price, name='price-page'),
    path('order/',views.order, name='order-page'),
    #path('info/',views.price, name='info-page'),
    path('config/',views.config, name='config-page'),
    path('customer/',views.customer, name='customer-page')
]