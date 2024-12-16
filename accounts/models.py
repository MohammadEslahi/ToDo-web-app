from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True, default='profile_image/default_profile_image.jpg')
    
    def __str__(self):
        return self.username