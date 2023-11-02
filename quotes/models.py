from django.db import models
# Create your models here.
from PIL import Image
 
CATEGORY = [
        ('wood', 'Wood'),
        ('metal', 'Metal'),
        ('plastic', 'Plastic'),
        # Add more choices as needed
    ]
# Define a model for Window materials
class WindowMaterial(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100, unique=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name

# Define a model for Door materials
class DoorMaterial(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Define a model for Window styles
class WindowStyle(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Define a model for Door styles
class DoorStyle(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Define a model for Window sizes
class WindowSize(models.Model):
    id = models.AutoField(primary_key=True)  
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.width} x {self.height}"

# Define a model for Door sizes
class DoorSize(models.Model):
    id = models.AutoField(primary_key=True)  
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.width} x {self.height}"

# Define a model for Windows
class Window(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    material = models.ForeignKey(WindowMaterial, on_delete=models.CASCADE)
    style = models.ForeignKey(WindowStyle, on_delete=models.CASCADE)
    size = models.ForeignKey(WindowSize, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='window_images/')
    class Meta:
        verbose_name_plural = '창문들'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        max_size = (800, 800)
        img.thumbnail(max_size)
        img.save(self.image.path)

    def __str__(self):
        return f'{self.id} {self.name}  {self.material} {self.style} {self.price}  {self.image}'

# Define a model for Doors
class Door(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    material = models.ForeignKey(DoorMaterial, on_delete=models.CASCADE)
    style = models.ForeignKey(DoorStyle, on_delete=models.CASCADE)
    size = models.ForeignKey(DoorSize, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='door_images/')

    class Meta:
        verbose_name_plural = '문 '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        max_size = (800, 800)
        img.thumbnail(max_size)
        img.save(self.image.path)

    def __str__(self):
        return f'{self.id} {self.name}  {self.material} {self.style} {self.price}  {self.image}'