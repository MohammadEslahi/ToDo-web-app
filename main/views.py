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
        checked_tasks = tasks.filter(checked=True)
        unchecked_tasks = tasks.filter(checked=False)
        print (checked_tasks, unchecked_tasks)

        # handling new task form
        categories = Category.objects.filter(author=request.user)
        task_form = TaskForm(request.POST, request.FILES)
        task_form.fields['category'].queryset = categories

        # Handle filtering by category
        category_filter = request.GET.get('category_filter')
        if category_filter:
            tasks = tasks.filter(category__name=category_filter)


        if request.method == 'POST':
            if request.POST.get('name') == '':
                    messages.warning(request,'Task name is required')
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.author = request.user
                # ensuring at least a default 'general' category is created
                if not new_task.category:
                    try:
                        Category.objects.get(name="general")
                    except:
                        Category.objects.create(name="general", author=request.user)
                    new_task.category= Category.objects.get(name="general")
                new_task.save()
                messages.success(request, 'New task successfully added!')
                return redirect('home')
            else:
                return render(request, 'main.html', {'tasks':tasks, 'task_form':task_form, 'categories':categories, 'checked_tasks':checked_tasks, 'unchecked_tasks':unchecked_tasks})
        else:
            return render(request, 'main.html', {'tasks':tasks, 'task_form':TaskForm, 'categories':categories})
        
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
            if 'Delete_task_image' in request.POST:
                obj.image.delete()
                messages.success(request, 'Task image removed')
                return redirect('update', id)
        

            form = TaskForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.author = request.user
                # ensuring at least a default 'general' category is created
                if not new_task.category:
                    try:
                        Category.objects.get(name="general")
                    except:
                        Category.objects.create(name="general", author=request.user)
                    new_task.category= Category.objects.get(name="general")
                new_task.save()
                messages.success(request, 'Task successfully edited!')
                return redirect('home')
            else:
                return render(request, 'update.html', {'TaskForm':form(instance=obj), 'obj':obj})

        else:
            form = TaskForm(instance=obj)
            form.fields['category'].queryset = categories
            return render(request, 'update.html', {'TaskForm':form, 'obj':obj, 'categories':categories})
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
    categories = Category.objects.filter(author=request.user)
    add_category_form = AddCategoryForm(request.POST)
    new_category = request.POST.get('name')
    if request.method == 'POST':
        # manually checking some errors
        if categories.filter(name=new_category).exists():
            messages.error(request, 'Category already exists')
        elif new_category=='general':
            messages.error(request, '"general" category is added by default :)')
        elif new_category=='':
            messages.error(request, 'please enter a NAME for the category.')
        elif 'delete_category' in request.POST:
            delete_category = get_object_or_404(Category, id=id)
            if delete_category.author == request.user:
                delete_category.delete()
                messages.success(request, 'Category deleted')
            
        else:
            if add_category_form.is_valid():
                my_category= add_category_form.save(commit=False)
                my_category.author = request.user
                my_category.save()
                messages.success(request, 'New Category added')
    return render(request, 'categories.html', {'categories':categories, 'add_category_form':add_category_form})