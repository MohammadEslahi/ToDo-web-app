from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age','profile_image')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'age', 'profile_image', 'email']