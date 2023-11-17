from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from PIL import Image
COUNTRY_CATEGORIES = [
    ('afghanistan', 'Afghanistan'),
    ('albania', 'Albania'),
    ('algeria', 'Algeria'),
    ('south korea', 'south korea'),
    ('united states ', 'United states'),
    ('France', 'France'),
    # Add more countries as needed
]

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200, null=True)
    country_category = models.CharField(max_length=20, choices=COUNTRY_CATEGORIES, default='south korea')
    region = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15)
    kakao_talk_login = models.CharField(max_length=50)
    image = models.ImageField(default="Profile_Images/1_0_0_20161219140623097.jpg",upload_to='Profile_Images', null=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            max_size = (800, 800)
            img.thumbnail(max_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username}'