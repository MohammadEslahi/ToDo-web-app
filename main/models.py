from django.db import models
from accounts.models import *




class ToDoItem(models.Model):
    text = models.CharField(max_length=20)
    checked = models.BooleanField(default=False)
    author = models.ForeignKey (CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text