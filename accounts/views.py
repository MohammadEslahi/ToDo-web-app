from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import *

class CustomUserCreationView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    success_message = 'Account created successfully!'


def CustomUserChangeView(request, id):
    user = get_object_or_404(CustomUser, id=id)
    form = CustomUserChangeForm(request.POST, request.FILES, instance = user)

    if request.user.id != id:
        messages.error(request, "It's not your account!")
        return redirect('home')

    if request.method == 'POST':
        if 'Delete profile image' in request.POST:
            user.profile_image = 'profile_image/default_profile_image.jpg'
            user.save()
            messages.success(request, 'Profile image removed')
            return redirect('edituser', id)
            
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully edited!')
            return redirect('home')
    else:
        form =  CustomUserChangeForm(instance = user)
    return render(request, 'edituser.html',{'form':CustomUserChangeForm(instance=user),'CustomUser':user})