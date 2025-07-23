#from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Task


# Create your views here.

def addTask(request):
    task = request.POST['task'] # name='task' -> home.hmtl
    Task.objects.create(task=task)
    return redirect('home')