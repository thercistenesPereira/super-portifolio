from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.site_header = "Super Portfolio Admin"
admin.site.register(Profile)
