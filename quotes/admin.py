from django.contrib import admin

# Register your models here.
from .models import WindowMaterial,DoorMaterial,WindowStyle,DoorStyle,WindowSize,DoorSize,Window,Door

admin.site.site_header = 'WOODEX'
class quoteAdim(admin.ModelAdmin):
    list_display = ('id', 'name','material', 'style', 'price','image')


admin.site.register(WindowMaterial)
admin.site.register(Window,quoteAdim)
admin.site.register(Door,quoteAdim)
admin.site.register(DoorMaterial)
admin.site.register(WindowStyle)
admin.site.register(DoorStyle)
admin.site.register(WindowSize)
admin.site.register(DoorSize)

