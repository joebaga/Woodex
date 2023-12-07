from django import forms
from .models import Configuration

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ['selected_windows', 'selected_doors','WindowMaterial','DoorMaterial','WindowStyle','DoorStyle','WindowSize','DoorSize']

    