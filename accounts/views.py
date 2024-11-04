from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *

class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')


def CustomUserChangeView(request, id):
    obj = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        return render(request, 'edituser.html',{'form':CustomUserChangeForm(instance=obj)})
    return render(request, 'edituser.html',{'form':CustomUserChangeForm(instance=obj),'CustomUser':CustomUser.objects.all()})