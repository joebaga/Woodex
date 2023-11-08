from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    kakao_talk_login = models.CharField(max_length=50)