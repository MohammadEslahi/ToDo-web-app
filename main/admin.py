from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'checked', 'author')


admin.site.register(Task, TaskAdmin)