from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


def home(request):
    tasks = Task.objects
    return render(request, 'schedule/home.html', {'tasks': tasks})


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'schedule/detail.html', {'task': task})


def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['description'] and request.POST['time'] and request.POST['date'] and request.POST['location']:
            task = Task()
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.time = request.POST['time']
            task.date = request.POST['date']
            task.location = request.POST['location']
            task.save()
            return redirect('home')
        else:
            return render(request, 'schedule/create.html', {'error': 'All fields are required!!'})
    else:
        return render(request, 'schedule/create.html')


def delete(request):
    if request.method == 'POST':
        selected_task = get_object_or_404(Task, pk=request.POST['task'])
        selected_task.delete()
        return redirect('home')

    else:
        tasks = Task.objects
        return render(request, 'schedule/delete.html', {'tasks': tasks})


