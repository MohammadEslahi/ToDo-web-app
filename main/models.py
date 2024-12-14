from django.db import models
from accounts.models import CustomUser


    

class Category(models.Model):
    name = models.CharField(max_length=10)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name_plural= 'Categories'
    def __str__(self):
        return self.name



class Task(models.Model):
    PRIORITY_CHOICES = [
        ('1-low', 'low'),
        ('2-medium', 'medium'),
        ('3-high','high')
    ]
    name = models.CharField(max_length=20)
    checked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='taskimages/', blank=True, null=True)
    priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default='low')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.name