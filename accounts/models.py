from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username