from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name='index'),
    path('quotes/',views.quotes, name='quotes-page'),
    path('config/',views.config, name='config'),
    path('price/',views.price, name='price'),
    path('download_csv/<str:product_type>/', views.download_csv, name='download_csv'),
    path('order/',views.order, name='order'),
    path('adm/',views.adm, name='adm'),
]