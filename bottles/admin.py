from django.contrib import admin
from .models import Bottle

class BottleAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_count', 'end_count']
    pass
admin.site.register(Bottle, BottleAdmin)
