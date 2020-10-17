from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

#changing layout inbuilt admin dashboard
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_staff', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)    
