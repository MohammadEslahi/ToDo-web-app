from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.views.generic import *

def homeView(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ToDoItem.objects.create(text=cd['text'], author=request.user)
            return HttpResponseRedirect("/")
    else:
        return render(request, 'main.html', {'ToDoItem':ToDoItem.objects.all(), 'ToDoListForm':ToDoListForm()})


def deleteView(request, id):
    obj = get_object_or_404(ToDoItem, id = id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request, 'delete.html',{'ToDoItem':ToDoItem.objects.get(id=id)})


def updateView(request, id):
    obj = ToDoItem.objects.get(id=id)
    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        return render(request, 'update.html', {'ToDoListForm':ToDoListForm(instance=obj)})
    
    return render(request, 'update.html', {})



def checkerView(request, id):
    # if request.method == 'POST':
    obj = ToDoItem.objects.get(id=id)
    obj.checked = True
    obj.save()
    return HttpResponseRedirect('/')


def uncheckerView(request, id):
    obj = ToDoItem.objects.get(id=id)
    obj.checked = False
    obj.save()
    return HttpResponseRedirect('/')