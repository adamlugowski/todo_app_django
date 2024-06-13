from django.urls import path, include
from .views import tasks_list

urlpatterns = [
    path('tasks', tasks_list)
]
