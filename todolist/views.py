from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Task


def index(request):
    t_list = Task.objects.all()
    context = {
        't_list': t_list,
    }
    return render(request, 'todolist/index.html', context)


def add_task(request):
    task_name = request.POST.get('task-name', False)
    if task_name is not False and task_name != "":
        t = Task(name=task_name)
        t.save()
    return HttpResponseRedirect(reverse('todolist:index'))


def remove_task(request):
    return HttpResponseRedirect(reverse('todolist:index'))


def task_up(request):
    return HttpResponseRedirect(reverse('todolist:index'))


def task_down(request):
    return HttpResponseRedirect(reverse('todolist:index'))
