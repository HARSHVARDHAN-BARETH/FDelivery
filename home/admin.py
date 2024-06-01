from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=("name", "price", "description")
admin.site.register(Product,ProductAdmin)
# Register your models here.
admin.site.register(Profile)