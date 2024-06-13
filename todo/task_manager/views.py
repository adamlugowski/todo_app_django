from django.shortcuts import render
from .models import Task


def tasks_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_manager/tasks_list.html', context=context)
