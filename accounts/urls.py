from django.urls import path
from . import views # how not to repeat this?
from .views import *


urlpatterns = [
    path('register/', CustomUserCreationView.as_view(), name='register'),
    path('edituser/<int:id>', views.CustomUserChangeView, name='edituser'),
]