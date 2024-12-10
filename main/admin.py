from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'priority', 'checked', 'date_created')
    readonly_fields = ('date_created',)  # makes 'date_created' read-only (otherwise an error raises)
    fields = ('text', 'author', 'priority', 'checked', 'date_created')
    

admin.site.register(Task, TaskAdmin)