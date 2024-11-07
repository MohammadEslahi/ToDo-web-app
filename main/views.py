from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth.decorators import login_required




def homeView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ToDoListForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                ToDoItem.objects.create(text=cd['text'], author=request.user)
                return HttpResponseRedirect("/")
        else:
            return render(request, 'main.html', {'ToDoItem':ToDoItem.objects.filter(author=request.user), 'ToDoListForm':ToDoListForm()})
    else:
        return render(request, 'main.html', {})


def deleteView(request, id):
    if request.user==ToDoItem.objects.get(id=id).author:
        obj = get_object_or_404(ToDoItem, id = id)
        if request.method == 'POST':
            obj.delete()
            return HttpResponseRedirect("/")
        
        return render(request, 'delete.html',{'ToDoItem':ToDoItem.objects.get(id=id)})
    else:
        return HttpResponse("You are not elligible to delete this item")

def updateView(request, id):
    if request.user==ToDoItem.objects.get(id=id).author:
        obj = ToDoItem.objects.get(id=id)
        if request.method == 'POST':
            form = ToDoListForm(request.POST, instance = obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, 'update.html', {'ToDoListForm':ToDoListForm(instance=obj)})
        
        return render(request, 'update.html', {})
    else:
        return HttpResponse("You are not elligible to edit this item")



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