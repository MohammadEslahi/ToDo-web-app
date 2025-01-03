from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'name', 'category','priority', 'image']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    
    name = forms.CharField(required=False)