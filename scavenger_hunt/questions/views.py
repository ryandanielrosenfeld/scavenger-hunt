from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect


def task1(request):
    if request.user.task_num > 1:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    correct = False
    incorrect = False
    if request.method == 'POST':
        form = Task1Form(request.POST)
        if form.is_valid():
            if request.POST['answer'] == '1924':
                correct = True
                request.user.activate = True
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect})
    form = Task1Form()
    request.user.task_num = 1
    request.user.save()
    return render(request, 'task1.html', {'form': form})


def task2(request):
    if request.user.task_num != 2:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    correct = False
    incorrect = False
    if request.method == 'POST':
        form = Task2Form(request.POST)
        if form.is_valid():
            if request.POST['answer'] == '1924':
                correct = True
                request.user.activate = True
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task2.html', {'form': form, 'correct': correct, 'incorrect': incorrect})
    form = Task1Form()
    request.user.task_num = 2
    request.user.save()
    return render(request, 'task2.html', {'form': form})
