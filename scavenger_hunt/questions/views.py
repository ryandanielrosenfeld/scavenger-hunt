from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from .models import Task


def task1(request):
    form = Task1Form()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 1:
        activated = True
    else:
        request.user.task_num = 1
        request.user.save()
    if request.method == 'POST':
        form = Task1Form(request.POST)
        if form.is_valid():
            if request.POST['answer'] == '1924':
                correct = True
                activated = True
                request.user.task_num = 2
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task1.html', {'form': form, 'activated': activated})


def task1_activate(request):
    t = Task.objects.get(number=1)
    t.activate = True
    t.save()
    return render(request, 'task1.html', {'activated', True})


def task2(request):
    form = Task2Form()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 2:
        activated = True
    elif request.user.task_num < 2:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = Task2Form(request.POST)
        if form.is_valid():
            if request.POST['answer'] == '1924':
                correct = True
                activated = True
                request.user.task_num = 3
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task2.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task2.html', {'form': form, 'activated': activated})
