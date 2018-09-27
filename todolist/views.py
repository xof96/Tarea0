from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Task


def index(request, err_me=None):
    error_message = err_me
    t_list = Task.objects.order_by('priority')
    context = {
        't_list': t_list,
    }
    if error_message is not None:
        context['error_message'] = error_message
    return render(request, 'todolist/index.html', context)


def add_task(request):
    task_name = request.POST.get('task-name', False)
    if task_name is not False and task_name != "":
        p = len(Task.objects.all()) + 1
        t = Task(name=task_name, priority=p)
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
            task_p = task.priority
            try:
                prev_p = task_p - 1
                prev_task = Task.objects.get(priority=prev_p)
                task.priority = prev_p
                prev_task.priority = task_p
                task.save()
                prev_task.save()
            except (KeyError, Task.DoesNotExist):
                return HttpResponseRedirect(reverse('todolist:index'))
        except Task.DoesNotExist:
            raise Http404("Tarea no existe")
    return HttpResponseRedirect(reverse('todolist:index'))


def task_down(request):
    t_id = request.POST.get('down', False)
    if t_id is not False:
        task_id = int(t_id)
        try:
            task = Task.objects.get(id=task_id)
            task_p = task.priority
            try:
                next_p = task_p + 1
                next_task = Task.objects.get(priority=next_p)
                task.priority = next_p
                next_task.priority = task_p
                task.save()
                next_task.save()
            except (KeyError, Task.DoesNotExist):
                return HttpResponseRedirect(reverse('todolist:index'))
        except Task.DoesNotExist:
            raise Http404("Tarea no existe")
    return HttpResponseRedirect(reverse('todolist:index'))
