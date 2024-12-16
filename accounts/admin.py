from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *


# It's how to change users' saved infos (fieldsets) or add new user (add_fieldsets)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'profile_image', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (('my fields',{'fields':('age','profile_image')}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('my fields', {'fields':('age', 'profile_image')}),)
    
admin.site.register(CustomUser, CustomUserAdmin)