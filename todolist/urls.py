from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-task/', views.add_task, name='addtask'),
    path('remove-task', views.remove_task, name='removetask'),
    path('taskup', views.task_up, name='taskup'),
    path('taskdown', views.task_down, name='taskdown'),
]