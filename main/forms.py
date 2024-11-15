from django import forms
from .models import *


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['text', 'image']