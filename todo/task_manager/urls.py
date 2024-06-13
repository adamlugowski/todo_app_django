from django.urls import path, include
from .views import tasks_list, index, add_task

urlpatterns = [
    path('', index, name='index'),
    path('tasks', tasks_list, name='tasks_list'),
    path('add_task', add_task, name='add_task')
]
