from django.contrib import admin
from .models import *

class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'checked', 'author')


admin.site.register(ToDoItem, ToDoItemAdmin)