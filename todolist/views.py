from django.http import HttpResponseRedirect, Http404
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
    t_id = request.POST.get('erase', False)
    if t_id is not False:
        task_id = int(t_id)
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
        except Task.DoesNotExist:
            raise Http404("Tarea no existe")

    return HttpResponseRedirect(reverse('todolist:index'))


def task_up(request):
    t_id = request.POST.get('up', False)
    if t_id is not False:
        task_id = int(t_id)
        try:
            task = Task.objects.get(id=task_id)
            try:
                prev_id = task_id - 1
                prev_task = Task.objects.get(id=prev_id)
                task.id = prev_id
                prev_task.id = task_id
                task.save()
                prev_task.save()
            except (KeyError, Task.DoesNotExist):
                raise render(request, 'todolist/index.html', {
                    'error_message': "Tarea no puede ser subida"
                })
        except Task.DoesNotExist:
            raise Http404("Tarea no existe")
    return HttpResponseRedirect(reverse('todolist:index'))


def task_down(request):
    t_id = request.POST.get('down', False)
    if t_id is not False:
        task_id = int(t_id)
        try:
            task = Task.objects.get(id=task_id)
            try:
                next_id = task_id + 1
                next_task = Task.objects.get(id=next_id)
                task.id = next_id
                next_task.id = task_id
                task.save()
                next_task.save()
            except (KeyError, Task.DoesNotExist):
                raise render(request, 'todolist/index.html', {
                    'error_message': "Tarea no puede ser bajada"
                })
        except Task.DoesNotExist:
            raise Http404("Tarea no existe")
    return HttpResponseRedirect(reverse('todolist:index'))
