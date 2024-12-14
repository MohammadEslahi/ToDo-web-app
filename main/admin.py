from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'checked', 'date_created')
    readonly_fields = ('date_created',)  # makes 'date_created' read-only (otherwise an error raises)
    fields = ('name', 'category', 'priority', 'checked', 'date_created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)

    

admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)