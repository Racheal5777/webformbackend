from django.contrib import admin
from .models import UserDetail

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'state', 'country','image', 'video')

# Register your models here.
