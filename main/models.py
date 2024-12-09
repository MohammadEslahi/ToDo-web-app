from django.db import models
from accounts.models import *




class Task(models.Model):
    text = models.CharField(max_length=20)
    checked = models.BooleanField(default=False)
    author = models.ForeignKey (CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='todoimages/', blank=True, null=True)

    def __str__(self):
        return self.text