from django.contrib import admin

# Register your models here.
from .models import Photo,Tags

admin.site.register(Tags)
admin.site.register(Photo)