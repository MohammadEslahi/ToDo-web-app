from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def TasksView(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user).order_by('-priority', '-date_created') # two-factor-sorting 

        # handling new task form
        categories = Category.objects.filter(author=request.user)
        task_form = TaskForm(request.POST, request.FILES)
        task_form.fields['category'].queryset = categories

        # Handle filtering by category
        category_filter = request.GET.get('category_filter')
        if category_filter:
            tasks = tasks.filter(category__name=category_filter)


        if request.method == 'POST':
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.author = request.user
                new_task.save()
                messages.success(request, 'New task successfully added!')
                return redirect('home')
        
        return render(request, 'main.html', {'tasks':tasks, 'task_form':task_form, 'categories':categories})
    else:
        return render(request, 'main.html', {})


def deleteView(request, id):
    obj = get_object_or_404(Task, id=id)
    if request.user== obj.author:
        if request.method == 'POST':
            obj.delete()
            messages.success(request, 'Task successfully deleted!')
            return redirect('home')
        return render(request, 'delete.html',{'Task':obj})
    else:
        return HttpResponse("You are not elligible to delete this item")

def updateView(request, id):
    obj = get_object_or_404(Task, id=id)
    categories = Category.objects.filter(author=request.user)
    form = TaskForm(request.POST, request.FILES)
    form.fields['category'].queryset = categories
    if request.user==obj.author:
        if request.method == 'POST':
            form = TaskForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Task successfully edited!')
                return redirect('home')
            else:
                return render(request, 'update.html', {'TaskForm':form(instance=obj), 'obj':obj})

        else:
            form = TaskForm(instance=obj)
            form.fields['category'].queryset = categories
            return render(request, 'update.html', {'TaskForm':form, 'obj':obj})
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



def manageCategories(request, id):
    new_category = request.POST.get('name')
    categories = Category.objects.filter(author=request.user)
    add_category_form = AddCategoryForm(request.POST)
    if request.method == 'POST':
        if categories.filter(name=new_category).exists():
            messages.error(request, 'Category already exists')
        else:
            if add_category_form.is_valid():
                my_category= add_category_form.save(commit=False)
                my_category.author = request.user
                my_category.save()


            else:
                add_category_form = AddCategoryForm()
    return render(request, 'categories.html', {'categories':categories, 'add_category_form':add_category_form})