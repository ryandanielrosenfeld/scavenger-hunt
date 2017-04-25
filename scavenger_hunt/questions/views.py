from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from .models import Task
from .services import activate_song
from .selenium_board_control import activate_board


def task1(request):
    print("task 1")
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
    print("task 1 activate")
    t = Task.objects.get(number=1)
    t.activate = True
    t.save()
    return HttpResponseRedirect('/task1/')


def task2(request):
    print("task 2")
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
            if request.POST['answer'].lower() == 'apple':
                correct = True
                activated = True
                request.user.task_num = 3
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task2.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task2.html', {'form': form, 'activated': activated})

def task2_activate(request):
    print("task 2 activate")
    t = Task.objects.get(number=2)
    t.activate = True
    t.save()
    user = request.user
    name = user.first_name
    activate_board(name)
    return HttpResponseRedirect('/task2/')


def task3(request):
    form = Task1Form()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 1:
        activated = True
    # else:
    #     request.user.task_num = 1
    #     request.user.save()
    # if request.method == 'POST':
    #     form = Task1Form(request.POST)
    #     if form.is_valid():
    #         if request.POST['answer'] == '1924':
    #             correct = True
    #             activated = True
    #             request.user.task_num = 2
    #             request.user.save()
    #         else:
    #             incorrect = True
    #         return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
    #                                               'activated': activated})
    return render(request, 'task3.html', {'form': form, 'activated': activated})


def task3_activate(request):
    activate_song()
    return HttpResponseRedirect('/task3/')
