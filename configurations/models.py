from django.db import models

# Create your models here.
from django.db import models
from quotes.models import Window, Door,WindowMaterial,DoorMaterial, WindowSize,DoorSize
from user.models import CustomerProfile  # Import the CustomerProfile model

class Configuration(models.Model):
    user_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    selected_windows = models.ManyToManyField(Window)
    selected_doors = models.ManyToManyField(Door)
    selected_wndwMaterial = models.ManyToManyField(WindowMaterial)
    selected_doorMaterial = models.ManyToManyField(DoorMaterial)
    selected_wndwSize = models.ManyToManyField(WindowSize)
    selected_doorSize = models.ManyToManyField(DoorSize)

    # Add other configuration-related fields as needed

    def __str__(self):
        return f'Configuration for {self.user_profile.user.username}'