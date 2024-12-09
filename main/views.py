from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth.decorators import login_required




def homeView(request):
    if request.user.is_authenticated:
        form = TaskForm(request.POST, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                new_instance = form.save(commit=False)
                new_instance.author = request.user
                new_instance.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, 'main.html', {'Task':Task.objects.filter(author=request.user), 'TaskForm':TaskForm})
    else:
        return render(request, 'main.html', {})


def deleteView(request, id):
    if request.user==Task.objects.get(id=id).author:
        obj = get_object_or_404(Task, id = id)
        if request.method == 'POST':
            obj.delete()
            return HttpResponseRedirect("/")
        
        return render(request, 'delete.html',{'Task':Task.objects.get(id=id)})
    else:
        return HttpResponse("You are not elligible to delete this item")

def updateView(request, id):
    if request.user==Task.objects.get(id=id).author:
        obj = Task.objects.get(id=id)
        if request.method == 'POST':
            form = TaskForm(request.POST, request.FILES, instance = obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, 'update.html', {'TaskForm':TaskForm(instance=obj), 'obj':obj})
        
        return render(request, 'update.html', {'obj':obj})
    else:
        return HttpResponse("You are not elligible to edit this item")


# for checking tasks
def checkerView(request, id):
    obj = Task.objects.get(id=id)
    obj.checked = True
    obj.save()
    return HttpResponseRedirect('/')


def uncheckerView(request, id):
    obj = Task.objects.get(id=id)
    obj.checked = False
    obj.save()
    return HttpResponseRedirect('/')