from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth.decorators import login_required




def TasksView(request):
    if request.user.is_authenticated:
        obj = Task.objects.filter(author=request.user).order_by('-priority', '-date_created') # two-factor-sorting
        form = TaskForm(request.POST, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                new_instance = form.save(commit=False)
                new_instance.author = request.user
                new_instance.save()
                return HttpResponseRedirect("/")
            else:
                return render(request, 'main.html', {'Task':obj, 'TaskForm':form})
        else:
            return render(request, 'main.html', {'Task':obj, 'TaskForm':TaskForm})


def deleteView(request, id):
    obj = get_object_or_404(Task, id=id)
    if request.user== obj.author:
        if request.method == 'POST':
            obj.delete()
            return HttpResponseRedirect("/")
        
        return render(request, 'delete.html',{'Task':obj})
    else:
        return HttpResponse("You are not elligible to delete this item")

def updateView(request, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST, request.FILES)
    if request.user==obj.author:
        if request.method == 'POST':
            form = TaskForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
            else:
                return render(request, 'update.html', {'TaskForm':form(instance=obj), 'obj':obj})

        else:
            return render(request, 'update.html', {'TaskForm':TaskForm(instance=obj), 'obj':obj})
    else:
        return HttpResponse("You are not elligible to edit this item")


# for checking tasks
def checkerView(request, id):
    obj = get_object_or_404(Task, id=id)
    obj.checked = True
    obj.save()
    return HttpResponseRedirect('/')


def uncheckerView(request, id):
    obj = get_object_or_404(Task, id=id)
    obj.checked = False
    obj.save()
    return HttpResponseRedirect('/')