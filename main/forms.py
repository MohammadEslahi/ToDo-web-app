from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['category', 'name', 'image', 'priority']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    
    name = forms.CharField(required=False)