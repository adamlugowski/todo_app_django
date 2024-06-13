from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def tasks_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_manager/tasks_list.html', context=context)


def index(request):
    return render(request, 'task_manager/index.html')


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'task_manager/add_task.html', {'form': form})
