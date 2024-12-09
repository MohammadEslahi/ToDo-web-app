from django.db import models
from accounts.models import *




class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high','high')
    ]
    text = models.CharField(max_length=20)
    checked = models.BooleanField(default=False)
    author = models.ForeignKey (CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='taskimages/', blank=True, null=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')

    def __str__(self):
        return self.text